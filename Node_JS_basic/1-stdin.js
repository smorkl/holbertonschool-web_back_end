console.log('Welcome to Holberton School, what is your name?');

// Leer entrada estándar
process.stdin.resume();
process.stdin.setEncoding('utf8');

process.stdin.on('data', (chunk) => {
  const name = chunk.trim(); // Remover saltos de línea y espacios adicionales
  console.log(`Your name is: ${name}`);
  console.log('This important software is now closing');
  process.exit(0); // Salida exitosa
});
