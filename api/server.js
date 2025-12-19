import express from 'express';
import { createServer } from 'http';
import { Server } from 'socket.io';
import cors from 'cors';

const app = express();

app.use(cors());
app.use(express.json());

// Store rooms and their data
const rooms = new Map();
const userSockets = new Map();

// Room class
class ChatRoom {
  constructor(id, name) {
    this.id = id;
    this.name = name;
    this.users = new Map();
    this.createdAt = Date.now();
  }

  addUser(socketId, username) {
    this.users.set(socketId, username);
  }

  removeUser(socketId) {
    this.users.delete(socketId);
  }

  getUserCount() {
    return this.users.size;
  }

  isEmpty() {
    return this.users.size === 0;
  }

  getUsernames() {
    return Array.from(this.users.values());
  }
}

// Generate unique IDs
function generateId() {
  return Math.random().toString(36).substring(2, 11);
}

// Create HTTP server for Socket.IO
const httpServer = createServer(app);
const io = new Server(httpServer, {
  cors: {
    origin: '*',
    methods: ['GET', 'POST']
  },
  transports: ['websocket', 'polling']
});

io.on('connection', (socket) => {
  console.log(`[CONNECT] User connected: ${socket.id}`);

  // Get all rooms
  socket.on('get_rooms', (callback) => {
    const roomsList = Array.from(rooms.values()).map(room => ({
      id: room.id,
      name: room.name,
      users: room.getUserCount()
    }));
    callback(roomsList);
  });

  // Join or create a room
  socket.on('join_room', (data, callback) => {
    try {
      const { username, roomName, roomId } = data;

      let room;
      if (roomId && rooms.has(roomId)) {
        // Join existing room
        room = rooms.get(roomId);
      } else {
        // Create new room
        const newRoomId = generateId();
        room = new ChatRoom(newRoomId, roomName);
        rooms.set(newRoomId, room);
      }

      // Remove user from previous room
      if (userSockets.has(socket.id)) {
        const prevRoomId = userSockets.get(socket.id).roomId;
        const prevRoom = rooms.get(prevRoomId);
        if (prevRoom) {
          prevRoom.removeUser(socket.id);
          io.to(prevRoomId).emit('user_left', { username: userSockets.get(socket.id).username });

          if (prevRoom.isEmpty()) {
            rooms.delete(prevRoomId);
          }
        }
      }

      // Add user to new room
      room.addUser(socket.id, username);
      userSockets.set(socket.id, { username, roomId: room.id });

      // Join socket to room
      socket.join(room.id);

      // Notify others
      socket.to(room.id).emit('user_joined', { username });
      io.to(room.id).emit('room_users', room.getUserCount());

      callback({
        success: true,
        room: {
          id: room.id,
          name: room.name,
          users: room.getUserCount()
        }
      });

      console.log(`[JOIN] ${username} joined room: ${room.name}`);
    } catch (error) {
      console.error('[ERROR]', error);
      callback({ success: false, message: error.message });
    }
  });

  // Send message
  socket.on('send_message', (data) => {
    try {
      const { message, roomId } = data;
      const userInfo = userSockets.get(socket.id);

      if (!userInfo || userInfo.roomId !== roomId) {
        socket.emit('message_error', 'You are not in this room');
        return;
      }

      if (!message || message.trim().length === 0) {
        return;
      }

      const room = rooms.get(roomId);
      if (!room) {
        socket.emit('message_error', 'Room not found');
        return;
      }

      io.to(roomId).emit('new_message', {
        username: userInfo.username,
        message: message.trim(),
        timestamp: Date.now()
      });

      console.log(`[MESSAGE] ${userInfo.username} in ${room.name}: ${message.substring(0, 50)}`);
    } catch (error) {
      console.error('[ERROR]', error);
      socket.emit('message_error', 'Failed to send message');
    }
  });

  // Leave room
  socket.on('leave_room', (data) => {
    try {
      const { roomId } = data;
      const userInfo = userSockets.get(socket.id);

      if (!userInfo) return;

      const room = rooms.get(roomId);
      if (room) {
        room.removeUser(socket.id);
        socket.to(roomId).emit('user_left', { username: userInfo.username });

        if (room.isEmpty()) {
          rooms.delete(roomId);
          console.log(`[DESTROY] Room destroyed: ${room.name}`);
        } else {
          io.to(roomId).emit('room_users', room.getUserCount());
        }
      }

      userSockets.delete(socket.id);
      socket.leave(roomId);

      console.log(`[LEAVE] ${userInfo.username} left room: ${roomId}`);
    } catch (error) {
      console.error('[ERROR]', error);
    }
  });

  // Disconnect
  socket.on('disconnect', () => {
    try {
      const userInfo = userSockets.get(socket.id);
      if (userInfo) {
        const room = rooms.get(userInfo.roomId);
        if (room) {
          room.removeUser(socket.id);
          io.to(userInfo.roomId).emit('user_left', { username: userInfo.username });

          if (room.isEmpty()) {
            rooms.delete(userInfo.roomId);
            console.log(`[DESTROY] Room destroyed: ${room.name}`);
          } else {
            io.to(userInfo.roomId).emit('room_users', room.getUserCount());
          }
        }
        userSockets.delete(socket.id);
      }
      console.log(`[DISCONNECT] User disconnected: ${socket.id}`);
    } catch (error) {
      console.error('[ERROR]', error);
    }
  });
});

// Health check endpoints
app.get('/', (req, res) => {
  res.json({ status: 'ok', message: 'Clackr server is running' });
});

app.get('/api/health', (req, res) => {
  res.json({
    status: 'ok',
    rooms: rooms.size,
    activeUsers: userSockets.size
  });
});

export default app;
