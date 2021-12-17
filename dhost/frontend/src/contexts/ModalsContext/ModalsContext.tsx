import {
  createContext,
  Dispatch,
  FC,
  SetStateAction,
  useContext,
  useState,
} from "react"
import { DappCreateModal } from "components/Modals"

interface ModalsContextType {
  showCreateDappModal: boolean
  setShowCreateDappModal: Dispatch<SetStateAction<boolean>>
}

export const ModalsContext = createContext({})

export const ModalsProvider: FC = ({ children }) => {
  const [showCreateDappModal, setShowCreateDappModal] = useState(false)

  return (
    <ModalsContext.Provider
      value={{ showCreateDappModal, setShowCreateDappModal }}
    >
      {children}
      {showCreateDappModal && <DappCreateModal />}
    </ModalsContext.Provider>
  )
}

export const useModals = () => useContext(ModalsContext) as ModalsContextType
