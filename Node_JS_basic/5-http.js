const http = require('http');
const fs = require('fs');
const path = require('path');

const countStudents = (filePath) => {
  if (!fs.existsSync(filePath)) {
    throw new Error('Cannot load the database');
  }

  const data = fs.readFileSync(filePath, 'utf-8');
  const lines = data.split('\n').filter((line) => line.trim() !== '');
  const students = lines.slice(1).map((line) => line.split(','));

  const fieldCounts = {};

  students.forEach(([firstname, lastname, age, field]) => {
    if (!fieldCounts[field]) {
      fieldCounts[field] = [];
    }
    fieldCounts[field].push(firstname);
  });

  const result = [];
  result.push(`Number of students: ${students.length}`);
  for (const [field, names] of Object.entries(fieldCounts)) {
    result.push(
      `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`
    );
  }

  return result.join('\n');
};

const app = http.createServer((req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    try {
      const filePath = path.resolve(__dirname, process.argv[2] || '');
      const studentInfo = countStudents(filePath);
      res.end(`This is the list of our students\n${studentInfo}`);
    } catch (error) {
      res.writeHead(500, { 'Content-Type': 'text/plain' });
      res.end('Cannot load the database');
    }
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Not Found');
  }
});

app.listen(1245, () => {
  console.log('Server is running on port 1245');
});

module.exports = app;
