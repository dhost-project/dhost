import Dapp from "models/Dapp"

import List from "./List"
import ListItem from "./ListItem"

export default function DappList({
  dapps,
}: {
  dapps: Dapp[]
}): React.ReactElement {
  return (
    <List>
      {dapps.map((dapp) => (
        <ListItem href={`/ipfs/${dapp.slug}`}>{dapp.slug}</ListItem>
      ))}
    </List>
  )
}
