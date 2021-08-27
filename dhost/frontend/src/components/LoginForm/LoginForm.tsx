<<<<<<< HEAD
import axios from "axios"
import { env } from "environment"
import { useState } from "react"
=======
import { useState } from "react"
import { env } from "environment";
import { http } from "utils/http";
>>>>>>> 17629ff (add custom axios instance to inject csrf token & interceptor for futur uses (#149))

export function LoginForm() {
  const [loginForm, setLoginForm] = useState({
    username: "",
    password: "",
  })

  async function login(event: React.FormEvent) {
    event.preventDefault()

    const loginUrl = `${env.API_URL}/api/login/`
    const username = encodeURIComponent(loginForm.username)
    const password = encodeURIComponent(loginForm.password)
    const next = encodeURIComponent("/")

    const data = `username=${username}&password=${password}&next=${next}`
    const headers = { "Content-Type": "application/x-www-form-urlencoded" }

    await http.get(loginUrl, { headers }) // TODO check behavior
    return await http.post(loginUrl, data, { headers })
  }

  return (
    <form onSubmit={login}>
      <div className="relative">
        <input
          id="username"
          type="text"
          name="username"
          value={loginForm.username}
          onChange={(e) =>
            setLoginForm({ ...loginForm, username: e.target.value })
          }
          placeholder="Username"
          className="peer h-10 w-full border-b-2 border-gray-300 text-gray-900 placeholder-transparent focus:outline-none focus:border-green-500"
        />
        <label
          htmlFor="username"
          className="absolute left-0 -top-3.5 text-gray-600 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-400 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-gray-600 peer-focus:text-sm"
        >
          Username
        </label>
      </div>
      <div className="relative mt-8">
        <input
          id="pasword"
          type="password"
          name="password"
          value={loginForm.password}
          onChange={(e) =>
            setLoginForm({ ...loginForm, password: e.target.value })
          }
          placeholder="Password"
          className="peer h-10 w-full border-b-2 border-gray-300 text-gray-900 placeholder-transparent focus:outline-none focus:border-green-500"
        />
        <label
          htmlFor="password"
          className="absolute left-0 -top-3.5 text-gray-600 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-400 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-gray-600 peer-focus:text-sm"
        >
          Password
        </label>
      </div>
      <input
        className="px-4 py-2 mt-12 rounded bg-green-300 w-full hover:bg-green-200 cursor-pointer focus:outline-none focus:ring-2 focus:ring-green-500"
        type="submit"
        value="Login"
      />
      <a
        href="/"
        className="mt-4 block text-sm text-center font-medium text-green-700 hover:underline focus:outline-none focus:ring-2 focus:ring-green-500 rounded"
      >
        Forgot your password?
      </a>
    </form>
  )
}
