import React, { useState, useEffect } from 'react';
import axios from 'axios';
import toast, {Toaster} from 'react-hot-toast'
import '../App.css'
const TurnoForm = () => {
  const initialState = {
    dni: '',
    nombre: '',
    apellido: '',
    email: '',
    numeroTelefono: '',
    especialidad: '',
    servicio: '',
    profesional: '',
    fecha: '',
    hora: '',
  };
  
  const [formData, setFormData] = useState(initialState);
  const [especialidades, setEspecialidades] = useState([]);
  const [servicios, setServicios] = useState([]);
  const [usuarioExistente, setUsuarioExistente] = useState(null);
  const [profesionalesFiltrados, setProfesionalesFiltrados] = useState([]);
  const [mostrarCamposUsuario, setMostrarCamposUsuario] = useState(false);

  useEffect(() => {
    // Cargar opciones para las especialidades desde el backend
    axios.get('http://127.0.0.1:8000/api/Especialidades/')
      .then(response => setEspecialidades(response.data))
      .catch(error => console.error('Error al cargar especialidades', error));
      setMostrarCamposUsuario(false);
  }, []);

  const verificarUsuarioExistente = async (dni) => {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/api/Usuarios/?dni=${dni}`);
      const usuarios = response.data;

      const usuarioEncontrado = usuarios.find(usuario => usuario.dni === dni);

      if (usuarioEncontrado) {
        // Si hay un usuario registrado con el DNI, obtenemos su nombre y apellido
        setUsuarioExistente({
          nombre: usuarioEncontrado.nombre,
          apellido: usuarioEncontrado.apellido,
        });
      } else {
        setUsuarioExistente(null);
      }
    } catch (error) {
      console.error('Error al verificar el usuario existente', error);
      setUsuarioExistente(null);
    }
  };

  const handleChangeDNI = (e) => {
    const dni = e.target.value;
    setUsuarioExistente(null); // Limpiar el usuario existente al cambiar el DNI
    setFormData({ ...formData, dni });
    verificarUsuarioExistente(dni);
  };

  const handleChangeEspecialidad = async (e) => {
    const especialidadId = e.target.value;
    setFormData({ ...formData, especialidad: especialidadId, servicio: '', profesional: '' });
  
    try {
      const serviciosResponse = await axios.get(`http://127.0.0.1:8000/api/Servicios/?especialidad=${especialidadId}`);
      setServicios(serviciosResponse.data);
    } catch (error) {
      console.error('Error al cargar servicios', error);
      setServicios([]);
    }
  };
  
  const handleChangeServicio = (e) => {
    const servicioId = e.target.value;
    setFormData({ ...formData, servicio: servicioId, profesional: '' });
  
    // Obtener todos los profesionales directamente desde el modelo Profesional
    axios.get(`http://127.0.0.1:8000/api/Profesionales/`)
      .then(response => setProfesionalesFiltrados(response.data))
      .catch(error => console.error('Error al cargar profesionales', error));
  };
  
  const submitForm = async () => {
    try {
      // Obtener el DNI del usuario del formulario
      const dniUsuario = formData.dni;
  
      // Verificar la existencia del usuario
      const responseUsuario = await axios.get(`http://127.0.0.1:8000/api/Usuarios/?dni=${dniUsuario}`);
      const usuarios = responseUsuario.data;
      const usuarioEncontrado = usuarios.find(usuario => usuario.dni === dniUsuario);
  
      if (!usuarioEncontrado) {
        // Si el usuario no existe, puedes manejarlo aquí (por ejemplo, mostrar un mensaje o crear el usuario)
        console.log('Usuario no encontrado');
        return;
      }
  
      // Obtener el ID del usuario encontrado
      const idUsuario = usuarioEncontrado.id;
  
      // Incluir el ID del usuario en la solicitud
      const response = await axios.post('http://127.0.0.1:8000/api/Turnos/', {
        ...formData,
        usuario: idUsuario,  // Asignar el ID del usuario al campo usuario
      });
  
      console.log('Turno registrado exitosamente', response.data);
      setFormData(initialState);
      setUsuarioExistente(null);
      toast.success('Turno registrado exitosamente', {
        position: 'top-center', 
        style:{
          background: '#101010',
          color: 'white'
        }
      });
    } catch (error) {
      console.error('Error al registrar el turno', error);
    }
  };
  return (
    <body>
      <Toaster/>
    <form className='form' onSubmit={(e) => { e.preventDefault(); submitForm(); }}>
      <h4 className='titulo'>Turnos</h4>
  
      <label htmlFor="dni">DNI:</label>
      <input
        className='campo'
        type="text"
        id="dni"
        value={formData.dni}
        onChange={(e) => {
          setUsuarioExistente(null); 
          setFormData({ ...formData, dni: e.target.value });
          verificarUsuarioExistente(e.target.value);
        }}
        required
      />
      {usuarioExistente && (
        <p className='cartel-bienvenida'>Bienvenido/a, {usuarioExistente.nombre} {usuarioExistente.apellido}</p>
      )}
      {mostrarCamposUsuario && (
        <>
          <label htmlFor="nombre">Nombre:</label>
          <input
            className='campo'
            type="text"
            id="nombre"
            value={formData.nombre}
            onChange={(e) => setFormData({ ...formData, nombre: e.target.value })}
            required
          />

          <label htmlFor="apellido">Apellido:</label>
          <input
            className='campo'
            type="text"
            id="apellido"
            value={formData.apellido}
            onChange={(e) => setFormData({ ...formData, apellido: e.target.value })}
            required
          />

          <label htmlFor="email">Email:</label>
          <input
            className='campo'
            type="email"
            id="email"
            value={formData.email}
            onChange={(e) => setFormData({ ...formData, email: e.target.value })}
            required
          />

          <label htmlFor="numeroTelefono">Número de Teléfono:</label>
          <input
            className='campo'
            type="text"
            id="numeroTelefono"
            value={formData.numeroTelefono}
            onChange={(e) => setFormData({ ...formData, numeroTelefono: e.target.value })}
            required
          />
        </>
      )}
<label htmlFor="especialidad">Especialidad:</label>
      <select
        className='campo'
        id="especialidad"
        value={formData.especialidad}
        onChange={handleChangeEspecialidad}
        required
      >
        <option value="" disabled>Seleccione especialidad</option>
        {especialidades.map((especialidad) => (
          <option key={especialidad.id_especialidad} value={especialidad.id_especialidad}>
            {especialidad.nombre_especialidad}
          </option>
        ))}
      </select>

    <label htmlFor="servicio">Servicio:</label>
    <select
        className='campo'
        id="servicio"
        value={formData.servicio}
        onChange={handleChangeServicio}
        required
      >
      <option value="" disabled>Seleccione servicio</option>
        {servicios.map((servicio) => (
      <option key={servicio.id_servicio} value={servicio.id_servicio}>
        {servicio.nombre_servicio}
      </option>
      ))}
    </select>

    <label htmlFor="profesional">Profesional:</label>
<select
  className='campo'
  id="profesional"
  value={formData.profesional}
  onChange={(e) => setFormData({ ...formData, profesional: e.target.value })}
  required
>
  <option value="" disabled>Seleccione profesional</option>
  {profesionalesFiltrados.map((profesional) => (
    <option key={profesional.id_profesional} value={profesional.id_profesional}>
      {profesional.nombre}
    </option>
  ))}
</select>

      <label htmlFor="fecha">Fecha:</label>
      <input
        className='campo'
        type="date"
        id="fecha"
        value={formData.fecha}
        onChange={(e) => setFormData({ ...formData, fecha: e.target.value })}
        required
      />

      <label htmlFor="hora">Hora:</label>
      <input
        className='campo'
        type="time"
        id="hora"
        value={formData.hora}
        onChange={(e) => setFormData({ ...formData, hora: e.target.value })}
        required
      />

      <button className='boton' type="submit">Registrar Turno</button>
    </form>
    </body>
  );
};


export default TurnoForm;
