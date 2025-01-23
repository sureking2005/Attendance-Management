import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './components/HomePage';
import TeacherLoginForm from './components/TeacherLoginForm';
import StudentLogin from './components/StudentLogin';
import ParentLogin from './components/ParentLogin';
import StudentReg from './components/StudentReg';
import TeacherReg from './components/TeacherReg';
import TeacherDashboard from './components/TeacherDashboard';
function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/teacher-login" element={<TeacherLoginForm />} />
        <Route path="/student-login" element={<StudentLogin />} />
        <Route path="/parent-login" element={<ParentLogin/>} />
        <Route path="/student-register" element={<StudentReg />} />
        <Route path="/teacher-register" element={<TeacherReg />} />
        <Route path="/attendance" element={<TeacherDashboard />}/>
      </Routes>
    </Router>
  );
}

export default App;
