import Container from "react-bootstrap/Container"
import Nav from "react-bootstrap/Nav"
import NavDropdown from "react-bootstrap/NavDropdown"
import Navbar from "react-bootstrap/Navbar"

function TopNavbar(): React.ReactElement {
  return (
    <Navbar bg="dark" expand="lg" variant="dark">
      <Container>
        <Navbar.Brand href="/">
          <img
            alt=""
            src="/logo.svg"
            width="30"
            height="30"
            className="d-inline-block align-top"
          />{" "}
          DHost
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="/dapps/">Dapps</Nav.Link>
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
      </Container>
    </Navbar>
  )
}

export default TopNavbar
