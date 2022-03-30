import { meUser } from "api/Users"
import { User } from "models/api/User"
import { useEffect, useState } from "react"
import { useTranslation } from "react-i18next"

export function AccountSettings(): React.ReactElement {
  const { t } = useTranslation()
  const [state, setState] = useState<User>({
    id: "",
    username: "",
    email: "",
    avatar: ""
  })

  const fetchData = async () => {
    try {
      let res = await meUser()
      console.log(res.data)
      setState({ ...res.data })
    }
    catch (error) {
      console.log(error)
    }
  }

  const updateSettings = () => {
    console.log(state)
    // updateDapp()
    // setDapp({ ...dapp })
  }

  const changeUsername = (e: React.ChangeEvent<HTMLInputElement>) => {
    var _user = state
    _user.username = e.target.value;
    setState({ ..._user })
  }

  const changeEmail = (e: React.ChangeEvent<HTMLInputElement>) => {
    var _user = state
    _user.email = e.target.value;
    setState({ ..._user })
  }

  useEffect(() => {
    fetchData()
  }, [])

  return (
    <div className="container mx-auto">
      <h2>{t("ACCOUNT_SETTINGS_TITLE")}</h2>

      <div className="pb-4 w-1/2">
        <h2 className="block uppercase tracking-wide text-gray-700 text-xs font-medium mb-2">
          Username
        </h2>

        <input
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          type="text"
          value={state.username}
          onChange={(e) => {
            changeUsername(e)
          }}
        />
      </div>

      <div className="pb-4 w-1/2">
        <h2 className="block uppercase tracking-wide text-gray-700 text-xs font-medium mb-2">
          Email
        </h2>

        <input
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          type="text"
          value={state.email}
          onChange={(e) => {
            changeEmail(e)
          }}
        />
      </div>
      <div className="flex items-center">
        <button
          id="build"
          className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded"
          type="submit"
          name="build"
          onClick={updateSettings}
        >
          Validate
        </button>
      </div>
      <a className="btn btn-danger" href="/account/delete-confirm">
        Delete account
      </a>
    </div>
  )
}
