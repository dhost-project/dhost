import { toast } from "react-toastify"
import {
  DappContextType,
  DappProvider,
  useDapp,
} from "contexts/DappContext/DappContext"

type TParams = { dapp_slug: string }

export function ValidationButton(
  { dapp, setDapp }: DappContextType,
  props: { short: string }
): React.ReactElement {
  function displayData(e: React.MouseEvent<HTMLButtonElement>) {
    console.log(e.target)
    console.log(dapp)
    toast.info("Change done.", { position: toast.POSITION.BOTTOM_RIGHT })
  }

  return (
    <div>
      <div className="flex justify-center w-1/3">
        <div className="flex items-center">
          <button
            id={props.short}
            className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded"
            type="submit"
            onClick={displayData}
          >
            Validate
          </button>
        </div>
      </div>
    </div>
  )
}
