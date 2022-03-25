import { Dispatch, SetStateAction } from "react"
import { ModalEnvVar } from "components/DappSettings/ModalEnvVar"
import { DappContextType, IDapp } from "contexts/DappContext/DappContext"
import { Button } from "react-bootstrap"
import { useEnvVarModals } from "contexts/EnvVarModalsContext/EnvVarModalsContext"

function DappSettingsEnvVar({
  dapp,
  setDapp,
}: {
  dapp: IDapp
  setDapp: Dispatch<SetStateAction<IDapp>>
}): React.ReactElement {

  const { setShowCreateEnvVarModal } = useEnvVarModals()


  function renderSensitive(sensistive: boolean | undefined) {
    if (sensistive) {
      return <span>✓</span>
    } else {
      return
    }
  }

  return (
    <>
      <table className="table-fixed w-full text-align">
        <thead>
          <tr>
            <th className="w-1/3 uppercase tracking-wide text-gray-700 text-xs font-medium mb-2 mr-2 pb-5">
              Variable
            </th>
            <th className="w-1/3 uppercase tracking-wide text-gray-700 text-xs font-medium mb-2 mr-2 pb-5">
              Value
            </th>
            <th className="w-1/3 uppercase tracking-wide text-gray-700 text-xs font-medium mb-2 mr-2 pb-5">
              Sensitive
            </th>
          </tr>
        </thead>
        <tbody>
          {dapp.env_vars.map((_env_var, i) => (
            <tr key={`${_env_var.variable}-${i}`}>
              <td>{_env_var.variable}</td>
              <td>{_env_var.value}</td>
              <td>{renderSensitive(_env_var.sensitive)}</td>
            </tr>
          ))}
        </tbody>
        <Button
          className="flex justify-center items-center h-8 mr-4"
          onClick={() => {
            setShowCreateEnvVarModal(true)
          }}
        >
          New
        </Button>
      </table>
    </>
  )
}

export default DappSettingsEnvVar
