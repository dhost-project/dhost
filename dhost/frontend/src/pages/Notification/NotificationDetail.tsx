import { useTranslation } from "react-i18next"
import { Button } from "components/Button"
import { Notification } from "models/api/Notification"
import { useEffect } from "react"

export function NotificationDetail({
  notification,
}: {
  notification: Notification
}): React.ReactElement {
  // const { t } = useTranslation()

  const renderWells = (_notification: Notification) => {

    // console.log(_notification)
    return (
      <div className="container mx-auto">
        {/* <h2>{t("NOTIFICATION_DETAIL_TITLE")}</h2> */}
        <Button href="/notifications/">Back to list</Button>
        <h1>{_notification.subject}</h1>
        <p>{_notification.content}</p>
        <p>{_notification.url}</p>
        <p>{_notification.level}</p>
        <p>{_notification.timestamp}</p>

      </div>
    )
  }
  return (
    (notification !== undefined) ? renderWells(notification) : <span>"No details."</span>
  )
}
