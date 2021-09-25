import { env } from "environment"

import { LoginForm } from "components/LoginForm"

export function Login(): React.ReactElement {
  const githublLoginUrl = `${env.API_URL}/api/social/login/github/`

  return (
    <div className="mx-auto w-96 border rounded-xl shadow-xl py-8 my-20">
      <h1 className="text-3xl mb-12 mt-2 text-center">Login</h1>
      <div className="px-8">
        <LoginForm />
        <hr className="my-6"></hr>
        <h2 className="block text-sm text-center font-medium text-gray-700">
          Or login with
        </h2>
        <a
          href={githublLoginUrl}
          className="px-4 py-2 mt-6 text-center rounded bg-gray-300 w-full hover:bg-gray-200 cursor-pointer focus:outline-none focus:ring-2 focus:ring-green-500"
          type="submit"
        >
          Github
        </a>
      </div>
    </div>
  )
}
