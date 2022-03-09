import { useEffect, useState } from "react"
import { listRepositorys } from "api/Repositories"
import { useDapp } from "contexts/DappContext/DappContext"
import { ConnectedGithubDeploy } from "./ConnectedGithubDeploy"
import { NotConnectedGithubDeploy } from "./NotConnectedGithubDeploy"

export function GithubDeploy() {
  const { setUserRepo } = useDapp()
  const [isConnected, setIsConnected] = useState(false)

  useEffect(() => {
    getListRepositorys()
  }, [])

  useEffect(() => {
    console.log("isConnected", isConnected)
  }, [isConnected])

  async function getListRepositorys() {
    try {
      const res = await listRepositorys()
      console.log("listRepositorys", res)

      if (res.status >= 200) {
        console.log("setconnected true", res.data)
        setIsConnected(true)
        setUserRepo([])
      }
    } catch (error: any) {
      console.warn("getListRepositorys", error)
      setIsConnected(false)
    }
  }

  return isConnected ? (
    <ConnectedGithubDeploy setIsConnected={setIsConnected} />
  ) : (
    <NotConnectedGithubDeploy />
  )
}
