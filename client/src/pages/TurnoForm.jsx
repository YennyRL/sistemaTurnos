import React, {useState, useEffect} from 'react';
import {useForm} from 'react-hook-form'
import { EspecialidadesList } from '../components/especialidadesList';

export function TurnoForm() {

  const TurnoForm = () => {
    const [selectedEspecialidad, setSelectedEspecialidad] = useState('');
  }
    useEffect(() => {
      // Ahora puedes acceder a la lista de especialidades directamente
      console.log(EspecialidadesList.especialidades);
    }, []);

  return (
    <form action="">
      <input placeholder="Ingrese su DNI"
        {...register("dni", {required : true})}
      />
      <select
        id="especialidad"
        name="especialidad"
        value={selectedEspecialidad}
        onChange={(e) => setSelectedEspecialidad(e.target.value)}>
        <option value="" disabled>Selecciona una especialidad</option>
        {EspecialidadesList.especialidades.map((opcion) => (
          <option key={opcion.id} value={opcion.id}>
            {opcion.nombre_especialidad}
          </option>
        ))}
      </select>
      <button>Agendar</button>
    </form>
  )
}
