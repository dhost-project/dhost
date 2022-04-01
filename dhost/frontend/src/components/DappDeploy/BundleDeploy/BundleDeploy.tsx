import { ChangeEvent, MouseEvent, useEffect, useState } from "react"
import { useTranslation } from "react-i18next"
import { useParams } from "react-router-dom"
import { createBundle, listBundles } from "api/Bundle"
import { Bundle } from "models/api/Bundle"
import { TParams } from "pages/Dapp"
import bundleLogo from "../../../assets/bundle.svg"
import uploadLogo from "../../../assets/upload.svg"
import { deployIPFSDapp } from "api/IPFSDapps"

export function BundleDeploy() {
  const { dapp_slug } = useParams<TParams>()
  const { t } = useTranslation()

  const [file, setFile] = useState<File>()
  const [currentBundle, setCurrentBundle] = useState<Bundle>()

  useEffect(() => {
    getBundle()
  }, [])

  async function getBundle() {
    const bundleList = (await listBundles(dapp_slug)).data
    if (bundleList.length > 0) setCurrentBundle(bundleList[0])
    console.log({ bundleList })
  }

  async function handleCreateBundle(e: MouseEvent) {
    if (!file) return
    console.log("handleCreateBundle", { file, currentBundle })
    const res = await createBundle(dapp_slug, file)
    console.log("res", res)
  }

  async function handleDeploy(e: MouseEvent) {
    // console.log("handleDeploy", { file, currentBundle })
    const res = await deployIPFSDapp(dapp_slug)
    console.log("res", res)
  }

  function handleFilesUpload(e: ChangeEvent<HTMLInputElement>) {
    if (!e?.target?.files) return
    setFile(e.target.files[0])
  }

  console.log({ currentBundle })

  return (
    <>
      <section className="grid-5-10 p-4 border-b-1 border-gray-200">
        <div className="pr-10">
          <h2 className="mb-2 font-normal text-green-500">
            {t("UPLOAD_FILES_TITLE")}
          </h2>
          <p className="text-xs">
            {/* Code diffs, manual and auto deploys are avaible for this app. */}
          </p>
        </div>

        <div className="relative flex flex-col">
          <div className="relative flex flex-col items-center w-full h-full p-4 border rounded border-gray-500 cursor-pointer">
            {currentBundle ? (
              <>
                <p>deployed bundle</p>
              </>
            ) : (
              <>
                {file ? (
                  <>
                    <span className="font-semibold">Current bundle : </span>
                    <div className="flex flex-col justify-center items-center my-4">
                      <img
                        className="h-20 w-20"
                        src={bundleLogo}
                        alt="Bundle logo"
                      />
                      <span className="text-bold text-green-500">
                        {file.name}
                      </span>
                    </div>
                    <span className="font-semibold">
                      You can choose an another bundle to deploy (.zip only)
                    </span>
                  </>
                ) : (
                  <>
                    <span className="font-semibold">
                      Choose your bundle to deploy (.zip only)
                    </span>
                    <img
                      className="h-20 w-20 my-4"
                      src={uploadLogo}
                      alt="Upload logo"
                    />
                    <span className="font-semibold">
                      Or drag and drop your bundle here
                    </span>
                  </>
                )}
              </>
            )}

            <input
              className="absolute left-0 top-0 h-full w-full opacity-0 focus:outline-none cursor-pointer"
              type="file"
              onChange={handleFilesUpload}
              multiple={false}
            />
          </div>
          <button
            className="flex justify-center items-center self-end h-8 btn btn-primary mt-4"
            onClick={handleCreateBundle}
          >
            Create Bundle
          </button>
          <button
            className="flex justify-center items-center self-end h-8 btn btn-primary mt-4"
            onClick={handleDeploy}
          >
            Deploy
          </button>
        </div>

        <div className="flex flex-col"></div>
      </section>
    </>
  )
}
