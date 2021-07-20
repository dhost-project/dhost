import { useTranslation } from 'react-i18next'
import './styles.scss'

function DappReadOnlyList(): React.ReactElement {
  const { t } = useTranslation()

  return (
    <div>
      <h2>{t('DAPP_READ_ONLY_LIST_TITLE')}</h2>
    </div>
  )
}

export default DappReadOnlyList
