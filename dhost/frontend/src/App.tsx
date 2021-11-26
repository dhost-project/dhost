import { BrowserRouter } from "react-router-dom"
import { toast, ToastContainer } from "react-toastify"
import "react-toastify/dist/ReactToastify.min.css"
import { Footer } from "components/Footer"
import { Header } from "components/Header"
import { Navbar } from "components/Navbar"
import { RouterOutlet } from "./Router"

export default function App(): React.ReactElement {
  // Toast Container default classes
  const contextClass = {
    success: "bg-green-400",
    error: "bg-red-400",
    info: "bg-blue-400",
    warning: "bg-yellow-400",
    default: "bg-indigo-600",
    dark: "bg-white-600 font-gray-300",
  }

  return (
    <BrowserRouter>
      <div className="flex flex-col min-h-screen justify-between">
        <div>
          <Header />
          <Navbar />
          <RouterOutlet />
          <ToastContainer
            position={toast.POSITION.BOTTOM_RIGHT}
            autoClose={5000}
            icon={false}
            toastClassName={(options) =>
              contextClass[options?.type || "default"] +
              " relative flex p-1 m-2 min-h-10 rounded-md justify-between overflow-hidden cursor-pointer"
            }
          />
        </div>
        <Footer />
      </div>
    </BrowserRouter>
  )
}
