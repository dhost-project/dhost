import { RouteComponentProps } from 'react-router-dom'
import { useTranslation } from 'react-i18next'
import './styles.scss'

type TParams = { slug: string }

function Files({ match }: RouteComponentProps<TParams>): React.ReactElement {
  const { t } = useTranslation()

  return (
    <div>
      <h2>
        {t('FILES_TITLE')} {match.params.slug}
      </h2>
    </div>
  )
}

export default Files
