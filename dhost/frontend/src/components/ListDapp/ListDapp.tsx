import { DappContext, DappContextType, IDapp, useDapp } from "contexts/DappContext/DappContext"
import { Dapp } from "models/api/Dapp"
import { List } from "./List"
import { ListItem } from "./ListItem"
import { useHistory } from "react-router-dom"
import { useEffect, useState } from "react"
import { listIPFSDapps } from "api/IPFSDapps"
import { render } from "@headlessui/react/dist/utils/render"


export function ListDapp({ dapps }: { dapps: Dapp[] }): React.ReactElement {

  let _dapps : IDapp[] = []
  const [localDapps, setLocalDapps] = useState<IDapp[]>([]);
  const {dapp, setDapp} = useDapp();
  let history = useHistory()


  const fetchDapps = async() => {
    try {
      console.log("fetching data from json")
      const response = await listIPFSDapps()
      const json = (await response).data
      console.log(json)
      console.log(json[0])
      for (let d of json) {

        console.log(d)

        dapp.basic.url = d.ipfs_gateway;
        dapp.basic.slug = d.slug;
        _dapps.push(dapp);
        console.log(_dapps.length)
      }
      console.log(dapp)
      console.log("dapps :")
      console.log(_dapps)
      setLocalDapps(_dapps)
    } catch (error) {
      console.log("error", error)
    }
  }
  

  useEffect(() => {
    fetchDapps()

    // (async function() {
      // const res = await listIPFSDapps()
      // console.log('listDapps', res)
      // updateState(state.append(res));
    // })()
  },[])

  function renderWells(){
    return     (<div className="mt-3 block">
    <hr className="mt-4 mb-3" />
    <div className="mx-5">
      {localDapps.map((dapp,i) => (
        <button
          key={i}
          className="w-full mb-3 mt-2 px-4 py-4 border-2 text-base text-gray-800 font-medium rounded-lg bg-white hover:bg-green-50 hover:border-green-400 focus:bg-green-50 focus:border-green-400 focus:ring-offset-0 focus:ring-green-400 focus:outline-none focus:ring-1 transition cursor-pointer"
          onClick={() => history.push(`/ipfs/${dapp.basic.slug}`)}
        >
          <p className="uppercase" style={{ textAlign: "left" }}>
            {dapp.basic.slug}
          </p>
        </button>
      ))}
    </div>
  </div>)
    }

  return (
    localDapps.length > 0 ?
    renderWells() : <span>Data loading...</span>
    // <></>
    // <List>
    //   {dapps.map((dapp) => (
    //     <ListItem key={`${dapp.slug}`} href={`/ipfs/${dapp.slug}`}>
    //       {dapp.slug}
    //     </ListItem>
    //   ))}
    // </List>


  )
}
