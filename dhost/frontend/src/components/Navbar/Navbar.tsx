import { faSearch } from "@fortawesome/free-solid-svg-icons"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import Button from "react-bootstrap/Button"
import FormControl from "react-bootstrap/FormControl"
import InputGroup from "react-bootstrap/InputGroup"
import Nav from "react-bootstrap/Nav"
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
          <InputGroup>
            <FormControl
              type="search"
              placeholder="Search for dapps"
              aria-label="Search search for dapps"
              id="navbar-search"
            />
            <Button id="navbar-search-button" variant="outline-dark">
              <FontAwesomeIcon icon={faSearch} />
            </Button>
          </InputGroup>
        </Nav>
        <Nav>
          <Navbar.Text>
            <img
              alt=""
              src="https://www.gravatar.com/avatar/"
              width="30"
              height="30"
              className="d-inline-block align-top rounded-circle"
            />
          </Navbar.Text>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  )
}

export default TopNavbar
