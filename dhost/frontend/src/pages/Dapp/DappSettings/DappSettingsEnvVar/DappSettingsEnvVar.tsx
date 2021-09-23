import { DappContextType } from "contexts/DappContext/DappContext"

import tick from "assets/tick.png";

function DappSettingsEnvVar({ dapp, setDapp }: DappContextType): React.ReactElement {


  function renderSensitive(sensistive: boolean | undefined) {
    if (sensistive) {
      return <img className="my-2 mx-1 h-8 w-auto" src={tick} alt="True" />
    }
    else {
      return 
    }
  }

  return (
      <table className="table-fixed w-full">
        <thead>
          <tr>
            <th className="w-1/3">Variable</th>
            <th className="w-1/3">Value</th>
            <th className="w-1/3">Sensitive</th>
          </tr>
        </thead>
        <tbody>
          {dapp.env_vars.map((_env_var) =>
            <tr>
              <td>{_env_var.variable}</td>
              <td>{_env_var.value}</td>
              <td>{renderSensitive(_env_var.sensitive)}</td>
            </tr>
          )}
        </tbody>
      </table>
  )
}

export default DappSettingsEnvVar
