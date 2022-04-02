import { FC } from "react"
import { DappProvider } from "./DappContext/DappContext"
import { EnvVarModalsProvider } from "./EnvVarModalsContext/EnvVarModalsContext"
import { ModalsProvider } from "./ModalsContext/ModalsContext"
import { ModalsDestroyDappProvider } from "./ModalsContext/ModalsDappDestroyContext"

import { UserProvider } from "./UserContext/UserContext"

export const AppContext: FC = ({ children }) => {
  return (
    <UserProvider>
      <DappProvider>
        <ModalsProvider>
          <EnvVarModalsProvider>
            <ModalsDestroyDappProvider>
              {children}
            </ModalsDestroyDappProvider>
          </EnvVarModalsProvider>
        </ModalsProvider>
      </DappProvider>
    </UserProvider>
  )
}

export * from "./DappContext"
