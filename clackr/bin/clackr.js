#!/usr/bin/env node

import { io } from 'socket.io-client';
import chalk from 'chalk';
import figlet from 'figlet';
import inquirer from 'inquirer';
import { createInterface } from 'readline';

const SERVER_URL = process.env.CLACKR_SERVER || 'https://clackr-server.vercel.app';

let socket = null;
let currentRoom = null;
let username = null;
let rl = null;

function showBanner() {
  console.clear();
  console.log(chalk.cyan(figlet.textSync('CLACKR', { horizontalLayout: 'default' })));
  console.log(chalk.gray('━'.repeat(50)));
  console.log(chalk.blue('  A Real-time CLI Chat Application'));
  console.log(chalk.gray('━'.repeat(50)));
  console.log();
}

async function getUsername() {
  const answers = await inquirer.prompt([
    {
      type: 'input',
      name: 'username',
      message: 'Enter your username:',
      default: `User${Math.floor(Math.random() * 10000)}`,
      validate: (input) => input.trim().length > 0 || 'Username cannot be empty'
    }
  ]);
  return answers.username.trim();
}

async function connectToServer() {
  return new Promise((resolve, reject) => {
    socket = io(SERVER_URL, {
      reconnection: true,
      reconnectionDelay: 1000,
      reconnectionDelayMax: 5000,
      reconnectionAttempts: 5,
      transports: ['websocket', 'polling']
    });

    socket.on('connect', () => {
      console.log(chalk.green('✓ Connected to server'));
      resolve();
    });

    socket.on('connect_error', (error) => {
      console.error(chalk.red('✗ Connection error:'), error.message);
      reject(error);
    });

    socket.on('disconnect', () => {
      console.log(chalk.yellow('⚠ Disconnected from server'));
    });

    socket.on('error', (error) => {
      console.error(chalk.red('✗ Error:'), error);
    });

    setTimeout(() => reject(new Error('Connection timeout')), 10000);
  });
}

async function getRoomsList() {
  return new Promise((resolve) => {
    socket.emit('get_rooms', (rooms) => {
      resolve(rooms || []);
    });
  });
}

async function selectOrCreateRoom() {
  const rooms = await getRoomsList();
  
  const choices = rooms.map(room => ({
    name: `${room.name} (${room.users} user${room.users !== 1 ? 's' : ''})`,
    value: room.id
  }));
  
  choices.push(new inquirer.Separator());
  choices.push({
    name: '➕ Create New Room',
    value: 'CREATE_NEW'
  });

  const answers = await inquirer.prompt([
    {
      type: 'list',
      name: 'room',
      message: 'Select a room or create a new one:',
      choices: choices.length > 1 ? choices : [
        { name: '➕ Create New Room', value: 'CREATE_NEW' }
      ]
    }
  ]);

  if (answers.room === 'CREATE_NEW') {
    const roomAnswer = await inquirer.prompt([
      {
        type: 'input',
        name: 'roomName',
        message: 'Enter room name:',
        default: `Room${Math.floor(Math.random() * 10000)}`,
        validate: (input) => input.trim().length > 0 || 'Room name cannot be empty'
      }
    ]);
    return { name: roomAnswer.roomName.trim(), id: null };
  }

  const selectedRoom = rooms.find(r => r.id === answers.room);
  return { name: selectedRoom.name, id: selectedRoom.id };
}

function joinRoom(roomName, roomId) {
  return new Promise((resolve, reject) => {
    socket.emit('join_room', { username, roomName, roomId }, (response) => {
      if (response.success) {
        currentRoom = response.room;
        console.log(chalk.green(`\n✓ Joined room: ${chalk.bold(currentRoom.name)}`));
        console.log(chalk.gray(`Room ID: ${currentRoom.id}`));
        console.log(chalk.gray(`Users in room: ${currentRoom.users}`));
        console.log(chalk.gray('Type messages and press Enter. Type /leave to exit.\n'));
        resolve();
      } else {
        reject(new Error(response.message || 'Failed to join room'));
      }
    });
  });
}

function setupMessageHandlers() {
  socket.on('user_joined', (data) => {
    if (rl.terminal) {
      console.log(chalk.yellow(`\n→ ${data.username} joined the room`));
      rl.prompt();
    }
  });

  socket.on('user_left', (data) => {
    if (rl.terminal) {
      console.log(chalk.yellow(`\n← ${data.username} left the room`));
      rl.prompt();
    }
  });

  socket.on('room_users', (count) => {
    if (currentRoom) {
      currentRoom.users = count;
    }
  });

  socket.on('new_message', (data) => {
    if (rl.terminal) {
      const time = new Date(data.timestamp).toLocaleTimeString();
      const isOwn = data.username === username;
      const prefix = isOwn ? chalk.cyan('You') : chalk.magenta(data.username);
      console.log(`\n${chalk.gray(`[${time}`)} ${prefix}${chalk.gray(']:')} ${data.message}`);
      rl.prompt();
    }
  });

  socket.on('message_error', (error) => {
    console.log(chalk.red(`\n✗ ${error}`));
    if (rl.terminal) rl.prompt();
  });

  socket.on('room_destroyed', () => {
    console.log(chalk.red('\n✗ Room has been destroyed (everyone left)'));
    socket.disconnect();
    process.exit(0);
  });
}

function startChatInterface() {
  rl = createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: true
  });

  rl.on('line', (input) => {
    const message = input.trim();

    if (message === '/leave') {
      console.log(chalk.yellow('Leaving room...'));
      socket.emit('leave_room', { roomId: currentRoom.id });
      socket.disconnect();
      process.exit(0);
    } else if (message === '/rooms') {
      getRoomsList().then(rooms => {
        console.log(chalk.cyan('\nAvailable Rooms:'));
        if (rooms.length === 0) {
          console.log(chalk.gray('No rooms available'));
        } else {
          rooms.forEach(room => {
            console.log(`  ${room.name} (${room.users} users)`);
          });
        }
        if (rl.terminal) rl.prompt();
      });
    } else if (message === '/help') {
      console.log(chalk.cyan('\nAvailable Commands:'));
      console.log('  /rooms - List all available rooms');
      console.log('  /help  - Show this help message');
      console.log('  /leave - Leave the current room and exit');
      console.log(chalk.gray('Just type a message and press Enter to send\n'));
      if (rl.terminal) rl.prompt();
    } else if (message.length > 0) {
      socket.emit('send_message', { message, roomId: currentRoom.id });
    }
  });

  rl.on('close', () => {
    if (currentRoom) {
      socket.emit('leave_room', { roomId: currentRoom.id });
    }
    socket.disconnect();
    process.exit(0);
  });

  rl.setPrompt(chalk.blue('\nYou: '));
  rl.prompt();
}

async function main() {
  try {
    showBanner();

    username = await getUsername();
    console.log(chalk.green(`\nWelcome, ${chalk.bold(username)}!`));

    console.log(chalk.cyan('\nConnecting to server...'));
    await connectToServer();

    const room = await selectOrCreateRoom();
    await joinRoom(room.name, room.id);

    setupMessageHandlers();
    startChatInterface();
  } catch (error) {
    console.error(chalk.red('✗ Error:'), error.message);
    process.exit(1);
  }
}

process.on('SIGINT', () => {
  console.log(chalk.yellow('\n\nGoodbye!'));
  if (socket) socket.disconnect();
  process.exit(0);
});

main();
