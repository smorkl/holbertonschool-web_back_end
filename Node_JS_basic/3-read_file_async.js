const fs = require('fs');

/**
 * Counts the number of students in a CSV file asynchronously.
 *
 * @param {string} path - The path to the CSV file.
 * @returns {Promise} - Resolves when the counting is done or rejects if the file cannot be read.
 */
function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter(line => line.trim() !== ''); // Remove empty lines
      const students = lines.map(line => line.split(','));
      const fields = students[0]; // Headers: firstname, lastname, age, field

      if (fields.length < 4) {
        reject(new Error('Invalid file format'));
        return;
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

      console.log(`Number of students: ${students.length - 1}`); // Total students
      for (const field in fieldCounts) {
        console.log(
          `Number of students in ${field}: ${fieldCounts[field].length}. List: ${fieldCounts[field].join(', ')}`
        );
      }

      resolve();
    });
  });
}

module.exports = countStudents;