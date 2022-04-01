import { DappProvider, useDapp } from "contexts/DappContext/DappContext"
import { Nav } from "./Nav"
import { NavItem } from "./NavItem"

export const Dappbar = () => {
  let { dapp } = useDapp()

  return (
    <div>
      <div className="py-4 px-4 border-b bg-gradient-to-r from-green-100 to-blue-100">
        <div className="container-fluid mx-auto relative w-100 md:w-75 lg:w-75">
          <h1 className="text-4xl">
            <a
              className="text-reset text-decoration-none"
              href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            >
              {dapp.basic.slug.toUpperCase()}
            </a>
          </h1>
          <h2 className="text-xl">
            <a
              className="text-reset text-decoration-none"
              href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
              rel="noreferrer"
              target="_blank"
            >
              {dapp.basic.url}
            </a>
          </h2>
          <a
            className="absolute top-0 right-0 bg-green-500 border-solid border border-secondary-light rounded-md px-5 py-2 text-white"
            href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            rel="noreferrer"
            target="_blank"
          >
            Visit
          </a>
        </div>
      </div>
      <DappProvider>
        <Nav>
          <NavItem href={`/dapps/${dapp.basic.slug}/`}>Overview</NavItem>
          <NavItem href={`/dapps/${dapp.basic.slug}/deploy`}>Deploy</NavItem>
          <NavItem href={`/dapps/${dapp.basic.slug}/source`}>Source</NavItem>
          <NavItem href={`/dapps/${dapp.basic.slug}/logs`}>Logs</NavItem>
          <NavItem href={`/dapps/${dapp.basic.slug}/settings`}>
            Settings
          </NavItem>
        </Nav>
      </DappProvider>
    </div>
  )
}
