// full_server/controllers/StudentsController.js
import { readDatabase } from '../utils';
import path from 'path';

class StudentsController {
  // Obtener todos los estudiantes
  static async getAllStudents(req, res) {
    const filePath = path.join(__dirname, 'database.csv'); // Ruta del archivo CSV

    try {
      const data = await readDatabase(filePath); // Leer y procesar el archivo CSV
      let response = 'This is the list of our students\n';

      // Recorrer los campos (fields) ordenados alfabéticamente
      Object.keys(data).sort((a, b) => a.localeCompare(b, 'en', { sensitivity: 'base' })).forEach((field) => {
        response += `Number of students in ${field}: ${data[field].length}. List: ${data[field].join(', ')}\n`;
      });

      res.status(200).send(response); // Enviar la respuesta con la lista de estudiantes
    } catch (err) {
      res.status(500).send('Cannot load the database'); // En caso de error
    }
  }

  // Obtener estudiantes por major
  static async getAllStudentsByMajor(req, res) {
    const { major } = req.params; // Obtener el major desde los parámetros de la ruta
    const filePath = path.join(__dirname, '../../database.csv'); // Ruta del archivo CSV

    try {
      if (!['CS', 'SWE'].includes(major)) {
        return res.status(500).send('Major parameter must be CS or SWE'); // Validar el parámetro
      }

      const data = await readDatabase(filePath); // Leer y procesar el archivo CSV

      // Verificar si el major existe en los datos
      if (data[major]) {
        res.status(200).send(`List: ${data[major].join(', ')}`); // Enviar la lista de estudiantes en ese major
      } else {
        res.status(404).send('Major not found');
      }
    } catch (err) {
      res.status(500).send('Cannot load the database'); // En caso de error
    }
  }
}

export default StudentsController;
