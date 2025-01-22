import React from 'react';
import { useNavigate } from 'react-router-dom';

const HomePage = () => {
  const navigate = useNavigate();

  const handleNavigation = (role) => {
    navigate(`/${role}-login`);
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100">
      <div className="bg-white p-8 rounded-lg shadow-md">
        <h1 className="text-2xl font-bold mb-6 text-center">Welcome to School Portal</h1>
        <div className="space-y-4">
          <button
            onClick={() => handleNavigation('teacher')}
            className="w-full bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 transition-colors"
          >
            Teacher
          </button>
          <button
            onClick={() => handleNavigation('student')}
            className="w-full bg-green-500 text-white py-2 px-4 rounded hover:bg-green-600 transition-colors"
          >
            Student
          </button>
          <button
            onClick={() => handleNavigation('parent')}
            className="w-full bg-purple-500 text-white py-2 px-4 rounded hover:bg-purple-600 transition-colors"
          >
            Parent
          </button>
        </div>
      </div>
    </div>
  );
};

export default HomePage;