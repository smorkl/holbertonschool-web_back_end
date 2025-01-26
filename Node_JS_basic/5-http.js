const http = require('http');
const fs = require('fs');
const { promisify } = require('util');

// Promisify fs.readFile for easier use
const readFileAsync = promisify(fs.readFile);

/**
 * Counts the number of students in a CSV file asynchronously.
 *
 * @param {string} path - The path to the CSV file.
 * @returns {Promise<string>} - A promise that resolves to a formatted string with student information.
 */
async function countStudents(path) {
  try {
    const data = await readFileAsync(path, 'utf-8');
    const lines = data.split('\n').filter(line => line.trim() !== ''); // Remove empty lines

    const students = lines.map(line => line.split(','));
    const fields = students[0]; // Headers: firstname, lastname, age, field

    if (fields.length < 4) {
      throw new Error('Invalid file format');
    }

    const fieldCounts = {};
    for (let i = 1; i < students.length; i++) {
      const student = students[i];
      if (student.length < 4) continue; // Skip invalid rows
      const field = student[3]; // Access 'field' column
      const firstname = student[0]; // Access 'firstname' column

      if (!fieldCounts[field]) {
        fieldCounts[field] = [];
      }

      fieldCounts[field].push(firstname);
    }

    let output = `Number of students: ${students.length - 1}`;
    for (const field in fieldCounts) {
      output += `\nNumber of students in ${field}: ${fieldCounts[field].length}. List: ${fieldCounts[field].join(', ')}`;
    }
    return output;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

// Create the HTTP server
const app = http.createServer(async (req, res) => {
  if (req.url === '/') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    const databasePath = process.argv[2];
    if (!databasePath) {
      res.statusCode = 500;
      res.setHeader('Content-Type', 'text/plain');
      res.end('Database path not provided');
      return;
    }

    try {
      const studentsInfo = await countStudents(databasePath);
      res.statusCode = 200;
      res.setHeader('Content-Type', 'text/plain');
      res.end(`This is the list of our students\n${studentsInfo}`);
    } catch (error) {
      res.statusCode = 500;
      res.setHeader('Content-Type', 'text/plain');
      res.end(error.message);
    }
  } else {
    res.statusCode = 404;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Not Found');
  }
});

// Set the server to listen on port 1245
app.listen(1245, () => {
  console.log('Server is running on port 1245');
});

// Export the app
module.exports = app;
