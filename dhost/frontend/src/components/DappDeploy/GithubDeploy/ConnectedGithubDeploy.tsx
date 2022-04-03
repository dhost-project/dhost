import { Dispatch, SetStateAction, useEffect, useState } from "react"
import { useTranslation } from "react-i18next"
import { useParams } from "react-router-dom"
import {
  createGithubOptions,
  listGithubOptions,
  updateGithubOptions,
} from "api/GithubOptions"
import { fetchBranchesRepository, listRepositorys } from "api/Repositories"
import { useDapp } from "contexts/DappContext/DappContext"
import { useUserContext } from "contexts/UserContext/UserContext"
import { Repository } from "models/api/Repository"
import { TParams } from "pages/Dapp"

export function ConnectedGithubDeploy() {
  const { t } = useTranslation()
  const { userInfo, setUserInfo } = useUserContext()
  const { dapp_slug }: TParams = useParams()
  const { dapp, setDapp } = useDapp()

  const [currentRepoInfos, setCurrentRepoInfos] = useState<Repository>()
  const [selectedRepo, setSelectedRepo] = useState<number | undefined>()
  const [selectedBranch, setSelectedBranch] = useState<number | undefined>()

  useEffect(() => {
    console.log("ConnectedGithubDeploy", { dapp_slug, dapp, userInfo })

    listGithubOptions(dapp_slug).then((res) =>
      console.log("listGithubOptions", res)
    )
  }, [dapp])

  async function linkRepository() {
    if (!selectedRepo) return
    // TODO linkRepository
    console.log("linkRepository", { selectedRepo })

    const _hydratedCurrentRepository = (
      await fetchBranchesRepository(selectedRepo)
    ).data
    const _listRepositories = (await listRepositorys()).data

    setUserInfo((userInfo) => ({
      ...userInfo,
      githubRepositories: _listRepositories,
    }))

    setCurrentRepoInfos(_hydratedCurrentRepository)

    console.log("setDapp linkRepository")
    setDapp((dapp) => ({
      ...dapp,
      github: {
        ...dapp.github,
        repo: _hydratedCurrentRepository.github_repo,
      },
    }))
  }

  function linkBranch() {
    if (!selectedBranch) return

    // TODO linkBranch
    console.log("linkBranch", { selectedBranch })
    setDapp((dapp) => ({
      ...dapp,
      github: {
        ...dapp.github,
        branch: selectedBranch,
      },
    }))

    // TODO clarify branch (number) and how to get it
    updateGithubOptions(dapp_slug, {
      ...dapp.github,
      branch: selectedBranch,
    })
  }

  function getRepositoryBranches(repositoryName: string) {
    return userInfo.githubRepositories.find(
      (repository) => repository.github_repo === repositoryName
    )?.branches
  }

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

        <div className="flex flex-col">
          <div className="flex justify-between mb-4">
            <select
              onChange={(e) => setSelectedRepo(parseInt(e.target.value))}
              className="mr-2 border-1 border-gray-400 w-full p-1 rounded"
            >
              {userInfo.githubRepositories.map((repository) => (
                <option
                  key={repository.id}
                  value={repository.id}
                  selected={repository.github_repo === dapp.github.repo}
                >
                  📥 {repository.github_repo}
                </option>
              ))}
            </select>
            <button
              className="w-40 text-medium border-1 border-gray-700 text-gray-700 hover:bg-gray-700 rounded hover:text-white"
              onClick={linkRepository}
            >
              Connect Repository
            </button>
          </div>
          {dapp.github.repo && dapp.github.branch ? (
            <GithubBranchLinked />
          ) : (
            <div className="flex justify-between">
              {getRepositoryBranches(dapp.github.repo)?.length ? (
                <>
                  <select className="mr-2 border-1 border-gray-400 w-full p-1 rounded">
                    {getRepositoryBranches(dapp.github.repo)?.map(
                      (branch, i) => (
                        <option
                          key={`github-deploy-${branch.name}-${i}`}
                          value={branch.id}
                        >
                          🖇 {branch.name}
                        </option>
                      )
                    )}
                  </select>
                  <button className="w-40 text-medium border-1 border-gray-700 text-gray-700 hover:bg-gray-700 rounded hover:text-white">
                    Connect Branch
                  </button>
                </>
              ) : (
                <div>
                  <p>No branches found or repository not yet connected</p>
                </div>
              )}
            </div>
          )}
        </div>

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

        {dapp.github.auto_deploy ? (
          <div className="flex flex-col">
            <div className="mb-3 pl-4 pr-4 pt-2 pb-2 bg-blue-100 border-1 border-blue-300 rounded-sm text-blue-500 font-medium">
              <p className="text-sm">
                You can now change your main deploy branch from "master" to
                "main" for both automatic and manual deploys, please follow the
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
              <span className="font-medium">
                Deploys happen automatically:{" "}
              </span>
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
        ) : (
          <div>Enable auto deploy</div>
        )}
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

export function GithubBranchLinked() {
  function disconnect() {
    // TODO
    console.log("TODO disconnect")
  }

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
          onClick={disconnect}
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
