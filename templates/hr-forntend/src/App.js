import React from 'react';
import {BrowserRouter, Routes, Route} from "react-router-dom";
import Navbar from './components/Navbar';
import Registration from './components/Registration';
import CandidateList from "./components/CandidateList";
import 'bootstrap/dist/css/bootstrap.min.css';


const App = () => {
    return (

        <BrowserRouter>
            <Navbar/>
            <Routes>
                <Route path="/" element={<Registration/>}/>
                <Route path="/list" element={<CandidateList/>}/>
            </Routes>
        </BrowserRouter>
    );
};

export default App;
