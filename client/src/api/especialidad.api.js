import axios from 'axios'

export const getEspecialidades = () => {
   return axios.get('http://127.0.0.1:8000/api/Especialidades/')
}