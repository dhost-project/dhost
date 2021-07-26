import Container from "react-bootstrap/Container"

import "./style.scss"

function Footer(): React.ReactElement {
  return (
    <footer>
      <div id="footer-nav">
        <Container></Container>
      </div>
      <div id="footer-bottom">
        <Container className="py-1">DHost 2020-2021.</Container>
      </div>
    </footer>
  )
}

export default Footer
