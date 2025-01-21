import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css';
import StudentPage from './pages/StudentPage';

function App() {

  return (
    <Router>
      <div className="App">
        {/* Define Routes */}
        <Routes>
          <Route path="/" element={<StudentPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

