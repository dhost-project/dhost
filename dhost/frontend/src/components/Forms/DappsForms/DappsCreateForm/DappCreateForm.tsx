import { FormEvent, useState } from "react"
import { Form } from "react-bootstrap"
import { useHistory } from "react-router-dom"
import { createIPFSDapp } from "api/IPFSDapps"
import { Button } from "components/Button"
import { IPFSDappParams } from "models/api/IPFSDapp"
import { useModals } from "contexts/ModalsContext/ModalsContext";

const initialDapp: IPFSDappParams = {
  slug: "",
  ipfs_gateway: "",
}

export function DappCreateForm() {
  const history = useHistory()
  const { setShowCreateDappModal } = useModals()
  const [dappForm, setDappForm] = useState<IPFSDappParams>({ ...initialDapp })

  async function handleSubmit(e: FormEvent) {
    e.preventDefault()
    try {
      const res = await createIPFSDapp(dappForm)
      history.push(`/ipfs/${res.data.slug}/deploy`)
      setShowCreateDappModal(false)
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
        <Form.Label>Dapp URL</Form.Label>
        <Form.Control
          type="text"
          placeholder="Enter a URL"
          value={dappForm.ipfs_gateway}
          onChange={(e) =>
            setDappForm({ ...dappForm, ipfs_gateway: e.target.value })
          }
        />
      </Form.Group>

      <Button type="submit">Submit</Button>
    </Form>
  )
}
