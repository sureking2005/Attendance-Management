import React from 'react';
import { BrowserRouter as Router, Route, Routes, BrowserRouter } from 'react-router-dom';
import HomePage from './pages/HomePage'
import Login from './pages/Login'

function App() {

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage/>}/>
        <Route path="/teacher-login" element={<Login role="teacher" />}/>
        <Route path="/student-login" element={<Login role="student" />}/>
        <Route path="/parent-login" element={<Login role="parent" />}/>

      </Routes>
    </BrowserRouter>

  );
}

export default App;

