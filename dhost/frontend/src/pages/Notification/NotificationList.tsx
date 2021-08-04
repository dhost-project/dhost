import { useTranslation } from "react-i18next"

import ListNotification from "components/ListNotification"

import Notification from "models/Notification"

function NotificationList({
  notifications,
}: {
  notifications: Notification[]
}): React.ReactElement {
  const { t } = useTranslation()

  return (
    <div className="container mx-auto">
      <h2>{t("NOTIFICATION_LIST_TITLE")}</h2>
      <ListNotification notifications={notifications} />
    </div>
  )
}

export default NotificationList
