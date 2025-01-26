const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

console.log('Welcome to Holberton School, what is your name?');

rl.on('line', (input) => {
  process.stdout.write(`Your name is: ${input.trim()}\r\n`);
  rl.close();
});

rl.on('close', () => {
  process.stdout.write('This important software is now closing\r\n');
});
