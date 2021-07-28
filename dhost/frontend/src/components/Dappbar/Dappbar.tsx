import "./style.css"

export default function Dappbar(): React.ReactElement {
  return (
    <div>
      <div id="bg-dappbar" className="py-4 border-b">
        <div className="container mx-auto relative">
          <h1 className="text-4xl">
            <a
              className="text-reset text-decoration-none"
              href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            >
              Dhost v2.0
            </a>
          </h1>
          <h2 className="text-xl">
            <a
              className="text-reset text-decoration-none"
              href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
              rel="noreferrer"
              target="_blank"
            >
              dhost-project/dhost-v2
            </a>
          </h2>
          <a
            className="absolute top-0 right-0"
            href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            rel="noreferrer"
            target="_blank"
          >
            Visit
          </a>
        </div>
      </div>
      <div className="border-b-2">
        <div className="container mx-auto relative">
          <div id="nav-dappbar" className="flex justify-around">
            <a href="/home" className="active p-2">
              Overview
            </a>
            <a href="link-1" className="p-2">
              Deploy
            </a>
            <a href="link-2" className="p-2">
              Source
            </a>
            <a href="link-2" className="p-2">
              Logs
            </a>
            <a href="link-2" className="p-2">
              Settings
            </a>
          </div>
        </div>
      </div>
    </div>
  )
}
