import {
  createContext,
  Dispatch,
  FC,
  SetStateAction,
  useContext,
  useState,
} from "react"
import { DappCreateModal, DappDestroyModal } from "components/Modals"

interface ModalsContextType {
  showCreateDappModal: boolean
  setShowCreateDappModal: Dispatch<SetStateAction<boolean>>
  showDestroyDappModal: boolean
  setShowDestroyDappModal: Dispatch<SetStateAction<boolean>>
}

export const ModalsContext = createContext({})

export const ModalsProvider: FC = ({ children }) => {
  const [showCreateDappModal, setShowCreateDappModal] = useState(false)
  const [showDestroyDappModal, setShowDestroyDappModal] = useState(false)

  return (
    <ModalsContext.Provider
      value={{
        showCreateDappModal, setShowCreateDappModal,
        showDestroyDappModal, setShowDestroyDappModal
      }}
    >
      {children}
      {showCreateDappModal && <DappCreateModal />}
      {showDestroyDappModal && <DappDestroyModal />}
    </ModalsContext.Provider>
  )
}

export const useModals = () => useContext(ModalsContext) as ModalsContextType
