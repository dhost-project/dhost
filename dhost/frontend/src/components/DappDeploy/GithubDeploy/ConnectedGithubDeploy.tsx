import { Dispatch, SetStateAction, useState } from "react"
import { useTranslation } from "react-i18next"

export function GithubBranchLinked({
  setIsConnected,
}: {
  setIsConnected: Dispatch<SetStateAction<boolean>>
}) {
  return (
    <div className="border-1 border-gray-300 rounded shadow-sm overflow-hidden">
      <header className="flex justify-between p-2 border-b-1 border-gray-300">
        <p className="text-sm">
          Connected to
          <a
            href="https://github.com"
            className="pl-1 pr-1 text-blue-500 hover:text-blue-400"
          >
            <span className="pr-1 no-underline">📘 </span>
            <span className="underline">project-name/repo-name</span>
          </a>
          by
          <a
            href="https://github.com"
            className="pl-1 pr-1 text-blue-500 hover:text-blue-400"
          >
            <span className="pr-1 no-underline">🧙‍♂️ </span>
            <span className="underline">username</span>
          </a>
        </p>

        <button
          onClick={() => setIsConnected(false)}
          className="pl-2 pr-2 text-sm font-medium text-red-500 border-1 border-red-500 rounded-sm hover:bg-red-500 hover:text-white"
        >
          Disconnect...
        </button>
      </header>
      <div className="flex flex-col p-2 bg-gray-100">
        <p className="pb-1 text-sm">
          <span className="pr-2">➰</span>
          Release in the{" "}
          <a href="https://github.com" className="text-blue-500 underline">
            activity feed
          </a>{" "}
          link to Github to view commit diffs
        </p>
        <p className="pb-1 text-sm">
          <span className="pr-2">🥨</span>
          Automatically deploy from
          <span className="ml-1 mr-1 pl-1 pr-1 bg-gray-100 border-1 border-gray-400 rounded-sm">
            🖇 dev
          </span>
        </p>
      </div>
    </div>
  )
}

export function ConnectedGithubDeploy({
  setIsConnected,
}: {
  setIsConnected: Dispatch<SetStateAction<boolean>>
}) {
  const { t } = useTranslation()
  const [isBranchLinked, setIsBranchLinked] = useState(false)

  return (
    <>
      <section className="grid-5-10 p-4 border-b-1 border-gray-200">
        <div className="pr-10">
          <h2 className="mb-2 font-normal text-green-500">
            {t("DEPLOY_APP_CONNECTED")}
          </h2>
          <p className="text-xs">
            Code diffs, manual and auto deploys are avaible for this app.
          </p>
        </div>

        {isBranchLinked ? (
          <GithubBranchLinked setIsConnected={setIsConnected} />
        ) : (
          <div className="flex justify-between">
            <select className="mr-2 border-1 border-gray-400 w-full p-1 rounded">
              <option value="master">🖇 master</option>
              <option value="main">🖇 main</option>
              <option value="dev">🖇 dev</option>
              <option value="feature">🖇 feature</option>
            </select>
            <button className="w-40 text-medium border-1 border-gray-700 text-gray-700 hover:bg-gray-700 rounded hover:text-white">
              Deploy Branch
            </button>
          </div>
        )}

        <div className="flex flex-col"></div>
      </section>

      <section className="grid-5-10 p-4 border-b-1 border-gray-200">
        <div className="pr-10">
          <h2 className="mb-2 font-normal text-green-500">
            {t("DEPLOY_AUTO")}
          </h2>
          <p className="text-xs">
            Enable a chosen branch to be automatically deployed to this Dapp.
          </p>
        </div>

        <div className="flex flex-col">
          <div className="mb-3 pl-4 pr-4 pt-2 pb-2 bg-blue-100 border-1 border-blue-300 rounded-sm text-blue-500 font-medium">
            <p className="text-sm">
              You can now change your main deploy branch from "master" to "main"
              for both automatic and manual deploys, please follow the
              instruction{" "}
              <a href="https://github.com" className="underline">
                here
              </a>
              .
            </p>
          </div>

          <p className="text-sm mb-3">
            ✅ Automatic deploys from
            <span className="ml-1 mr-1 pl-1 pr-1  bg-gray-100 border-1 border-gray-400 rounded-sm">
              🖇 dev
            </span>
            are enabled
          </p>

          <p className="text-sm mb-3 text-gray-500">
            Every push to
            <span className="ml-1 mr-1 pl-1 pr-1 bg-gray-100 border-1 border-gray-400 rounded-sm">
              dev
            </span>
            will deploy a new version of this app.{" "}
            <span className="font-medium">Deploys happen automatically: </span>
            be sure that this branch in Github is always in a deployable state
            and any tests having been passed before you push.{" "}
            <a href="https://github.com" className="text-blue-500 underline">
              Learn more.
            </a>
          </p>

          <label
            htmlFor="waitForDeploy"
            className="flex mb-2 items-center text-sm"
          >
            <input id="waitForDeploy" type="checkbox" className="mr-1" />
            Wait for CI to pass before deploy
          </label>

          <p className="text-sm mb-3 text-gray-500">
            Only enable this option if you have CI service on your repo.
          </p>

          <div>
            <button className="pl-4 pr-4 pt-1 pb-1 font-medium text-sm text-gray-500 border-1 border-gray-500 rounded hover:bg-gray-500 hover:text-white">
              Disable Automatic Deploy
            </button>
          </div>
        </div>
      </section>

      <section className="grid-5-10 p-4 border-b-1 border-gray-200">
        <div className="pr-10">
          <h2 className="mb-2 font-normal text-green-500">
            {t("DEPLOY_MANUAL_ONE")}
          </h2>
          <p className="text-xs">
            Deploy the current state of a branch to this app.
          </p>
        </div>

        <div className="flex flex-col text-sm">
          <h4 className="font-medium mb-2 text-gray-500">
            Deploy a Github branch
          </h4>
          <p className="mb-2 text-gray-400">
            This will deploy the current state of the branch you specify below.{" "}
            <a href="https://github.com" className="text-blue-500 underline">
              Learn more
            </a>
          </p>
          <h4 className="font-medium mb-2 text-gray-500">
            Choose a branch to deploy
          </h4>
          <div className="flex justify-between">
            <select className="mr-2 border-1 border-gray-400 w-full p-1 rounded">
              <option value="master">🖇 master</option>
              <option value="main">🖇 main</option>
              <option value="dev">🖇 dev</option>
              <option value="feature">🖇 feature</option>
            </select>
            <button className="w-40 text-medium border-1 border-gray-700 text-gray-700 hover:bg-gray-700 rounded hover:text-white">
              Deploy Branch
            </button>
          </div>
        </div>
      </section>
    </>
  )
}
