export default function Nav({
  children,
}: {
  children: React.ReactElement[]
}): React.ReactElement {
  return (
    <div className="border-b">
      <div className="container mx-auto relative">
        <nav className="flex justify-around">{children}</nav>
      </div>
    </div>
  )
}
