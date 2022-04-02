import { SetStateAction, Dispatch, useEffect } from "react"
import { createContext, FC, Context, useState, useContext } from "react"
import { fetchAllRepository } from "api/Repositories"
import { BuildOptions } from "models/api/BuildOptions"
import { DappLogs } from "models/api/DappLogs"
import { EnvVar } from "models/api/EnvVar"
import { GithubOptions } from "models/api/GithubOptions"
import { IPFSDapp } from "models/api/IPFSDapp"

// type StateSetter<T> = (value: T | ((value: T) => T)) => void;
export interface IDapp {
  basic: IPFSDapp
  build: BuildOptions
  github: GithubOptions
  env_vars: EnvVar[]
  dappLogsList: DappLogs[]
}

export interface DappContextType {
  dapp: IDapp
  setDapp: Dispatch<SetStateAction<IDapp>> // StateSetter<number>
}

export const DappContext = createContext({} as DappContextType)

export const DappProvider: FC = ({ children }) => {
  const _dapp: IDapp = {
    basic: {
      slug: "",
      url: "",
      owner: "",
      status: "",
      created_at: "",
      ipfs_gateway: "",
      ipfs_hash: "",
    },
    build: {
      command: "",
      docker: "",
    },
    github: {
      repo: "",
      branch: 0,
      auto_deploy: false,
      confirm_ci: false,
    },
    env_vars: [
      {
        variable: "",
        value: "",
        sensitive: false,
      },
    ],
    dappLogsList: [],
  } as IDapp

  const [dapp, setDapp] = useState<IDapp>(_dapp)

  // TODO update dapp context when route/dapp_slug change

  return (
    <DappContext.Provider
      value={{
        dapp,
        setDapp,
      }}
    >
      {children}
    </DappContext.Provider>
  )
}

export const useDapp = (): DappContextType =>
  useContext(DappContext) as DappContextType
