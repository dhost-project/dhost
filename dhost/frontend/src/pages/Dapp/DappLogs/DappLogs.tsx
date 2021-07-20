import { RouteComponentProps } from 'react-router-dom'
import { useTranslation } from 'react-i18next'
import './styles.scss'

type TParams = { dapp_slug: string }

function Logs({ match }: RouteComponentProps<TParams>): React.ReactElement {
  const { t } = useTranslation()

  return (
    <div>
      <h2>
        {t('LOGS_TITLE')} {match.params.dapp_slug}
      </h2>
    </div>
  )
}

export default Logs
