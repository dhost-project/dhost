import { FC } from "react"
import { DappProvider } from "./DappContext/DappContext"
import { EnvVarModalsProvider } from "./EnvVarModalsContext/EnvVarModalsContext"
import { ModalsProvider } from "./ModalsContext/ModalsContext"
import { UserProvider } from "./UserContext/UserContext"

export const AppContext: FC = ({ children }) => {
  return (
    <UserProvider>
      <DappProvider>
        <ModalsProvider><EnvVarModalsProvider>{children}</EnvVarModalsProvider> </ModalsProvider>
      </DappProvider>
    </UserProvider>
  )
}

export * from "./DappContext"
