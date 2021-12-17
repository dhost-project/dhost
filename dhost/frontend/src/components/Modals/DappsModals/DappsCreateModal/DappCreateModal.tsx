import { DappCreateForm } from "components/Forms/DappsForms"
import { useModals } from "contexts/ModalsContext/ModalsContext"

export function DappCreateModal() {
  const { setShowCreateDappModal } = useModals()

  return (
    <div
      className="absolute z-50 top-0 left-0 w-full h-full flex justify-center items-center bg-gray-800 bg-opacity-50"
      onClick={() => setShowCreateDappModal(false)}
    >
      <DappCreateForm />
    </div>
  )
}
