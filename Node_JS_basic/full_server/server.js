// full_server/server.js
import express from 'express';
import routes from './routes';

 // se crea una nueva aplicacion, (objeto)
const app = express();
// declaramos el puerto en el que queremos corer el servidor
const port = 1245;

// Usar las rutas definidas
app.use('/', routes);

// Iniciar elservidor, usamos callbak para mostrar en la terminal que 
// el servidor esta funcionando y muestra la url
app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});

export default app;
