import { DappContext, DappContextType, IDapp, useDapp } from "contexts/DappContext/DappContext"
import { Dapp } from "models/api/Dapp"
import { List } from "./List"
import { ListItem } from "./ListItem"

import { useEffect, useState } from "react"
import { listIPFSDapps } from "api/IPFSDapps"


export function ListDapp({ dapps }: { dapps: Dapp[] }): React.ReactElement {

  let _dapps : DappContextType[] = []
  const [state, setState] = useState([]);
  const {dapp, setDapp} = useDapp();


  const fetchData = async() => {
    try {
      const response = await listIPFSDapps()
      const json = (await response).data
      console.log(json)
      for (let d of json) {
        // var _dapp = dapp;
        // _dapp.basic = d;
        // _dapp.basic.owner = d.owner
        var _dapp = dapp;
        _dapp.basic.url = d.ipfs_gateway;
        _dapp.basic.slug = d.slug;
        setDapp({... _dapp});
        _dapps.push({dapp, setDapp});
      }
      console.log(dapp)
    } catch (error) {
      console.log("error", error)
    }
  }

  useEffect(() => {
    fetchData()

    // (async function() {
      // const res = await listIPFSDapps()
      // console.log('listDapps', res)
      // updateState(state.append(res));
    // })()
  })

  return (
    // <></>
    <List>
      {dapps.map((dapp) => (
        <ListItem key={`${dapp.slug}`} href={`/ipfs/${dapp.slug}`}>
          {dapp.slug}
        </ListItem>
      ))}
    </List>
  )
}
