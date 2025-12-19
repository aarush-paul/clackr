
# Clackr 💬

A real-time CLI-based chat application built with Node.js, WebSocket, and Socket.IO. Create rooms, join friends, and chat instantly from your terminal.

## Features

✨ **Real-time Messaging** - Instant message delivery using WebSocket  
🔧 **Dynamic Rooms** - Create and join rooms on the fly  
👥 **User Management** - Automatic user tracking and real-time notifications  
🎨 **Beautiful CLI UI** - Colorful terminal interface with Figlet and Chalk  
🌐 **Internet-Based** - Connect from anywhere over the internet (not just local network)  
🗑️ **Auto-Cleanup** - Rooms automatically destroyed when empty  
📱 **Cross-Platform** - Works on macOS, Linux, and Windows  
💾 **Ephemeral Messages** - No data persistence, chats deleted when room closes  
🔒 **Zero Data Collection** - Your conversations stay private  

## Prerequisites

- Node.js 16.0.0 or higher
- npm 7.0.0 or higher

## Installation

Install Clackr globally via npm:

```bash
npm install -g clackr
```

## Quick Start

### Run Clackr
```bash
clackr
```

### Interactive Menu
1. **Enter your username** - Choose any name or use auto-generated
2. **Select a room** - Join existing room or create a new one
3. **Start chatting** - Type messages and press Enter
4. **Use commands** - `/rooms`, `/help`, `/leave`

### Example Session
```bash
$ clackr

  ____ _     _    ____ _  ______
 / ___| |   / \  / ___| |/ /  _ \
| |   | |  / _ \ \___ \   /| |_) |
| |___| | / ___ \ ___) |  \ |  _ <
 \____|_|/_/   \_\____/|_|\_\_| \_\

? Enter your username: Alice
✓ Connected to server

? Select a room or create a new one:
  ❯ General (2 users)
    Off-topic (1 user)
    ➕ Create New Room
```

## Development & Deployment

### Local Testing
```bash
# Terminal 1: Start the server
npm run dev

# Terminal 2: Start the client(s)
npm start
```

### Vercel Deployment
```bash
npm install -g vercel
vercel --prod

# Then set environment variable for client
export CLACKR_SERVER=https://your-deployment.vercel.app
npm start
```

### Docker
```bash
docker build -t clackr .
docker run -p 3000:3000 clackr
```

## In-Chat Commands

| Command | Description |
|---------|-------------|
| `/rooms` | List all available rooms |
| `/help` | Show help and available commands |
| `/leave` | Leave room and exit |
| Just type and press Enter | Send a message |

## Architecture

**Client** (`bin/clackr.js`)
- Interactive CLI with Inquirer.js
- Real-time message display
- WebSocket client via Socket.IO

**Server** (`bin/server.js` or `api/server.js`)
- Express.js HTTP server
- Socket.IO WebSocket server
- Room and user management
- Message broadcasting

## Configuration

### Environment Variables
```bash
CLACKR_SERVER=http://localhost:3000  # Server URL for client
PORT=3000                             # Server port
NODE_ENV=development                  # Environment mode
```

## Project Structure

```
├── bin/
│   ├── clackr.js          # CLI client
│   └── server.js          # Development server
├── api/
│   └── server.js          # Vercel serverless
├── package.json           # Dependencies
├── vercel.json           # Vercel config
├── Dockerfile            # Docker setup
└── README.md             # This file
```

## Security Notes

**Current Implementation:**
- Username-based identification
- In-memory data storage
- No encryption by default

**For Production:**
- Add user authentication (JWT/OAuth)
- Implement rate limiting
- Use HTTPS/WSS only
- Add message validation
- Consider Vercel for automatic HTTPS

## Troubleshooting

### Connection Issues
```bash
# Check if server is running
curl http://localhost:3000/api/health

# Test with custom port
PORT=5000 npm run dev
```

### Port Already in Use
```bash
PORT=4000 npm run dev
```

### Missing Dependencies
```bash
npm install
```

## Performance

- **Supports** ~100+ concurrent users per instance
- **Scalable** - Easy horizontal scaling with Vercel or clustering
- **Fast** - WebSocket provides near-instant messaging
- **Lightweight** - ~7.9 KB package size

## License

MIT License - Use freely for personal or commercial projects

## Repository

**GitHub:** https://github.com/aarush-paul/clackr  
**npm:** https://npmjs.com/package/clackr (coming soon)

---

Built with ❤️ using Node.js, Express, and Socket.IO
![App Screenshot](https://raw.githubusercontent.com/aarush-paul/clackr/main/pics/3.png)


## Deployment

To deploy this project run

```bash
  npm i clackr
  npm run host
  npm run join
```


## Authors

- [@aarush-paul](https://www.github.com/aarush-paul)


## License

[Creative Commons Zero v1.0 Universal](https://github.com/aarush-paul/clackr/blob/main/LICENSE)

