import { useEffect, useState } from "react"
import { listRepositorys } from "api/Repositories"
import { ConnectedGithubDeploy } from "./ConnectedGithubDeploy"
import { NotConnectedGithubDeploy } from "./NotConnectedGithubDeploy"

export function GithubDeploy() {
  const [isConnected, setIsConnected] = useState(false)

  useEffect(() => {
    getListRepositories()
  }, [])

  useEffect(() => {
    console.log("isConnected", isConnected)
  }, [isConnected])

  async function getListRepositories() {
    try {
      // TODO add a refetch button to enable manual refetch for user
      const listRepositoryRes = await listRepositorys()

      if (listRepositoryRes.status >= 200) {
        // console.log("setconnected true", listRepositoryRes.data)
        setIsConnected(true)
      }
    } catch (error: any) {
      // console.warn("getListRepositories", error)
      setIsConnected(false)
    }
  }

  return isConnected ? <ConnectedGithubDeploy /> : <NotConnectedGithubDeploy />
}
