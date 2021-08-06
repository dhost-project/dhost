import { Notification } from "models/Notification"

export function ListItem({
  notification,
}: {
  notification: Notification
}): React.ReactElement {
  var colors = "bg-gray-100 text-gray-600 hover:bg-gray-200 hover:text-gray-700"

  if (notification.level === "success") {
    colors =
      "bg-green-100 text-green-600 hover:bg-green-200 hover:text-green-700"
  } else if (notification.level === "warning") {
    colors =
      "bg-yellow-100 text-yellow-600 hover:bg-yellow-200 hover:text-yellow-700"
  } else if (notification.level === "error") {
    colors = "bg-red-100 text-red-600 hover:bg-red-200 hover:text-red-700"
  }

  return (
    <a
      className={`${colors} px-4 py-2`}
      href={`/notifications/${notification.id}/`}
    >
      {notification.subject}
    </a>
  )
}
