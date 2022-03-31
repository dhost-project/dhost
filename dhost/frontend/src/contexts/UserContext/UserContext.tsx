import { createContext, Dispatch, FC, SetStateAction, useContext, useEffect, useState } from "react"
import { listDapps, retrieveDapp } from "api/Dapps"
import { Dapp } from "models/api/Dapp"
import { User } from "models/api/User"
import { Notification } from "models/api/Notification"
import { listNotifications } from "api/Notifications"
import { meUser } from "api/Users"

export interface IUser {
  user: User
  dapps: Dapp[]
  notifications: Notification[]
  subscription: string
}

export interface UserContextType {
  userInfo: IUser
  setUserInfo: Dispatch<SetStateAction<IUser>>
}

export const UserContext = createContext({})

export const UserProvider: FC = ({ children }) => {

  const _iUser: IUser = {
    user: {
      username: "",
      email: "",
      avatar: "",
      id: ""
    },
    dapps: [],
    notifications: [],
    subscription: ""
  }

  const [userInfo, setUserInfo] = useState<IUser>(_iUser)

  useEffect(() => {
    retrieveData()
  }, [])

  async function retrieveData() {
    const _listDapps = (await listDapps()).data
    const _listNotifications = (await listNotifications()).data
    console.log(_listNotifications)
    const _user = (await meUser()).data
    const _userInfo: IUser = {
      user: _user,
      dapps: _listDapps,
      notifications: _listNotifications,
      subscription: "Free"
    }
    setUserInfo({ ..._userInfo })
  }

  return (
    <UserContext.Provider
      value={{
        userInfo,
        setUserInfo
      }}
    >
      {children}
    </UserContext.Provider>
  )
}

export const useUserContext = (): UserContextType => useContext(UserContext) as UserContextType
