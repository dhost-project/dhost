import { SetStateAction, Dispatch } from "react"
import { createContext, FC, Context, useState, useContext } from "react"
import { fetchAllRepository } from "api/Repositories"
import { BuildOptions } from "models/api/BuildOptions"
import { Dapp } from "models/api/Dapp"
import { EnvVar } from "models/api/EnvVar"
import { GithubOptions } from "models/api/GithubOptions"
import { Repository } from "models/api/Repository"

// type StateSetter<T> = (value: T | ((value: T) => T)) => void;
export interface IDapp {
  basic: Dapp
  build: BuildOptions
  github: GithubOptions
  env_vars: EnvVar[]
}

export interface DappContextType {
  dapp: IDapp
  setDapp: Dispatch<SetStateAction<IDapp>> // StateSetter<number>
  userRepo: Repository[]
  setUserRepo: Dispatch<SetStateAction<Repository[]>>
  updateRemoteUserRepo(): Promise<void>
}

export const DappContext = createContext({} as DappContextType)

export const DappProvider: FC = ({ children }) => {
  const _dapp: IDapp = {
    basic: {
      slug: "dapp_1",
      url: "gateway.com",
      owner: "filipo",
      status: "down",
      created_at: "08/08/08",
    },
    build: {
      command: "npm install",
      docker: "Dockerfile",
    },
    github: {
      repo: "best_repo",
      branch: 2,
      auto_deploy: false,
      confirm_ci: false,
    },
    env_vars: [
      {
        variable: "first_var",
        value: "val_var",
        sensitive: false,
      },
      {
        variable: "sec_var",
        value: "val_var",
        sensitive: true,
      },
    ],
  } as IDapp

  const [dapp, setDapp] = useState<IDapp>(_dapp)
  const [userRepo, setUserRepo] = useState<Repository[]>([] as Repository[])

  const updateRemoteUserRepo = async () => {
    try {
      const res = await fetchAllRepository()
      console.warn("updateRemoteUserRepo", res)
    } catch (e) {
      console.warn("updateRemoteUserRepo error", e)
    }
  }

  return (
    <DappContext.Provider
      value={{
        dapp,
        setDapp,
        userRepo,
        setUserRepo,
        updateRemoteUserRepo,
      }}
    >
      {children}
    </DappContext.Provider>
  )
}

export const useDapp = (): DappContextType =>
  useContext(DappContext) as DappContextType
