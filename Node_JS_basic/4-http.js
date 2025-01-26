const http = require('http');

// Create the HTTP server
const app = http.createServer((req, res) => {
  res.statusCode = 200; // HTTP status code 200: OK
  res.setHeader('Content-Type', 'text/plain'); // Response type: plain text
  res.end('Hello Holberton School!'); // Response body
});

// Set the server to listen on port 1245
app.listen(1245, () => {
  console.log('Server is running on port 1245');
});

// Export the app for external use
module.exports = app;
