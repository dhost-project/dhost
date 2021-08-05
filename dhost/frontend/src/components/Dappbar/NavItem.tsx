import "./NavItem.css"

export function NavItem({
  href,
  isActive = false,
  children,
}: {
  href: string
  isActive?: boolean
  children: any
}): React.ReactElement {
  return (
    <a
      href={href}
      className={`dappbar-item relative px-3 py-2 text-gray-700 ${
        isActive ? "active" : "hover:text-gray-900"
      }`}
    >
      {children}
    </a>
  )
}
