import { FormEvent, useState } from "react"
import { Form } from "react-bootstrap"
import { useHistory } from "react-router-dom"
import { createIPFSDapp, retrieveIPFSDapp } from "api/IPFSDapps"
import { Button } from "components/Button"
import { IPFSDappParams } from "models/api/IPFSDapp"
import { useModals } from "contexts/ModalsContext/ModalsContext";
import { createBuildOptions } from "api/BuildOptions"
import { toast } from "react-toastify"
import { useUserContext } from "contexts/UserContext/UserContext"
import { Dapp } from "models/api/Dapp"
import { retrieveDapp } from "api/Dapps"

const initialDapp: IPFSDappParams = {
  slug: "",
  ipfs_gateway: "https://ipfs.io/ipfs/",
}

export function DappCreateForm() {
  const history = useHistory()
  const { setShowCreateDappModal } = useModals()
  const [dappForm, setDappForm] = useState<IPFSDappParams>({ ...initialDapp })
  const { userInfo, setUserInfo } = useUserContext()

  async function handleSubmit(e: FormEvent) {
    e.preventDefault()
    try {
      const res = await createIPFSDapp(dappForm)
      console.log("dappCreated", res)
      await createBuildOptions(dappForm.slug, { command: "", docker: "" })
      // let _res = (await retrieveDapp(dappForm.slug)).data
      // let _dapps = userInfo.dapps
      // _dapps.push(_res)
      // let _userInfo = userInfo
      // _userInfo.dapps = _dapps
      // setUserInfo({ ..._userInfo })
      history.push(`/dapps/${res.data.slug}/deploy`)
      setShowCreateDappModal(false)
      window.location.reload()
      toast.success("Dapp created")
    } catch (error) {
      console.warn(error)
    }
  }

  return (
    <Form
      onSubmit={handleSubmit}
      onClick={(e) => e.stopPropagation()}
      className="bg-white p-4 rounded shadow"
    >
      <Form.Group className="mb-3" controlId="formBasicEmail">
        <Form.Label>Dapp Slug</Form.Label>
        <Form.Control
          type="text"
          placeholder="Enter a Dapp slug"
          value={dappForm.slug}
          onChange={(e) => setDappForm({ ...dappForm, slug: e.target.value })}
        />
      </Form.Group>

      <Form.Group className="mb-3" controlId="formBasicEmail">
        <Form.Label>Select IPFS gateway</Form.Label>
        <Form.Select
          placeholder="Enter a URL"
          value={dappForm.ipfs_gateway}
          onChange={(e) =>
            setDappForm({ ...dappForm, ipfs_gateway: e.target.value })
          }
        >
          <option value="https://ipfs.io/ipfs/">https://ipfs.io/ipfs/</option>
          <option value="https://gateway.ipfs.io/ipfs/">https://gateway.ipfs.io/ipfs/</option>

        </Form.Select>
      </Form.Group>

      <Button type="submit">Submit</Button>
    </Form>
  )
}
