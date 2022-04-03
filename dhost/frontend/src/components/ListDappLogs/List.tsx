export function List({
  children,
}: {
  children: React.ReactElement[]
}): React.ReactElement {
  return <div className="flex flex-col divide-y rounded">{children}</div>
}
