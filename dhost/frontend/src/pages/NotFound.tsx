import { useTranslation } from "react-i18next"

export default function NotFound(): React.ReactElement {
  const { t } = jest ? {t:(s: any)=>s} : useTranslation()

  const style404 = {
    fontSize: "10rem",
  }

  return (
    <div className="container mx-auto">
      <div className="text-center">
        <h1 style={style404}>404</h1>
        <h2 className="text-5xl">{t("Page not found.")}</h2>
      </div>
    </div>
  )
}
