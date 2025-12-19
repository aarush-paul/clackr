# Clackr - CLI Chat Application

A modern, real-time CLI-based chat application built with Node.js and Socket.IO. Create chat rooms, join existing ones, and communicate instantly from your terminal.

## Features

- 🚀 **Real-time Messaging** - Instant message delivery using WebSocket
- 📦 **Dynamic Rooms** - Create and join chat rooms on the fly
- 👥 **User Management** - Automatic user tracking and room population
- 💬 **Colorful UI** - Beautiful terminal UI with Chalk and Figlet
- 🌐 **Internet Access** - Users can join from anywhere over the internet
- 🗑️ **Auto-cleanup** - Rooms automatically destroyed when empty
- 📱 **Cross-platform** - Works on macOS, Linux, and Windows

## Installation

### Prerequisites
- Node.js 16.0.0 or higher
- npm 7.0.0 or higher

### Quick Start

```bash
# Clone or navigate to the clackr folder
cd clackr

# Install dependencies
npm install

# Run the CLI
npm start
```

Or install globally:

```bash
npm install -g .
clackr
```

## Usage

### Running Clackr

```bash
npm start
# or
clackr
```

### Interactive Menu

1. **Enter Username** - Choose your display name (or auto-generated)
2. **Select Room** - Choose from existing rooms or create a new one
3. **Chat** - Type messages and press Enter
4. **Commands**:
   - `/rooms` - List all available rooms
   - `/help` - Show help and available commands
   - `/leave` - Leave the room and exit

### Example Session

```
  ____ _     _    ____ _  ______
 / ___| |   / \  / ___| |/ /  _ \
| |   | |  / _ \ \___ \   /| |_) |
| |___| | / ___ \ ___) |  \ |  _ <
 \____|_|/_/   \_\____/|_|\_\_| \_\

══════════════════════════════════════════════
  A Real-time CLI Chat Application
══════════════════════════════════════════════

? Enter your username: Alice
Welcome, Alice!

Connecting to server...
✓ Connected to server

? Select a room or create a new one: (Use arrow keys)
❯ General (2 users)
  Off-topic (1 user)
  ➕ Create New Room

You: Hello everyone!
```

## Architecture

### Client (`bin/clackr.js`)
- Socket.IO client for WebSocket communication
- Interactive CLI interface using Inquirer.js
- Real-time message display
- Command-line argument processing

### Server (`bin/server.js`)
- Express.js HTTP server
- Socket.IO WebSocket server
- Room management and user tracking
- Message broadcasting

### Data Storage
- **In-memory** - All data is stored in memory and lost on server restart
- **Auto-cleanup** - Rooms are destroyed when the last user leaves
- **Ephemeral Messages** - Chat messages are not persisted

## Deployment

### Vercel Deployment

1. **Create a Vercel Account** - Sign up at [vercel.com](https://vercel.com)

2. **Connect Your Repository** - Push the project to GitHub

3. **Create Vercel Project**:
   ```bash
   npm install -g vercel
   vercel
   ```

4. **Configuration** - Vercel automatically detects Node.js projects

5. **Deploy**:
   ```bash
   vercel --prod
   ```

6. **Update Client URL** - Set environment variable for production server:
   ```bash
   export CLACKR_SERVER=https://your-project.vercel.app
   clackr
   ```

### Docker Deployment

```dockerfile
FROM node:18-alpine

WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

COPY . .

EXPOSE 3000
CMD ["npm", "run", "vercel"]
```

### Local Development Server

```bash
npm run dev
```

The server runs on `http://localhost:3000` by default.

## Environment Variables

- `CLACKR_SERVER` - Server URL for the CLI client (default: `https://clackr-server.vercel.app`)
- `PORT` - Server port (default: `3000`)

Example:
```bash
export CLACKR_SERVER=http://localhost:3000
npm start
```

## Project Structure

```
clackr/
├── bin/
│   ├── clackr.js          # CLI client entry point
│   └── server.js          # Development server
├── api/
│   └── server.js          # Serverless function for Vercel
├── package.json
├── vercel.json
├── .gitignore
└── README.md
```

## Dependencies

- **socket.io** - Real-time bidirectional communication
- **socket.io-client** - Client library for Socket.IO
- **chalk** - Terminal colors and styling
- **inquirer** - Interactive command line prompts
- **figlet** - ASCII art text
- **ora** - Elegant terminal spinner
- **express** - Web framework (server only)
- **cors** - CORS middleware (server only)

## Technical Details

### WebSocket Communication

The application uses Socket.IO for real-time, bidirectional communication between clients and server.

**Events**:
- `get_rooms` - Fetch list of available rooms
- `join_room` - Join or create a room
- `send_message` - Send a message to the room
- `leave_room` - Leave the current room
- `user_joined` - Broadcast when user joins
- `user_left` - Broadcast when user leaves
- `new_message` - New message from other users
- `disconnect` - Handle disconnection

### Room Management

Rooms are created dynamically and stored in memory. Each room tracks:
- Room ID (unique)
- Room name
- Active users
- Creation timestamp

Rooms are automatically destroyed when the last user leaves.

### Message Format

Messages include:
- Username
- Message text
- Timestamp
- Sender identification

## Performance Considerations

- **In-memory storage** - Scales well for concurrent sessions
- **WebSocket + Polling** - Fallback for older browsers/networks
- **Connection pooling** - Efficient socket management
- **Message broadcasting** - Room-based message delivery

## Limitations & Notes

1. **Data Persistence** - All messages and rooms are lost on server restart
2. **Scalability** - Single-instance deployment; use clustering for multiple instances
3. **Authentication** - Currently uses username-based identification
4. **Rate Limiting** - No built-in rate limiting (add middleware for production)

## Security Recommendations

For production deployment:
1. Add rate limiting middleware
2. Implement user authentication
3. Add message validation and sanitization
4. Enable HTTPS/WSS only
5. Add IP whitelisting if needed
6. Implement connection timeout handling

## Troubleshooting

### Connection Issues
```bash
# Check server is running
curl http://localhost:3000/api/health

# Enable debug mode
DEBUG=socket.io:* clackr
```

### Port Already in Use
```bash
# Use different port
PORT=4000 npm run dev
```

### Rooms Not Showing
```bash
# Verify server connection
export CLACKR_SERVER=http://localhost:3000
npm start
```

## Contributing

Feel free to fork and submit pull requests!

## License

MIT License - See LICENSE file for details

## Support

For issues and questions, please open an issue on the repository.

---

Built with ❤️ using Node.js and Socket.IO
