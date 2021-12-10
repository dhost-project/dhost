import { useTranslation } from "react-i18next"

export function HerokuDeploy() {
  const { t } = useTranslation()

  return (
    <>
      <section className="grid-5-10 p-4 border-b-1 border-gray-200">
        <div>
          <h2 className="font-normal text-green-500">{t("CONNECT_TO_GITHUB")}</h2>
        </div>
        <div className="flex">Heroku</div>
      </section>
    </>
  )
}
