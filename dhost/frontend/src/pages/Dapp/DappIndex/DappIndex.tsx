import { RouteComponentProps } from 'react-router-dom'
import { useTranslation } from 'react-i18next'
import './styles.scss'

type TParams = { slug: string }

function Overview({ match }: RouteComponentProps<TParams>): React.ReactElement {
  const { t } = useTranslation()

  return (
    <div>
      <h2>
        {t('OVERVIEW_TITLE')} {match.params.slug}
      </h2>
    </div>
  )
}

export default Overview
