import { ModalEnvVar } from "components/DappSettings/ModalEnvVar"
import { DappContextType } from "contexts/DappContext/DappContext"

function DappSettingsEnvVar({
  dapp,
  setDapp,
}: DappContextType): React.ReactElement {
  // <img className="my-2 mx-1 h-8 w-auto" src={tick} alt="True" />
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
      </table>
      <ModalEnvVar></ModalEnvVar>
    </>
  )
}

export default DappSettingsEnvVar
