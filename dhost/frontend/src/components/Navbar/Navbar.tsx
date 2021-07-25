import { faSearch } from "@fortawesome/free-solid-svg-icons"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import Button from "react-bootstrap/Button"
import Form from "react-bootstrap/Form"
import FormControl from "react-bootstrap/FormControl"
import Nav from "react-bootstrap/Nav"
import NavDropdown from "react-bootstrap/NavDropdown"
import Navbar from "react-bootstrap/Navbar"

import logo from "../../assets/logo.svg"
import "./style.scss"

function TopNavbar(): React.ReactElement {
  return (
    <Navbar bg="dark" expand="lg" variant="dark" className="px-4">
      <Navbar.Brand href="/">
        <img
          alt=""
          src={logo}
          width="30"
          height="30"
          className="d-inline-block align-top"
        />{" "}
        <span className="text-primary">D</span>Host
      </Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="me-auto">
          <Nav.Link href="/dapps/">Dapps</Nav.Link>
        </Nav>
        <Nav className="me-auto">
          <Form className="d-flex">
            <FormControl
              type="search"
              placeholder="Search for dapps"
              aria-label="Search search for dapps"
              id="navbar-search"
            />
            <Button id="navbar-search-button" variant="outline-dark">
              <FontAwesomeIcon icon={faSearch} />
            </Button>
          </Form>
        </Nav>
        <Nav>
          <NavDropdown title="Account" id="basic-nav-dropdown">
            <NavDropdown.Item href="">Settings</NavDropdown.Item>
            <NavDropdown.Item href="">Security</NavDropdown.Item>
            <NavDropdown.Divider />
            <NavDropdown.Item href="">Logout</NavDropdown.Item>
          </NavDropdown>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  )
}

export default TopNavbar
