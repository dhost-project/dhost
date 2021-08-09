import { useTranslation } from "react-i18next"
import { RouteComponentProps } from "react-router-dom"
import Dappbar from '../../../components/Dappbar/Dappbar';
import DappSettingsElement from "../../../components/DappSettingsElement";
import { CounterProvider } from "../../../contexts/DappContext/DappContext";

type TParams = { dapp_slug: string }


function Settings({ match }: RouteComponentProps<TParams>): React.ReactElement {
  const { t } = useTranslation()
  // const state: Map = { hello : 'hello', world: 'world'}

  return (
    <div>
      <Dappbar></Dappbar>
      <h2>
        {t("SETTINGS_TITLE")} {match.params.dapp_slug}
      </h2>
      <CounterProvider>
        <DappSettingsElement title="toto" desc="tata"></DappSettingsElement>
      </CounterProvider>
    </div>
  )
}

export default Settings
