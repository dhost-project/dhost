export function ListItem({
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
      className="px-4 py-2 hover:bg-gray-50 hover:text-gray-700 rounded"
      href={href}
    >
      {children}
    </a>
  )
}
