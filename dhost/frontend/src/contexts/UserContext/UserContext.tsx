import { createContext, FC, useContext, useEffect, useState } from "react"
import { listDapps, retrieveDapp } from "api/Dapps"
import { Dapp } from "models/api/Dapp"

const UserContext = createContext({})

export const UserProvider: FC = ({ children }) => {
  const [userDapps, setUserDapps] = useState<Dapp[]>([])

  useEffect(() => {
    retrieveListDapps()
  }, [])

  async function retrieveListDapps() {
    const _listDapps = (await listDapps()).data
    setUserDapps(_listDapps)
  }

  return (
    <UserContext.Provider
      value={{
        userDapps,
      }}
    >
      {children}
    </UserContext.Provider>
  )
}

export const useUserContext = () => useContext(UserContext)
