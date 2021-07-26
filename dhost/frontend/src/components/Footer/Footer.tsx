import "./style.scss"

function Footer(): React.ReactElement {
  return (
    <footer>
      <div className="d-flex border-top bg-light fw-light py-2 px-2">
        <div className="me-auto">
          <a href="https://github.com/dhost-project/dhost-doc" target="_blank">
            Documentation
          </a>
          <a
            href="https://github.com/dhost-project/dhost-examples"
            target="_blank"
          >
            Examples
          </a>
          <a href="https://github.com/dhost-project/dhost" target="_blank">
            Source code
          </a>
          <a
            href="https://github.com/dhost-project/dhost/issues/new"
            target="_blank"
          >
            Issues
          </a>
          <a href="">Support</a>
        </div>
        <div>
          <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" target="_blank">
            Privacy
          </a>
          <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" target="_blank">
            Legal
          </a>
          <a href="/">
            <span className="text-primary">D</span>Host 2020-2021
          </a>
        </div>
      </div>
    </footer>
  )
}

export default Footer
