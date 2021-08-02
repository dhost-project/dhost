import Dapp from "models/Dapp"

import Nav from "./Nav"
import NavItem from "./NavItem"

export default function Dappbar({ dapp }: { dapp: Dapp }): React.ReactElement {
  return (
    <div>
      <div className="py-4 border-b bg-gradient-to-r from-green-100 to-blue-100">
        <div className="container mx-auto relative">
          <h1 className="text-4xl">
            <a
              className="text-reset text-decoration-none"
              href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            >
              {dapp.slug}
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
            className="absolute top-0 right-0 bg-primary border-solid border border-secondary-light rounded-md px-5 py-2"
            href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            rel="noreferrer"
            target="_blank"
          >
            Visit
          </a>
        </div>
      </div>
      <Nav>
        <NavItem href={`/ipfs/${dapp.slug}/`} isActive>
          Overview
        </NavItem>
        <NavItem href={`/ipfs/${dapp.slug}/deploy`}>Deploy</NavItem>
        <NavItem href={`/ipfs/${dapp.slug}/source`}>Source</NavItem>
        <NavItem href={`/ipfs/${dapp.slug}/logs`}>Logs</NavItem>
        <NavItem href={`/ipfs/${dapp.slug}/settings`}>Settings</NavItem>
      </Nav>
    </div>
  )
}
