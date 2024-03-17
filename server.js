#!/usr/bin/env node

/*
Clakr | Made by Aarush Paul
Github: https://github.com/aarush-paul
*/
console.clear();
const CLI = require('clui');
const Spinner = CLI.Spinner;
var countdown = new Spinner('Importing modules  ', ['◜','◠','◝','◞','◡','◟']);
var countdown2 = new Spinner('Starting Up  ', ['◜','◠','◝','◞','◡','◟']);
var countdown3 = new Spinner('', [' ',' ',' ',' ',' ',' ']);
countdown.start();
const io = require("socket.io")();
const chalk = require("chalk");
const prompt = require("prompt-sync")({ sigint: true });
const localtunnel = require('localtunnel');
console.log(chalk.bold.blue("         ,,                                    "));
console.log(chalk.bold.blue("       `7MM                 `7MM               "));
console.log(chalk.bold.blue("         MM                   MM               "));
console.log(chalk.bold.blue(` ,p6"bo  MM   ,6"Yb.  ,p6"bo  MM  ,MP' 7Mb,od8 `));
console.log(chalk.bold.blue(`6M'  OO  MM  8)   MM 6M'  OO  MM ;Y     MM' "' `));
console.log(chalk.bold.blue("8M       MM   ,pm9MM 8M       MM;Mm     MM     "));
console.log(chalk.bold.blue("YM.    , MM  8M   MM YM.    , MM `Mb.   MM     "));
console.log(chalk.bold.blue(" YMbmd'.JMML.`Moo9^Yo.YMbmd'.JMML. YA..JMML.   "));
console.log(chalk.bold.blue(" ██████╗███████╗██████╗ ██╗   ██╗███████╗██████╗   "));
console.log(chalk.bold.blue("██╔════╝██╔════╝██╔══██╗██║░░░██║██╔════╝██╔══██╗  "));
console.log(chalk.bold.blue("╚█████╗░█████╗░░██████╔╝╚██╗░██╔╝█████╗░░██████╔╝  "));
console.log(chalk.bold.blue("░╚═══██╗██╔══╝░░██╔══██╗░╚████╔╝░██╔══╝░░██╔══██╗  "));
console.log(chalk.bold.blue("██████╔╝███████╗██║░░██║░░╚██╔╝░░███████╗██║░░██║  "));
console.log(chalk.bold.blue("╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  "));
console.log(" ");
console.log(chalk.bold.blue("Made By Aarush Paul"));
console.log(" ");
console.log(chalk.yellow("https://github.com/aarush-paul/clackr"));
console.log(" ");
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
sleep(5000)
  .then(() => countdown.stop())
  .then(() => countdown2.start())
  .then(() => sleep(2000))
  .then(() => countdown2.stop())

sleep(8000).then(() => {
const port = prompt("Enter the port you want to use (must be between 1025 and 65535): ");
if (port < 1025 || port > 65535) {
    console.log(chalk.bold.red("[!] Invalid Port!"));
    process.exit();
}
const users = {};                                                                                                                  
io.listen(port);

(async () => {
  const tunnel = await localtunnel({ port: port});
  console.log(chalk.bold.green("[i] Your chat url is:  " + chalk.bold.red(tunnel.url) + ". Run `clacker join` on another terminal window and enter this url to join. Send this url to your friends and ask them to paste this link in the console after running `clackr join`. "));
})();

console.log(" ");
console.log(chalk.bold.bgGreen("=====CHATROOM LOGS(Press CTRL+Q to destroy room)====="));

    io.on("connection", (socket) => {
	    console.log(chalk.bold.cyan("[!] New Connection: ") + chalk.dim.underline(socket.id));
        socket.on('new user', (name) => {
            users[socket.id] = chalk.bold.yellow(name);
            socket.broadcast.emit("message", ` `);
            socket.broadcast.emit("message", chalk.bgYellow(`${name} joined the chat.`));
            socket.broadcast.emit("message", ` `);
        });

        socket.on('message', (text) => {
            socket.broadcast.emit("message", `${users[socket.id]} > ${text}`);
        });
    });
    var stdin = process.stdin;
    stdin.setRawMode( true );
    stdin.resume();
    stdin.setEncoding( 'utf8' );
    stdin.on( 'data', function( key ){
      // ctrl-c ( end of text )
      if ( key === '\u0011' ) {
        (async function() {await ngrok.disconnect(url);}());
        process.exit();
      }
      process.stdout.write( key );
    });
  });
