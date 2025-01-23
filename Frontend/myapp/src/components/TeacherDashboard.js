import React, { useState, useEffect } from 'react';
import { useLocation } from 'react-router-dom';

const TeacherDashboard = ({ teacherId }) => {
  const [date, setDate] = useState('');
  const [attendance, setAttendance] = useState([]);
  const [studentDetails, setStudentDetails] = useState({
    name: '',
    id: '',
    status: 'Present',
  });
  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);
  const teacherIdFromUrl = queryParams.get('teacherId');

  useEffect(() => {
    if (!teacherId && !teacherIdFromUrl) {
      alert('Teacher ID is missing. Please log in again.');
      window.location.href = '/teacher-login';
    }
  }, [teacherId, teacherIdFromUrl]);

  const effectiveTeacherId = teacherId || teacherIdFromUrl;

  const handleAddStudent = () => {
    if (studentDetails.name && studentDetails.id) {
      setAttendance([...attendance, studentDetails]);
      setStudentDetails({ name: '', id: '', status: 'Present' });
    }
  };

  const handleSubmit = async () => {
    if (!effectiveTeacherId) {
      alert('Teacher ID (id_number) is missing. Please log in again.');
      return;
    }
    if (!date || attendance.length === 0) {
      alert('Please fill in all fields and add at least one student.');
      return;
    }
    try {
      const response = await fetch('http://localhost:8000/api/save_attendance/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          id_number: effectiveTeacherId, // Send id_number instead of teacher_id
          date,
          attendance_records: attendance,
        }),
      });
      const data = await response.json();
      if (response.ok) {
        alert('Attendance saved successfully!');
        setAttendance([]);
        setDate('');
      } else {
        alert('Failed to save attendance: ' + data.message);
      }
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred while saving attendance.');
    }
  };

  return (
    <div className="min-h-screen p-8 bg-gray-100">
      <h1 className="text-2xl font-bold mb-4">Teacher Dashboard</h1>
      <div className="bg-white p-6 rounded-lg shadow-md">
        <h2 className="text-xl font-semibold mb-4">Record Attendance</h2>
        <label className="block mb-2 font-medium">Date</label>
        <input
          type="date"
          value={date}
          onChange={(e) => setDate(e.target.value)}
          className="border rounded-md p-2 mb-4 w-full"
        />
        <h3 className="text-lg font-semibold mb-2">Add Student</h3>
        <div className="mb-4">
          <input
            type="text"
            placeholder="Student Name"
            value={studentDetails.name}
            onChange={(e) => setStudentDetails({ ...studentDetails, name: e.target.value })}
            className="border rounded-md p-2 mb-2 w-full"
          />
          <input
            type="text"
            placeholder="Student ID"
            value={studentDetails.id}
            onChange={(e) => setStudentDetails({ ...studentDetails, id: e.target.value })}
            className="border rounded-md p-2 mb-2 w-full"
          />
          <select
            value={studentDetails.status}
            onChange={(e) => setStudentDetails({ ...studentDetails, status: e.target.value })}
            className="border rounded-md p-2 mb-2 w-full"
          >
            <option value="Present">Present</option>
            <option value="Absent">Absent</option>
            <option value="Late">Late</option>
          </select>
          <button
            onClick={handleAddStudent}
            className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 transition"
          >
            Add Student
          </button>
        </div>
        <h3 className="text-lg font-semibold mb-2">Attendance List</h3>
        <ul className="mb-4">
          {attendance.map((student, index) => (
            <li key={index} className="border p-2 rounded mb-2">
              {student.name} (ID: {student.id}) - {student.status}
            </li>
          ))}
        </ul>
        <button
          onClick={handleSubmit}
          className="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600 transition"
        >
          Save Attendance
        </button>
      </div>
    </div>
  );
};

export default TeacherDashboard;
