import { listBundles, retrieveBundle } from "api/Bundle"
import { retrieveIPFSDapp } from "api/IPFSDapps"
import { useDapp } from "contexts/DappContext/DappContext"
import { useEffect, useState } from "react"
import { useTranslation } from "react-i18next"
import { RouteComponentProps } from "react-router-dom"
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.min.js";
import FileTree from "react-file-treeview";

type TParams = { dapp_slug: string }

export function DappSource({
  match,
}: RouteComponentProps<TParams>): React.ReactElement {
  const { t } = useTranslation()
  const { dapp } = useDapp()
  const [treeview, setTreeView] = useState<Object>()



  const fetchData = async () => {
    try {
      let res = await listBundles(dapp.basic.slug)
      let _res = await retrieveBundle(dapp.basic.slug, res.data[res.data.length - 1].id)
      if (_res.data.folder_tree) {
        setTreeView(JSON.parse(_res.data.folder_tree.replaceAll("'", "\"").replaceAll("True", "true").replaceAll("False", "false")))
      }
    }
    catch (error) {
      console.log(error)
    }
  }

  useEffect(() => {
    fetchData()
  }, [])

  //create Collapse button data
  const [collapseAll, setCollapseAll] = useState(false);
  const handleCollapseAll = (value: boolean | ((prevState: boolean) => boolean)) => setCollapseAll(value);

  //Create file action data*
  const handleFileOnClick = (file: any) => {
    console.log(file);
  };

  const action = {
    fileOnClick: handleFileOnClick,
  };

  //Create Decoration data*
  const treeDecorator = {
    showIcon: true,
    iconSize: 18,
    textSize: 15,
    showCollapseAll: true,
  };

  return (
    <div className="container mx-auto">
      <div className="border-2 border-grey-500 rounded overflow-y-auto m-4 p-4 max-h-[calc(100vh-310px)]">
        <button onClick={() => setCollapseAll(true)}>Collapse All</button>
        {treeview && <FileTree
          data={treeview}
          action={action} //optional
          collapseAll={{ collapseAll, handleCollapseAll }} //Optional
          decorator={treeDecorator} //Optional
        />}
      </div>
    </div>
  )
}
