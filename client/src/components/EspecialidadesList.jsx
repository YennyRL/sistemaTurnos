import {useEffect, useState} from 'react'
import { getEspecialidades } from '../api/especialidad.api'

export function EspecialidadesList() {
  
   const [especialidades, setEspecialidades] = useState([])

   useEffect(() => {
      const fetchEspecialidades = async () => {
        try {
          const response = await getEspecialidades();  // Asume que getEspecialidades devuelve un array de especialidades
          setEspecialidades(response.data);
        } catch (error) {
          console.error('Error:', error);
        }
      };
  
      fetchEspecialidades();
    }, []);

   return (
      <div>
         {especialidades.map(especialidad =>(
            <div key={especialidad.id}>
               <h1>{especialidad.nombre_especialidad}</h1>
            </div>
         ))}
      </div>
  )
}
