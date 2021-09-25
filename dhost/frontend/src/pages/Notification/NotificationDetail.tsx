import { useTranslation } from "react-i18next"

import { Button } from "components/Button"

import { Notification } from "models/api/Notification"

export function NotificationDetail({
  notification,
}: {
  notification: Notification
}): React.ReactElement {
  const { t } = useTranslation()

  return (
    <div className="container mx-auto">
      <h2>{t("NOTIFICATION_DETAIL_TITLE")}</h2>
      <Button href="/notifications/">Back to list</Button>
      <h1>{notification.subject}</h1>
      <p>{notification.content}</p>
    </div>
  )
}
