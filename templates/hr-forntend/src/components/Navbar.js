import React from 'react';
import { Navbar, Nav } from 'react-bootstrap';
import { LinkContainer } from 'react-router-bootstrap';
import Registration from "./Registration";

const Navigation = () => {
  return (
    <Navbar  expand="lg">
      <LinkContainer to="/">
        <Navbar.Brand>HR System</Navbar.Brand>
      </LinkContainer>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav variant="tabs">
          <LinkContainer to="/">
            <Nav.Link>Register</Nav.Link>
          </LinkContainer>
          <LinkContainer to="/list">
            <Nav.Link>Candidates</Nav.Link>
          </LinkContainer>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  );
};

export default Navigation;