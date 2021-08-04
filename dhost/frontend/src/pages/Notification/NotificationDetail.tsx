import { useTranslation } from "react-i18next"

import Notification from "models/Notification"

function NotificationDetail({
  notification,
}: {
  notification: Notification
}): React.ReactElement {
  const { t } = useTranslation()

  return (
    <div className="container mx-auto">
      <h2>{t("NOTIFICATION_DETAIL_TITLE")}</h2>
      <h1>{notification.subject}</h1>
      <p>{notification.content}</p>
    </div>
  )
}

export default NotificationDetail
