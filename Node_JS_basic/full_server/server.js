// full_server/server.js
import express from 'express';
import routes from './routes';

const app = express();
const port = 1245;

// Usar las rutas definidas
app.use('/', routes);

// Iniciar el servidor
app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});

export default app;
