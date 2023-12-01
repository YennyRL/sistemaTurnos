import {BrowserRouter, Routes, Route, Navigate} from 'react-router-dom'
import { TurnoForm } from './pages/TurnoForm'
import { EspecialidadesPage } from './pages/especialidadesPage'
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Navigate to="/turno"/>}/>
        <Route path="/turno" element={<TurnoForm/>}/>
        <Route path='/especialidades' element={<EspecialidadesPage/>}/>
      </Routes>
    </BrowserRouter>
  )
}

export default App