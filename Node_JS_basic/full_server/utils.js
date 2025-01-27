// full_server/utils.js
import fs from 'fs';


export function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf-8', (err, data) => {
      if (err) {
        reject('Cannot read the file');
        return;
      }

      try {
        const lines = data.trim().split('\n'); // Dividir por líneas
        const headers = lines[0].split(','); // Encabezados (primera línea)
        const result = {};

        lines.slice(1).forEach(line => {
          const values = line.split(','); // Dividir cada línea en columnas
          const row = headers.reduce((acc, header, index) => {
            acc[header] = values[index];
            return acc;
          }, {});

          // Agrupar por 'field'
          const { field, firstname } = row;
          if (!result[field]) {
            result[field] = [];
          }
          result[field].push(firstname);
        });

        resolve(result); // Resolver la promesa con los datos procesados
      } catch (error) {
        reject('Error processing the file');
      }
    });
  });
}
