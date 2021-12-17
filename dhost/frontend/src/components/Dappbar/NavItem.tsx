import { ReactElement, useEffect, useState } from "react"
import { Link, useLocation } from "react-router-dom"
import "./NavItem.css"

interface INavItem {
  href: string
  children: any
}

export function NavItem({ href, children }: INavItem): ReactElement {
  const location = useLocation()
  const [isActive, setIsActive] = useState(false)

  useEffect(() => {
    setIsActive(location.pathname === href)
  }, [location, href])

  return (
    <Link
      to={href}
      className={`dappbar-item relative px-3 py-2 text-gray-700 ${
        isActive ? "active" : "hover:text-gray-900"
      }`}
    >
      {children}
    </Link>
  )
}
