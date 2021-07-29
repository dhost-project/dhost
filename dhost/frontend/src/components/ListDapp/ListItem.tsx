export default function ListItem({
  href,
  isActive = false,
  children,
}: {
  href: string
  isActive?: boolean
  children: any
}): React.ReactElement {
  return (
    <a className="px-4 py-2" href={href}>
      {children}
    </a>
  )
}
