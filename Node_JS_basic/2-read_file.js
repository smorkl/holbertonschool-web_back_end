const fs = require('fs');

/**
 * Counts the number of students in a CSV file and displays the results.
 *
 * @param {string} path - The path to the CSV file.
 * @throws {Error} If the file cannot be loaded.
 */
function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf-8');
    const lines = data.split('\n').filter((line) => line.trim() !== ''); // Remove empty lines

    const students = lines.map((line) => line.split(','));
    const fields = students[0]; // Extract headers: firstname, lastname, age, field

    if (fields.length < 4) {
      throw new Error('Invalid file format');
    }

    const fieldCounts = {};

    for (let i = 1; i < students.length; i++) {
      const student = students[i];
      const field = student[3]; // Access the 'field' column
      const firstname = student[0]; // Access the 'firstname' column

      if (!fieldCounts[field]) {
        fieldCounts[field] = [];
      }

      fieldCounts[field].push(firstname);
    }

    console.log(`Number of students: ${students.length - 1}`); // Total students

    Object.keys(fieldCounts).forEach((field) => {
      console.log(
        `Number of students in ${field}: ${fieldCounts[field].length}. List: ${fieldCounts[field].join(', ')}`,
      );
    });
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
