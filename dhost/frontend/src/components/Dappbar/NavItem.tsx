export default function NavItem({
  href,
  isActive = false,
  children,
}: {
  href: string
  isActive?: boolean
  children: any
}): React.ReactElement {
  return (
    <a href={href} className={`p-2 ${isActive ? "active relative" : ""}`}>
      {children}
    </a>
  )
}
