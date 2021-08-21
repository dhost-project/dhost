import { LoginForm } from "components/LoginForm"

export function Login(): React.ReactElement {
  return (
    <div className="mx-auto w-96 border rounded-xl shadow-xl py-8 my-20">
      <h1 className="text-3xl mb-12 mt-2 text-center">Login</h1>
      <div className="px-8">
        <LoginForm />
      </div>
    </div>
  )
}
