import React, {useEffect, useState} from 'react';
import {Container, Form, Button, Alert} from 'react-bootstrap';
import axios from 'axios';
import {baseUrl} from "../config";

const Registration = () => {
    const [departments, setDepartments] = useState([]);
    const [candidate, setCandidate] = useState({
        first_name: '',
        last_name: '',
        date_of_birth: '',
        department: '',
        start_working_date: '',
        resume: null,
    });

    useEffect(() => {
        const fetchDepartments = async () => {
            try {
                const response = await axios.get(`${baseUrl}/departments/`);
                setDepartments(response.data);
            } catch (error) {
                console.error('Error fetching departments:', error);
            }
        };
        fetchDepartments();
    }, []);

    const [success, setSuccess] = useState(false);
    const [error, setError] = useState(false);

    const handleChange = (e) => {
        const {name, value} = e.target;
        setCandidate((prevCandidate) => ({
            ...prevCandidate,
            [name]: value,
        }));
    };

    const handleFileChange = (e) => {
        setCandidate((prevCandidate) => ({
            ...prevCandidate,
            resume: e.target.files[0],
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        const formData = new FormData();
        Object.entries(candidate).forEach(([key, value]) => {
            formData.append(key, value);
        });

        try {
            await axios.post(`${baseUrl}/candidate/`, formData);
            setSuccess(true);
            setError(false);
        } catch (error) {
            setError(true);
            setSuccess(false);
        }
    };

    return (
        <Container>
            <h2>Candidate Registration</h2>
            {success && <Alert variant="success">Registration successful!</Alert>}
            {error && <Alert variant="danger">Registration failed. Please try again.</Alert>}
            <Form onSubmit={handleSubmit}>
                <Form.Group controlId="first_name">
                    <Form.Label>First Name</Form.Label>
                    <Form.Control
                        type="text"
                        name="first_name"
                        value={candidate.first_name}
                        onChange={handleChange}
                        required
                    />
                </Form.Group>
                <Form.Group controlId="last_name">
                    <Form.Label>Last Name</Form.Label>
                    <Form.Control
                        type="text"
                        name="last_name"
                        value={candidate.last_name}
                        onChange={handleChange}
                        required
                    />
                </Form.Group>
                <Form.Group controlId="date_of_birth">
                    <Form.Label>Date of Birth</Form.Label>
                    <Form.Control
                        type="date"
                        name="date_of_birth"
                        value={candidate.date_of_birth}
                        onChange={handleChange}
                        required
                    />
                </Form.Group>
                <Form.Group controlId="department">
                    <Form.Label>Department</Form.Label>
                    <Form.Control as="select" name="department" value={candidate.department} onChange={handleChange}
                                  required>
                        <option value="">Select a department</option>
                        {departments.map((dept) => (
                            <option key={dept.code} value={dept.code}>
                                {dept.name}
                            </option>
                        ))}
                    </Form.Control>
                </Form.Group>
                <Form.Group controlId="start_working_date">
                    <Form.Label>Start Working Date</Form.Label>
                    <Form.Control
                        type="date"
                        name="start_working_date"
                        value={candidate.start_working_date}
                        onChange={handleChange}
                        required
                    />
                </Form.Group>
                <Form.Group>
                    <Form.Label>Resume</Form.Label>
                    <Form.Control type="file" name="resume" onChange={handleFileChange} required/>
                </Form.Group>
                <Button type="submit" variant="primary">
                    Register
                </Button>
            </Form>
        </Container>
    );
};

export default Registration;