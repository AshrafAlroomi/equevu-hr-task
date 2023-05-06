import React, {useEffect, useState} from 'react';
import {Table, Container, Button} from 'react-bootstrap';
import axios from 'axios';
import {baseUrl} from "../config";

const CandidateList = () => {
    const [candidates, setCandidates] = useState([]);

    useEffect(() => {
        fetchCandidates().then(r => console.log("Fetched"));
    }, []);

    const handleDownloadResume = async (candidate) => {
        try {
            const response = await axios.get(`${baseUrl}/candidates/${candidate.id}/resume/`, {
                responseType: 'blob',
                headers: {
                    'X-ADMIN': '1',
                },
            });
            const url = window.URL.createObjectURL(new Blob([response.data]));
            const link = document.createElement('a');

            const splitFile = candidate.resume.split('.')
            const fileExtension = splitFile[splitFile.length - 1];
            const fileName = `resume_${candidate.id}.${fileExtension}`

            link.href = url;
            link.setAttribute('download', fileName);
            document.body.appendChild(link);
            link.click();
            link.parentNode.removeChild(link);
        } catch (error) {
            console.error('Error downloading resume:', error);
        }
    };
    const fetchCandidates = async () => {
        try {
            const response = await axios.get(`${baseUrl}/candidates/`, {
                headers: {
                    'X-ADMIN': '1',
                },
            });
            setCandidates(response.data);
        } catch (error) {
            console.error('Error fetching candidates:', error);
        }
    };

    return (
        <Container>
            <h2 className="my-4">Candidate List</h2>
            <Table striped bordered hover>
                <thead>
                <tr>
                    <th>ID</th>
                    <th>First Name</th>
                    <th>Last Name</th>
                    <th>Date of Birth</th>
                    <th>Department</th>
                    <th>Years of Experience</th>
                    <th>Resume</th>
                </tr>
                </thead>
                <tbody>
                {candidates.map((candidate) => (
                    <tr key={candidate.id}>
                        <td>{candidate.id}</td>
                        <td>{candidate.first_name}</td>
                        <td>{candidate.last_name}</td>
                        <td>{candidate.date_of_birth}</td>
                        <td>{candidate.department}</td>
                        <td>{candidate.years_of_experience}</td>
                        <td>
                            <Button
                                variant="primary"
                                onClick={() => handleDownloadResume(candidate)}>
                                Download Resume
                            </Button>
                        </td>
                    </tr>
                ))}
                </tbody>
            </Table>
        </Container>
    );
};

export default CandidateList;
