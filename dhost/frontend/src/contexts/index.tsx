import { FC } from "react"
import { ModalsProvider } from "./ModalsContext/ModalsContext"

export const AppContext: FC = ({ children }) => {
  return <ModalsProvider>{children}</ModalsProvider>
}

export * from "./DappContext"
