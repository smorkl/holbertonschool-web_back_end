// full_server/utils.js
import fs from 'fs';
import path from 'path';
import csv from 'csv-parser';

export function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    const result = {};

    fs.createReadStream(filePath) // Crear un flujo de lectura del archivo CSV
      .pipe(csv()) // Usar csv-parser para procesar el CSV
      .on('data', (row) => {
        const { field, firstname } = row; // Extraer 'field' y 'firstname' de cada fila

        // Organizar los datos por 'field'
        if (!result[field]) {
          result[field] = [];
        }
        result[field].push(firstname); // Agregar el 'firstname' al campo correspondiente
      })
      .on('end', () => {
        resolve(result); // Resolver la promesa con el objeto resultante
      })
      .on('error', (err) => {
        reject('Cannot read the file'); // Rechazar en caso de error
      });
  });
}
