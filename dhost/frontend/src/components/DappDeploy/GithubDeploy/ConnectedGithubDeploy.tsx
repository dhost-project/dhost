import { Dispatch, SetStateAction, useEffect, useState } from "react"
import { useTranslation } from "react-i18next"
import { useParams } from "react-router-dom"
import { toast } from "react-toastify"
import {
  createGithubOptions,
  destroyGithubOptions,
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
  const { dapp_slug } = useParams<TParams>()
  const { dapp, setDapp } = useDapp()
  const { userInfo, setUserInfo } = useUserContext()

  const [selectedRepo, setSelectedRepo] = useState<number>()
  const [selectedBranch, setSelectedBranch] = useState<number>()

  useEffect(() => {
    // console.log("ConnectedGithubDeploy", { dapp_slug, dapp, userInfo })
    getListGithubOptions()
  }, [])

  async function getRepositoriesList() {
    const _listRepositories = (await listRepositorys()).data

    setUserInfo((userInfo) => ({
      ...userInfo,
      githubRepositories: _listRepositories,
    }))
  }

  async function getListGithubOptions() {
    try {
      const githubOptionsList = (await listGithubOptions(dapp_slug)).data
      if (!githubOptionsList.length) return

      // console.log("githubOptionsList", githubOptionsList)
      const githubOption = githubOptionsList[githubOptionsList.length - 1]
      setDapp((_dapp) => ({
        ..._dapp,
        github: githubOption,
      }))
    } catch (e) {
      // console.error("getListGithubOptions", e)
      toast.warn("Error while getting github options")
    }
  }

  async function linkRepository() {
    if (!selectedRepo) return
    // console.log("linkRepository", { selectedRepo })

    const _hydratedCurrentRepository = (
      await fetchBranchesRepository(selectedRepo)
    ).data

    getRepositoriesList() // To refresh repos with fetched branches

    setDapp((dapp) => ({
      ...dapp,
      github: {
        repo: `${_hydratedCurrentRepository.id}`,
        branch: 0,
        auto_deploy: false,
        confirm_ci: false,
      },
    }))
  }

  async function linkBranch() {
    if (!selectedBranch) {
      // console.log("selectedBranch", selectedBranch)
      toast.warn("Please select a branch")
      return
    }
    if (!dapp.github.repo) {
      // console.log("dapp.github.repo", dapp.github.repo)
      toast.warn(
        "Missing repository information, please reload and/or try again later"
      )
      return
    }

    const githubOptionsList = (await listGithubOptions(dapp_slug)).data
    // console.log("linkBranch", { selectedBranch, githubOptionsList })

    try {
      if (githubOptionsList.length) {
        if (
          githubOptionsList.some(
            (githubOptions) =>
              githubOptions.repo == dapp.github.repo &&
              githubOptions.branch == selectedBranch
          )
        ) {
          const updatedGithubOptions = await updateGithubOptions(
            dapp_slug,
            dapp.github.repo,
            // `${selectedBranch}`,
            {
              ...dapp.github,
              repo: dapp.github.repo,
              branch: selectedBranch,
            }
          )

          // console.log("updatedGithubOptions", updatedGithubOptions)

          setDapp((_dapp) => ({
            ..._dapp,
            github: updatedGithubOptions.data,
          }))
          return
        }
      }
      const createdGithubOptions = await createGithubOptions(
        dapp_slug,
        dapp.github.repo,
        // `${selectedBranch}`,
        {
          ...dapp.github,
          repo: dapp.github.repo,
          branch: selectedBranch,
        }
      )

      // console.log("createdGithubOptions", createdGithubOptions)

      setDapp((_dapp) => ({
        ..._dapp,
        github: createdGithubOptions.data,
      }))
    } catch (e) {
      console.warn(e)
      toast.error("Unable to set your github options")
    }
  }

  function getRepositoryBranches(repositoryId: string) {
    return userInfo.githubRepositories.find(
      (repository) => `${repository.id}` == repositoryId
    )?.branches
  }

  function getRepository(repositoryId: string) {
    return userInfo.githubRepositories.find(
      (repository) => `${repository.id}` == repositoryId
    )
    // console.log("getRepository", repo)
    // return repo
  }

  function setAutoDeploy(value: boolean) {
    setDapp((_dapp) => ({
      ..._dapp,
      github: {
        ..._dapp.github,
        auto_deploy: value,
      },
    }))
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
                  selected={`${repository.id}` == dapp.github.repo}
                >
                  📥 {repository.github_repo}
                </option>
              ))}
            </select>
            <button
              className="flex justify-center items-center btn border border-green-500 h-8 ml-2 text-green-500 bg-white p-4"
              onClick={linkRepository}
            >
              Connect Repository
            </button>
          </div>
          {dapp.github.repo && dapp.github.branch ? (
            <GithubBranchLinked repository={getRepository(dapp.github.repo)} />
          ) : (
            <div className="flex justify-between">
              {getRepositoryBranches(dapp.github.repo)?.length ? (
                <>
                  <select
                    onChange={(e) => {
                      console.log("branch", e.target.value)
                      setSelectedBranch(parseInt(e.target.value))
                    }}
                    className="mr-2 border-1 border-gray-400 w-full p-1 rounded"
                  >
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
                  <button
                    onClick={linkBranch}
                    className="flex justify-center items-center btn border border-green-500 h-8 ml-2 text-green-500 bg-white p-4"
                  >
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
              <button
                onClick={() => setAutoDeploy(false)}
                className="pl-4 pr-4 pt-1 pb-1 font-medium text-sm text-gray-500 border-1 border-gray-500 rounded hover:bg-gray-500 hover:text-white"
              >
                Disable Automatic Deploy
              </button>
            </div>
          </div>
        ) : (
          <div>
            <button
              onClick={() => setAutoDeploy(true)}
              className="pl-4 pr-4 pt-1 pb-1 font-medium text-sm text-green-500 border-1 border-green-500 rounded hover:bg-green-500 hover:text-white"
            >
              Enable Automatic Deploy
            </button>
          </div>
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
            {getRepositoryBranches(dapp.github.repo)?.length ? (
              <>
                <select
                  onChange={(e) => {
                    console.log("branch", e.target.value)
                    setSelectedBranch(parseInt(e.target.value))
                  }}
                  className="mr-2 border-1 border-gray-400 w-full p-1 rounded"
                >
                  {getRepositoryBranches(dapp.github.repo)?.map((branch, i) => (
                    <option
                      key={`github-deploy-${branch.name}-${i}`}
                      value={branch.id}
                    >
                      🖇 {branch.name}
                    </option>
                  ))}
                </select>
                <button
                  onClick={linkBranch}
                  className="flex justify-center items-center btn border border-green-500 h-8 ml-2 text-green-500 bg-white p-4"
                >
                  Deploy Branch
                </button>
              </>
            ) : (
              <div>
                <p>No branches found or repository not yet connected</p>
              </div>
            )}
          </div>
        </div>
      </section>
    </>
  )
}

export function GithubBranchLinked({
  repository,
}: {
  repository: Repository | undefined
}) {
  const { dapp_slug } = useParams<TParams>()
  const { dapp, setDapp } = useDapp()

  async function disconnect() {
    const res = await destroyGithubOptions(dapp_slug, dapp_slug)
    setDapp((_dapp) => ({
      ..._dapp,
      github: {
        repo: "",
        branch: 0,
        auto_deploy: false,
        confirm_ci: false,
      },
    }))
  }

  function getCurrentBranch() {
    return repository?.branches.find(
      (branch) => branch.id === dapp.github.branch
    )
  }

  return (
    <div className="border-1 border-gray-300 rounded shadow-sm overflow-hidden">
      <header className="flex justify-between p-2 border-b-1 border-gray-300">
        <p className="text-sm">
          Connected to
          <a
            href={`https://github.com/${repository?.github_owner}/${repository?.github_repo}`}
            className="pl-1 pr-1 text-blue-500 hover:text-blue-400"
          >
            <span className="pr-1 no-underline">📘 </span>
            {/* <span className="underline">project-name/repo-name</span> */}
            <span className="underline">
              {repository?.github_repo}/{getCurrentBranch()?.name}
            </span>
          </a>
          by
          <a
            href={`https://github.com/${repository?.github_owner}/${repository?.github_repo}`}
            className="pl-1 pr-1 text-blue-500 hover:text-blue-400"
          >
            <span className="pr-1 no-underline">🧙‍♂️ </span>
            {/* <span className="underline">username</span> */}
            <span className="underline">{repository?.github_owner}</span>
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
          <a
            href={`https://github.com/${repository?.github_owner}/${repository?.github_repo}`}
            className="text-blue-500 underline"
          >
            activity feed
          </a>{" "}
          link to Github to view commit diffs
        </p>
        {dapp.github.auto_deploy && (
          <p className="pb-1 text-sm">
            <span className="pr-2">🥨</span>
            Automatically deploy from
            <span className="ml-1 mr-1 pl-1 pr-1 bg-gray-100 border-1 border-gray-400 rounded-sm">
              🖇 {getCurrentBranch()?.name}
            </span>
          </p>
        )}
      </div>
    </div>
  )
}
