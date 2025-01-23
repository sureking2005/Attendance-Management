import React, { useState } from 'react';
const TeacherReg = () => {
    const [formData, setFormData] = useState({
        Name: '',
        id_number: '',
        password: ''
    });
    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await fetch('http://localhost:8000/api/teacher/register/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
            });
            
            const data = await response.json();
            if (response.ok) {
                console.log('Registration successful:', data);
            } else {
                console.error('Registration failed:', data);
            }
        } catch (error) {
            console.error('Error:', error);
        }
    };
    return (
        <form onSubmit={handleSubmit}>
          <input name="name" placeholder="Name" onChange={handleChange} required />
          <input name="id_number" placeholder="ID Number" onChange={handleChange} required />
          <input name="password" placeholder="Password" type="password" onChange={handleChange} required />
          <button type="submit">Register</button>
        </form>
      );
    };

export default TeacherReg;