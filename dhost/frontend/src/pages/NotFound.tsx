import { useTranslation } from 'react-i18next'

function NotFound(): React.ReactElement {
  const { t } = useTranslation()

  return (
    <div>
      <h1>404</h1>
      <h2>{t('PAGE_NOT_FOUND')}</h2>
    </div>
  )
}

export default NotFound
