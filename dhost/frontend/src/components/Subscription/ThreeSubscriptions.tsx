import { useState } from "react"
import { useHistory } from "react-router-dom"

export function ThreeSubscriptions() {
  const history = useHistory()
  const [period, setPeriod] = useState("annualy")
  const handlePeriod = (periodicity: string) => {
    setPeriod(periodicity)
  }

  const handleSubscription = (plan: string) => {
    history.push(`/payment?plan=${plan}&periodicity=${period}`)
    window.location.reload()
  }

  return (
    <>
      <div className="xl:mx-auto xl:container md:py-20 2xl:px-0 px-6">
        <div className="lg:flex items-center justify-between">
          <div className=" lg:w-1/2 w-full">
            <p className="text-base leading-4 text-gray-600">
              Choose your plan
            </p>
            <h1
              role="heading"
              className="md:text-5xl text-3xl font-bold leading-10 mt-3 text-gray-800"
            >
              Our pricing plan
            </h1>
            <p
              role="contentinfo"
              className="text-base leading-5 mt-5 text-gray-600"
            >
              We’re working on a suit of tools to make managing complex systems
              easier, for everyone for free. we can’t wait to hear what you
              think
            </p>
            <div className="w-56">
              <div className="bg-gray-100 shadow rounded-full flex items-center mt-10">
                <button
                  onClick={() => handlePeriod("monthly")}
                  className="focus:ring-2 focus:ring-offset-2 focus:ring-green-400 focus:outline-none text-base leading-none rounded-full py-4 px-6 mr-1"
                  id="monthly"
                  style={
                    period === "monthly"
                      ? { color: "white", backgroundColor: "#10B981" }
                      : { color: "#444", backgroundColor: "white" }
                  }
                >
                  Monthly
                </button>
                <button
                  onClick={() => handlePeriod("annualy")}
                  className="bg-green-500 focus:ring-2 focus:ring-offset-2 focus:ring-green-400 focus:outline-none text-base leading-none rounded-full py-4 px-6"
                  id="annually"
                  style={
                    period === "annualy"
                      ? { color: "white", backgroundColor: "#10B981" }
                      : { color: "#444", backgroundColor: "white" }
                  }
                >
                  Annually
                </button>
              </div>
            </div>
          </div>
          <div
            className="xl:w-1/2 lg:w-7/12 relative w-full lg:mt-0 mt-12 md:px-8"
            role="list"
          >
            <img
              src="https://i.ibb.co/0n6DSS3/bgimg.png"
              className="absolute w-full -ml-12 mt-24"
              alt="background circle images"
            />
            <div
              role="listitem"
              className="bg-white cursor-pointer shadow rounded-lg p-8 relative z-30"
              onClick={() => handleSubscription("starter")}
            >
              <div className="md:flex items-center justify-between">
                <h2 className="text-2xl font-semibold leading-6 text-gray-800">
                  Starter
                </h2>
                <p className="text-2xl font-semibold md:mt-0 mt-4 leading-6 text-gray-800">
                  FREE
                </p>
              </div>
              <p className="md:w-80 text-base leading-6 mt-4 text-gray-600">
                Full access to all features and no credit card required
              </p>
            </div>
            <div
              role="listitem"
              className="bg-white cursor-pointer shadow rounded-lg mt-3 flex relative z-30"
              onClick={() => handleSubscription("personal")}
            >
              <div className="w-2.5  h-auto bg-green-500 rounded-tl-md rounded-bl-md" />
              <div className="w-full p-8">
                <div className="md:flex items-center justify-between">
                  <h2 className="text-2xl font-semibold leading-6 text-gray-800">
                    Personal
                  </h2>
                  <p className="text-2xl md:mt-0 mt-4 font-semibold leading-6 text-gray-800">
                    {period === "annualy" ? "$7" : "$9"}
                    <span className="font-normal text-base">/mo</span>
                  </p>
                </div>
                <p className="md:w-80 text-base leading-6 mt-4 text-gray-600">
                  Unlimited products features and dedicated support channels
                </p>
              </div>
            </div>
            <div
              role="listitem"
              className="bg-white cursor-pointer shadow rounded-lg p-8 relative z-30 mt-7"
              onClick={() => handleSubscription("team")}
            >
              <div className="md:flex items-center justify-between">
                <h2 className="text-2xl font-semibold leading-6 text-gray-800">
                  Team
                </h2>
                <p className="text-2xl md:mt-0 mt-4 font-semibold leading-6 text-gray-800">
                  {period === "annualy" ? "$16" : "$18"}
                  <span className="font-normal text-base">/mo</span>
                </p>
              </div>
              <p className="md:w-80 text-base leading-6 mt-4 text-gray-600">
                Unlimited products features and dedicated support channels
              </p>
            </div>
          </div>
        </div>
      </div>
    </>
  )
}
