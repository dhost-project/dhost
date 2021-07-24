import Container from "react-bootstrap/Container"
import Button from "react-bootstrap/Button"
import Nav from "react-bootstrap/Nav"

import "./style.scss"

function Dappbar(): React.ReactElement {
  return (
    <div>
      <div className="bg-dappbar py-4">
        <Container className="position-relative">
          <h2>Dhost v2.0</h2>
          <h5>dhost-project/dhost-v2</h5>
          <Button className="position-absolute top-0 end-0 me-3">Visit</Button>
        </Container>
      </div>
      <div className="bg-light border-bottom">
        <Container>
          <Nav className="justify-content-evenly" activeKey="/home">
            <Nav.Item>
              <Nav.Link href="/home">Overview</Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link eventKey="link-1">Deploy</Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link eventKey="link-2">Source</Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link eventKey="link-2">Logs</Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link eventKey="link-2">Settings</Nav.Link>
            </Nav.Item>
          </Nav>
        </Container>
      </div>
    </div>
  )
}

export default Dappbar
