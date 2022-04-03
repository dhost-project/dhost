import { createContext, Dispatch, FC, SetStateAction, useContext, useEffect, useState } from "react"
import { listDapps, retrieveDapp } from "api/Dapps"
import { Dapp } from "models/api/Dapp"
import { User } from "models/api/User"
import { Notification } from "models/api/Notification"
import { listNotifications } from "api/Notifications"
import { meUser } from "api/Users"
import { Repository } from "models/api/Repository";
import { fetchAllRepository } from "api/Repositories";

export interface IUser {
  user: User
  dapps: Dapp[]
  notifications: Notification[]
  subscription: string
  githubRepositories: Repository[]
  isConnected: boolean
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
    subscription: "",
    githubRepositories: [],
    isConnected: false
  }

  const [userInfo, setUserInfo] = useState<IUser>(_iUser)

  useEffect(() => {
    retrieveData()
  }, [])

  useEffect(() => {
    console.log("user", userInfo)
  }, [userInfo])

  async function retrieveData() {
    const _userRes = await meUser()

    if (_userRes.status === 401) {
      setUserInfo(userInfo => ({
        ...userInfo,
        isConnected: false
      }))
      return
    }

    const [_listDapps, _listNotifications, _listRepositories] =
      await Promise.all([
        (await listDapps()).data,
        (await listNotifications()).data,
        (await fetchAllRepository().catch((error) => { console.warn(error) }))?.data ?? [],
      ])

    const _userInfo: IUser = {
      user: _userRes.data,
      dapps: _listDapps,
      notifications: _listNotifications,
      subscription: "Free",
      githubRepositories: _listRepositories,
      isConnected: true
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
