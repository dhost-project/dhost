import { ChangeEvent, useState } from "react"
import { useTranslation } from "react-i18next"
import uploadLogo from "../../../assets/upload.svg"
import bundleLogo from "../../../assets/bundle.svg"

export function BundleDeploy() {
  const { t } = useTranslation()
  const [file, setFile] = useState<File | null>(null)

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

        <div className="flex">
          <div className="relative flex flex-col items-center w-full h-full p-4 border rounded border-gray-500 cursor-pointer">
            {file ? (
              <>
                <span className="font-semibold">
                  Current bundle :{" "}
                </span>
                <div className="flex flex-col justify-center items-center my-4">
                  <img className="h-20 w-20" src={bundleLogo} alt="Bundle logo" />
                  <span className="text-bold text-green-500">{file.name}</span>
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
                <img className="h-20 w-20 my-4" src={uploadLogo} alt="Upload logo" />
                <span className="font-semibold">
                  Or drag and drop your bundle here
                </span>
              </>
            )}

            <input
              className="absolute left-0 top-0 h-full w-full opacity-0 focus:outline-none cursor-pointer"
              type="file"
              onChange={handleFilesUpload}
              multiple={false}
            />
          </div>
        </div>

        <div className="flex flex-col"></div>
      </section>
    </>
  )
}
