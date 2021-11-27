import { SetStateAction, Dispatch } from "react"
import { createContext, FC, Context, useState, useContext } from "react"
import { BuildOptions } from "models/api/BuildOptions"
import { Dapp } from "models/api/Dapp"
import { EnvVar } from "models/api/EnvVar"
import { GithubOptions } from "models/api/GithubOptions"

// type StateSetter<T> = (value: T | ((value: T) => T)) => void;
export interface IDapp {
  basic: Dapp
  build: BuildOptions
  github: GithubOptions
  env_vars: EnvVar[]
}

export type DappContextType = {
  dapp: IDapp
  setDapp: Dispatch<SetStateAction<IDapp>> // StateSetter<number>
}

export const DappContext: Context<Partial<DappContextType>> = createContext<
  Partial<DappContextType>
>({})

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
  const props = {
    dapp,
    setDapp,
  } as DappContextType

  return <DappContext.Provider value={props}>{children}</DappContext.Provider>
}

export const useDapp = (): DappContextType =>
  useContext(DappContext) as DappContextType
