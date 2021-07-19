import { useTranslation } from 'react-i18next'
import './styles.scss'

function IPFSDapp(): React.ReactElement {
  const { t } = useTranslation()

  return (
    <div>
      <h2>{t('IPFS_DAPP_TITLE')}</h2>
    </div>
  )
}

export default IPFSDapp
