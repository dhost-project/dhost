import { FC } from "react"
import { DappProvider } from "./DappContext/DappContext"
import { ModalsProvider } from "./ModalsContext/ModalsContext"
import { UserProvider } from "./UserContext/UserContext"

export const AppContext: FC = ({ children }) => {
  return (
    <UserProvider>
      <DappProvider>
        <ModalsProvider>{children}</ModalsProvider>
      </DappProvider>
    </UserProvider>
  )
}

export * from "./DappContext"
