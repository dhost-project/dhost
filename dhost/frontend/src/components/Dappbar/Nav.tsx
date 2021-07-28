export default function Nav({
  children,
}: {
  children: React.ReactElement[]
}): React.ReactElement {
  return (
    <div className="border-b-2">
      <div className="container mx-auto relative">
        <nav id="nav-dappbar" className="flex justify-around">
          {children}
        </nav>
      </div>
    </div>
  )
}
