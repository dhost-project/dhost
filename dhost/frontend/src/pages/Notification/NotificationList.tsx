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
      <ListNotification />
    </div>
  )
}
