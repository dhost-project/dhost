import { useEffect, useState } from "react"
import { listRepositorys } from "api/Repositories"
import { useDapp } from "contexts/DappContext/DappContext"
import { ConnectedGithubDeploy } from "./ConnectedGithubDeploy"
import { NotConnectedGithubDeploy } from "./NotConnectedGithubDeploy"

export function GithubDeploy() {
  const { setUserRepo } = useDapp()
  const [isConnected, setIsConnected] = useState(false)

  useEffect(() => {
    getListRepositories()
  }, [])

  useEffect(() => {
    console.log("isConnected", isConnected)
  }, [isConnected])

  async function getListRepositories() {
    try {
      const res = await listRepositorys()
      console.log("listRepositories", res)

      if (res.status >= 200) {
        console.log("setconnected true", res.data)
        setIsConnected(true)
        setUserRepo([])
      }
    } catch (error: any) {
      console.warn("getListRepositories", error)
      setIsConnected(false)
    }
  }

  return isConnected ? (
    <ConnectedGithubDeploy setIsConnected={setIsConnected} />
  ) : (
    <NotConnectedGithubDeploy />
  )
}
