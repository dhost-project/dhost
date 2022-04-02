import {
  createContext,
  Dispatch,
  FC,
  SetStateAction,
  useContext,
  useEffect,
  useState,
} from "react"
import { listDapps, retrieveDapp } from "api/Dapps"
import { listNotifications } from "api/Notifications"
import { fetchAllRepository } from "api/Repositories"
import { meUser } from "api/Users"
import { Dapp } from "models/api/Dapp"
import { Notification } from "models/api/Notification"
import { Repository } from "models/api/Repository"
import { User } from "models/api/User"

export interface IUser {
  user: User
  dapps: Dapp[]
  notifications: Notification[]
  subscription: string
  githubRepositories: Repository[]
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
      id: "",
    },
    dapps: [],
    notifications: [],
    subscription: "",
    githubRepositories: [],
  }

  const [userInfo, setUserInfo] = useState<IUser>(_iUser)

  useEffect(() => {
    retrieveData()
  }, [])

  useEffect(() => {
    console.log("user", userInfo)
  }, [userInfo])

  async function retrieveData() {
    const [_listDapps, _listNotifications, _listRepositories] =
      await Promise.all([
        (await listDapps()).data,
        (await listNotifications()).data,
        (await fetchAllRepository()).data,
      ])

    const _user = (await meUser()).data
    const _userInfo: IUser = {
      user: _user,
      dapps: _listDapps,
      notifications: _listNotifications,
      subscription: "Free",
      githubRepositories: _listRepositories,
    }
    setUserInfo({ ..._userInfo })
  }

  return (
    <UserContext.Provider
      value={{
        userInfo,
        setUserInfo,
      }}
    >
      {children}
    </UserContext.Provider>
  )
}

export const useUserContext = (): UserContextType =>
  useContext(UserContext) as UserContextType
