import { getUserSettings, meUser, updateUserSettings } from "api/Users"
import { useUserContext } from "contexts/UserContext/UserContext"
import { User } from "models/api/User"
import { useEffect, useRef, useState } from "react"
import { useTranslation } from "react-i18next"

export function AccountSettings(): React.ReactElement {
  const { t } = useTranslation()
  const settingsRef = useRef<HTMLDivElement | undefined>()

  const { userInfo, setUserInfo } = useUserContext()
  const [page, setPage] = useState<string>();

  const changeUsername = (e: React.ChangeEvent<HTMLInputElement>) => {
    var _user = userInfo
    _user.user.username = e.target.value;
    setUserInfo({ ..._user })
  }

  const changeEmail = (e: React.ChangeEvent<HTMLInputElement>) => {
    var _user = userInfo
    _user.user.email = e.target.value;
    setUserInfo({ ..._user })
  }

  const updateSettings = () => {
    updateUserSettings({
      username: userInfo.user.username,
      email: userInfo.user.email,
      first_name: "",
      last_name: ""
    })
  }

  const fetchData = async () => {
    try {
      let res = await getUserSettings()
      setPage(res.data)
      if (!settingsRef.current) {
        return
      }
      settingsRef.current.querySelector("form")?.setAttribute("action", "/api/settings/")
      settingsRef.current.querySelector("form")?.setAttribute("target", "dummyframe")
      settingsRef.current.querySelector(".btn.btn-secondary")?.remove()
      settingsRef.current.querySelector(".btn.btn-danger")?.remove()
      settingsRef.current.querySelector(".btn.btn-primary")?.addEventListener("click", () => {
        window.location.href = "/account/settings/"
      })
    }
    catch (error) {
      console.log(error)
    }
  }

  useEffect(() => {
    fetchData()
  }, [])

  return (
    <>
      <iframe name="dummyframe" id="dummyframe" style={{ display: "none" }}></iframe>
      <div className="content" ref={settingsRef as any} dangerouslySetInnerHTML={{ __html: (page ?? "") }}></div>
    </>
  )
}
