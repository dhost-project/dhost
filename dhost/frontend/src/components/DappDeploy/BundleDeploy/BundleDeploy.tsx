import { ChangeEvent, MouseEvent, useEffect, useState } from "react"
import { useTranslation } from "react-i18next"
import { useParams } from "react-router-dom"
import { toast } from "react-toastify"
import { createBundle, listBundles } from "api/Bundle"
import { deployIPFSDapp } from "api/IPFSDapps"
import { Bundle } from "models/api/Bundle"
import { TParams } from "pages/Dapp"
import bundleLogo from "../../../assets/bundle.svg"
import uploadLogo from "../../../assets/upload.svg"

export function BundleDeploy() {
  const { dapp_slug } = useParams<TParams>()
  const { t } = useTranslation()

  const [file, setFile] = useState<File>()
  const [currentUploadedBundle, setCurrentUploadedBundle] = useState<Bundle>()

  useEffect(() => {
    getBundle()
  }, [])

  async function getBundle() {
    try {
      const bundleList = (await listBundles(dapp_slug)).data
      if (bundleList.length > 0)
        setCurrentUploadedBundle(bundleList[bundleList.length - 1])
    } catch (e) {
      console.error("getBundle", e)
      toast.warn("Unable to retrieve current bundle list.")
    }
  }

  async function handleUploadBundle(e: MouseEvent) {
    if (!file) return
    try {
      const createdBundles = (await createBundle(dapp_slug, file)).data
      setCurrentUploadedBundle(createdBundles)
      setFile(undefined)
      toast.success("Bundle uploaded.")
    } catch (e) {
      console.error("handleUploadBundle", e)
      toast.warn("Something went wrong during dapp bundle upload.")
    }
  }

  async function handleDeploy(e: MouseEvent) {
    try {
      await deployIPFSDapp(dapp_slug)
      toast.success("Bundle deployment started, it can takes few minutes.")
    } catch (e) {
      console.error("handleDeploy", e)
      toast.warn("Something went wrong during dapp bundle deployment.")
    }
  }

  function handleFilesUpload(e: ChangeEvent<HTMLInputElement>) {
    if (!e?.target?.files) return
    setFile(e.target.files[0])
  }

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
            {currentUploadedBundle ? (
              <>
                <span className="font-semibold">
                  Current uploaded bundle :{" "}
                </span>
                <div className="flex w-full justify-center items-center my-4">
                  {file && (
                    <>
                      <div className="flex flex-col justify-center items-center">
                        <img
                          className="h-20 w-20"
                          src={bundleLogo}
                          alt="Bundle logo"
                        />
                        <span className="text-bold text-green-500">
                          {file.name}
                        </span>
                        <span>(local)</span>
                      </div>
                      <span className="mx-8">{"👉"}</span>
                    </>
                  )}
                  <div className="flex flex-col justify-center items-center">
                    <img
                      className="h-20 w-20"
                      src={bundleLogo}
                      alt="Bundle logo"
                    />
                    <span className="text-bold text-green-500">
                      {currentUploadedBundle.dapp}
                    </span>
                    {file && <span>(remote)</span>}
                  </div>
                </div>
                <span>
                  You can choose an another bundle to deploy (.zip only)
                </span>
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
          <div className="flex justify-end mt-4">
            <button
              className={
                "flex justify-center items-center h-8 btn ml-2 text-white " +
                (!file ? "bg-gray-500 text-gray-300" : "bg-green-500")
              }
              onClick={handleUploadBundle}
              disabled={!file}
            >
              Upload Bundle
              {currentUploadedBundle && file && " (local)"}
            </button>
            <button
              className={
                "flex justify-center items-center h-8 btn ml-2 text-white " +
                (!currentUploadedBundle
                  ? "bg-gray-500 text-gray-300"
                  : "bg-green-500")
              }
              onClick={handleDeploy}
              disabled={!currentUploadedBundle}
            >
              Deploy Bundle
              {currentUploadedBundle && file && " (remote)"}
            </button>
          </div>
        </div>

        <div className="flex flex-col"></div>
      </section>
    </>
  )
}
