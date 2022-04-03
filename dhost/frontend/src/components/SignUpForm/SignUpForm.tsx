import { env } from "environment"
import { useEffect, useState } from "react"
import { useHistory } from "react-router"
import Cookies from "universal-cookie"
import { fetchAllRepository } from "api/Repositories"
import { http } from "utils/http"
import { meUser } from "api/Users"
import { useUserContext } from "contexts/UserContext/UserContext"
import { SignUpParams } from "models/api/SignUpParams"

export function SignUpForm() {
    const { userInfo, setUserInfo } = useUserContext()
    let history = useHistory()
    const [signUpForm, setSignUpForm] = useState<SignUpParams>({
        username: "",
        email: "",
        password1: "",
        password2: ""
    })


    async function SignUp(event: React.FormEvent) {
        event.preventDefault()

        const signupUrl = `${env.API_URL}/api/signup/`
        const username = encodeURIComponent(signUpForm.username)
        const email = encodeURIComponent(signUpForm.email)
        const password1 = encodeURIComponent(signUpForm.password1)
        const password2 = encodeURIComponent(signUpForm.password2)
        const next = encodeURIComponent("/")

        const data = `username=${username}&email=${email}&password1=${password1}&password2=${password2}&next=${next}`
        const headers = { "Content-Type": "application/x-www-form-urlencoded" }

        await http.get(signupUrl, { headers }) // TODO check behavior
        const res = await http.post(signupUrl, data, { headers })

        if (res.status == 200 || res.status == 201) {
            const loginUrl = `${env.API_URL}/api/login/`
            const username = encodeURIComponent(signUpForm.username)
            const password = encodeURIComponent(signUpForm.password1)
            const next = encodeURIComponent("/")

            const data = `username=${username}&password=${password}&next=${next}`
            const headers = { "Content-Type": "application/x-www-form-urlencoded" }

            await http.get(loginUrl, { headers }) // TODO check behavior
            const _res = await http.post(loginUrl, data, { headers })


            if ((await meUser()).status !== 401) {
                history.push("/")
                setUserInfo({ ...userInfo, isConnected: true })
                window.location.reload()
            }
        }

        // const _listRepositories = (await fetchAllRepository()).data
        // setUserInfo((userInfo) => ({
        //   ...userInfo,
        //   githubRepositories: _listRepositories,
        // }))

        return res
    }

    return (
        <form onSubmit={SignUp}>
            <div className="relative">
                <input
                    id="username"
                    type="text"
                    name="username"
                    value={signUpForm.username}
                    onChange={(e) =>
                        setSignUpForm({ ...signUpForm, username: e.target.value })
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
                    id="email"
                    type="email"
                    name="email"
                    value={signUpForm.email}
                    onChange={(e) =>
                        setSignUpForm({ ...signUpForm, email: e.target.value })
                    }
                    placeholder="Email"
                    className="peer h-10 w-full border-b-2 border-gray-300 text-gray-900 placeholder-transparent focus:outline-none focus:border-green-500"
                />
                <label
                    htmlFor="password"
                    className="absolute left-0 -top-3.5 text-gray-600 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-400 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-gray-600 peer-focus:text-sm"
                >
                    Email
                </label>
            </div>
            <div className="relative mt-8">
                <input
                    id="pasword1"
                    type="password"
                    name="password1"
                    value={signUpForm.password1}
                    onChange={(e) =>
                        setSignUpForm({ ...signUpForm, password1: e.target.value })
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
            <div className="relative mt-8">
                <input
                    id="pasword2"
                    type="password"
                    name="password2"
                    value={signUpForm.password2}
                    onChange={(e) =>
                        setSignUpForm({ ...signUpForm, password2: e.target.value })
                    }
                    placeholder="Password"
                    className="peer h-10 w-full border-b-2 border-gray-300 text-gray-900 placeholder-transparent focus:outline-none focus:border-green-500"
                />
                <label
                    htmlFor="password"
                    className="absolute left-0 -top-3.5 text-gray-600 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-400 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-gray-600 peer-focus:text-sm"
                >
                    Confirmation Password
                </label>
            </div>
            <a
                onClick={() => { history.push("/login") }}
                className="mt-4 block text-sm text-center font-medium text-green-700 hover:underline focus:outline-none focus:ring-2 focus:ring-green-500 rounded"
            >
                Already have an account?
            </a>
            <input
                className="px-4 py-2 mt-12 rounded bg-blue-300 w-full hover:bg-blue-200 cursor-pointer focus:outline-none focus:ring-2 focus:ring-blue-500"
                type="submit"
                value="SignUp"
            />
        </form>
    )
}
