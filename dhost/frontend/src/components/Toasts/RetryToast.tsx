import { ToastProps } from "react-toastify/dist/types"

interface CustomToastProps { // TODO find a better way to implement this class
  closeToast?: () => void
  toastProps?: ToastProps
  callback: Function
}

export function RetryToast({
  closeToast,
  callback,
}: CustomToastProps) {
  function executeAndClose() {
    callback()
    closeToast!() // '!' is used to assert that closeToast is defined otherwise we actually want an error
  }

  return (
    <div className="flex justify-evenly">
      This is a retry toast, <br/>
      Click "Retry" to do it again 👉
      <button
        className="bg-blue-600 ml-1 py-1 px-2 rounded hover:bg-blue-300"
        onClick={executeAndClose}
      >
        Retry
      </button>
    </div>
  )
}
