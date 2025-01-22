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
    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };
    const