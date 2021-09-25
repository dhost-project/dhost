import { Dapp } from "models/api/Dapp"

import { List } from "./List"
import { ListItem } from "./ListItem"

export function ListDapp({ dapps }: { dapps: Dapp[] }): React.ReactElement {
  return (
    <List>
      {dapps.map((dapp) => (
        <ListItem key={`${dapp.slug}`} href={`/ipfs/${dapp.slug}`}>
          {dapp.slug}
        </ListItem>
      ))}
    </List>
  )
}
