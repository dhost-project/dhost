import { FormEvent, useState } from "react"
import { Form } from "react-bootstrap"
import { useHistory } from "react-router-dom"
import { destroyIPFSDapp } from "api/IPFSDapps"
import { Button } from "components/Button"
import { useModals } from "contexts/ModalsContext/ModalsContext"
import { DappDestroyParams } from "models/api/DappDestroyParams"
import { useUserContext } from "contexts/UserContext/UserContext"

const initialDapp: DappDestroyParams = {
    slug: ""
}

export function DappDestroyForm() {
    const history = useHistory()
    const { setShowDestroyDappModal } = useModals()
    const [dappForm, setDappForm] = useState<DappDestroyParams>({ ...initialDapp })
    const { userInfo, setUserInfo } = useUserContext()

    async function handleSubmit(e: FormEvent) {
        e.preventDefault()
        try {
            const res = await destroyIPFSDapp(dappForm.slug)
            history.push(`/`)
            setShowDestroyDappModal(false)
            window.location.reload()
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
                <Form.Label>Type the Dapp Slug</Form.Label>
                <Form.Control
                    type="text"
                    placeholder="Enter the Dapp slug"
                    value={dappForm.slug}
                    onChange={(e) => setDappForm({ ...dappForm, slug: e.target.value })}
                />
            </Form.Group>
            <Button type="submit">Destroy</Button>
        </Form>
    )
}
