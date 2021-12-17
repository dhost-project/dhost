import { useTranslation } from "react-i18next"
import { toast } from "react-toastify"
import { RetryToast } from "components/Toasts/RetryToast"

export function Home(): React.ReactElement {
  const { t } = useTranslation()

  // Toaster retry example
  async function startToasting(seconds: number = 3) {
    const toastId = toast.loading(`⏳ Please hold on ${seconds} seconds ⏳`)

    await new Promise((resolve) => {
      // Too simulate long stuff happening
      let _seconds = seconds

      const intervalRef = setInterval(() => {
        toast.update(toastId, {
          render: `⏳ Please hold on ${--_seconds || "🎉"} seconds ⏳`,
        })

        if (_seconds <= 0) {
          resolve(true)
          clearInterval(intervalRef)
        }
      }, 1000)
    })

    toast.dismiss(toastId)
    toast(<RetryToast callback={() => startToasting(seconds + 1)} />, {
      type: "info",
    })
  }

  return (
    <div className="container mx-auto">
      <h2>{t("HOME_TITLE")}</h2>

      <div className="flex flex-wrap">
        <button
          className="bg-gray-300 p-1 m-1"
          onClick={() => toast("Test notification")}
        >
          Notification test
        </button>
        <button
          className="bg-gray-300 p-1 m-1"
          onClick={() => toast.success("Test success notification")}
        >
          Notification test
        </button>
        <button
          className="bg-gray-300 p-1 m-1"
          onClick={() => toast.error("Test error notification")}
        >
          Notification error test
        </button>
        <button
          className="bg-gray-300 p-1 m-1"
          onClick={() => toast.warning("Test warning notification")}
        >
          Notification error test
        </button>
        <button
          className="bg-gray-300 p-1 m-1"
          onClick={() => toast.info("Test info notification")}
        >
          Notification error test
        </button>
        <button className="bg-gray-300 p-1 m-1" onClick={() => startToasting()}>
          Retry test
        </button>
      </div>
    </div>
  )
}
