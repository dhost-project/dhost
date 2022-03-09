import { env } from "environment"
import { useTranslation } from "react-i18next"

export function NotConnectedGithubDeploy() {
  const { t } = useTranslation()

  async function handleConnectToGithub() {
    console.log("handleConnectToGithub")
    window.open(`${env.API_URL}/api/social/login/github/`)
  }

  return (
    <>
      <section className="grid-5-10 p-4 border-b-1 border-gray-200">
        <div className="pr-10">
          <h2 className="mb-2 font-normal text-green-500">
            {t("CONNECT_TO_GITHUB")}
          </h2>
          <p className="text-xs">
            Connect this Dapp to GitHub to enable code diffs and deploys.
          </p>
        </div>
        <div className="flex flex-col">
          <p className="mb-3 text-sm">View your code diffs on GitHub</p>
          <p className="mb-3 text-sm">
            Connect your app to a GitHub repository to see commit diffs in the
            activity log.
          </p>
          <p className="mb-3 text-sm">Deploy changes with GitHub</p>
          <p className="mb-3 text-sm">
            Connecting to a repository will allow you to deploy a branch to your
            app.
          </p>
          <p className="mb-3 text-sm">Automatic deploys from GitHub</p>
          <p className="mb-3 text-sm">
            Select a branch to deploy automatically whenever it is pushed to.
          </p>

          <button
            className="bg-green-500 w-44 p-1 pt-2 pb-2 text-white rounded hover:bg-green-400"
            onClick={handleConnectToGithub}
          >
            Connect to Github
          </button>
        </div>
      </section>
    </>
  )
}
