const express = require('express');
const fs = require('fs');

const app = express();

/**
 * Counts the number of students in a CSV file and returns the results as a string.
 *
 * @param {string} path - The path to the CSV file.
 * @returns {Promise<string>} The formatted string with student details.
 */
async function countStudents(path) {
  try {
    const data = await fs.promises.readFile(path, 'utf-8');
    const lines = data.split('\n').filter((line) => line.trim() !== ''); // Remove empty lines

    if (lines.length < 2) {
      throw new Error('No students found');
    }

    const students = lines.map((line) => line.split(','));
    const fields = students[0]; // Extract headers: firstname, lastname, age, field

    if (fields.length < 4) {
      throw new Error('Invalid file format');
    }

    const fieldCounts = {};

    for (let i = 1; i < students.length; i += 1) {
      const student = students[i];
      const field = student[3]; // Access the 'field' column
      const firstname = student[0]; // Access the 'firstname' column

      if (!fieldCounts[field]) {
        fieldCounts[field] = [];
      }

      fieldCounts[field].push(firstname);
    }

    const result = [];
    result.push(`Number of students: ${students.length - 1}`);

    Object.keys(fieldCounts).forEach((field) => {
      result.push(
        `Number of students in ${field}: ${fieldCounts[field].length}. List: ${fieldCounts[field].join(', ')}`,
      );
    });

    return result.join('\n');
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

app.get('/', (req, res) => {
  res.setHeader('Content-Type', 'text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  const database = process.argv[2];
  if (!database) {
    res.setHeader('Content-Type', 'text/plain');
    res.send('This is the list of our students\nCannot load the database');
    return;
  }

  try {
    const studentInfo = await countStudents(database);
    res.setHeader('Content-Type', 'text/plain');
    res.send(`This is the list of our students\n${studentInfo}`);
  } catch (error) {
    res.setHeader('Content-Type', 'text/plain');
    res.send('This is the list of our students\nCannot load the database');
  }
});

app.listen(1245, () => {
  console.log('Server is running on port 1245');
});

module.exports = app;
