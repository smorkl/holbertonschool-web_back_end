// full_server/routes/index.js
import express from 'express';
import AppController from '../controllers/AppController';
import StudentsController from '../controllers/StudentsController';

const router = express.Router();

// Ruta para la página principal
router.get('/', AppController.getHomepage);

// Ruta para obtener todos los estudiantes
router.get('/students', StudentsController.getAllStudents);

// Ruta para obtener estudiantes por major
router.get('/students/:major', StudentsController.getAllStudentsByMajor);

export default router;
