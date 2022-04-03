import { env } from "environment"
import { SignUpForm } from "components/SignUpForm"

export function SignUp(): React.ReactElement {
    const githublLoginUrl = `${env.API_URL}/api/social/login/github/`

    return (
        <div className="mx-auto w-96 border rounded-xl shadow-xl py-8 my-20">
            <h1 className="text-3xl mb-12 mt-2 text-center">SignUp</h1>
            <div className="px-8">
                <SignUpForm />
            </div>
        </div>
    )
}
