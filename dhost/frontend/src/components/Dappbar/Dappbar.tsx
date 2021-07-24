import { faGithub } from "@fortawesome/free-brands-svg-icons"
import { faExternalLinkAlt } from "@fortawesome/free-solid-svg-icons"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import Button from "react-bootstrap/Button"
import Container from "react-bootstrap/Container"
import Nav from "react-bootstrap/Nav"

import "./style.scss"

function Dappbar(): React.ReactElement {
  return (
    <div>
      <div id="bg-dappbar" className="py-4 border-bottom">
        <Container className="position-relative">
          <h2>Dhost v2.0</h2>
          <h5>
            <FontAwesomeIcon icon={faGithub} /> dhost-project/dhost-v2
          </h5>
          <Button
            id="btn-visit"
            className="position-absolute top-0 end-0"
            href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
          >
            Visit <FontAwesomeIcon icon={faExternalLinkAlt} />
          </Button>
        </Container>
      </div>
      <div className="bg-light border-bottom border-2">
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
