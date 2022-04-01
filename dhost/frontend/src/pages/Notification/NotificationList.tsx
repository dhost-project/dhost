import { SearchIcon } from "@heroicons/react/outline"
import { useTranslation } from "react-i18next"
import { Button } from "components/Button"
import { ListNotification } from "components/ListNotification"
import { Notification } from "models/api/Notification"
import { useUserContext } from "contexts/UserContext/UserContext"

export function NotificationList(): React.ReactElement {
  const { t } = useTranslation()



  return (
    <div className="container mx-auto py-4">
      <form className="flex flex-1">
        <input
          type="text"
          className="px-2 py-1 rounded-l border text-gray-700"
          placeholder="Search dapps"
        />
        <button
          className="flex-none px-2 text-gray-500 rounded-r border-r
                border-b border-t hover:bg-gray-100"
        >
          <SearchIcon className="h-5" />
        </button>
      </form>
      <div className="flex py-2">
        <Button size="sm">{t("Mark all as read")}</Button>
        <Button size="sm">{t("Mark all as un-read")}</Button>
      </div>
      <ListNotification />
    </div>
  )
}
