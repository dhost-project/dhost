import { Menu, Popover, Transition } from "@headlessui/react"
import {
  BeakerIcon,
  BellIcon,
  CogIcon,
  LogoutIcon,
  MenuIcon,
  PuzzleIcon,
  SearchIcon,
  ShieldCheckIcon,
  SupportIcon,
  UserGroupIcon,
  XIcon,
} from "@heroicons/react/outline"
import { Fragment, useEffect, useState } from "react"
import { Button } from "react-bootstrap"
import { Link, useHistory } from "react-router-dom"
import { logout } from "api/Logout"
import logo from "assets/logo.svg"
import { useModals } from "contexts/ModalsContext/ModalsContext"
import { useUserContext } from "contexts/UserContext/UserContext"
import { gravatar_url } from "utils/gravatar"

// TODO remove, for test only
const gravatar = gravatar_url("7bc5dd72ce835d2a2868785729c0f176")

const account_sections = [
  [
    {
      name: "Dapps",
      href: "/",
      icon: BeakerIcon,
    },
    {
      name: "Pricing",
      href: "/pricing/",
      icon: PuzzleIcon,
    },
  ],
  [
    {
      name: "Settings",
      href: "/account/settings/",
      icon: CogIcon,
    },
    {
      name: "Security",
      href: "/account/settings/",
      icon: ShieldCheckIcon,
    },
    {
      name: "Support",
      href: "/support/",
      icon: SupportIcon,
    },
  ],
  [
    {
      name: "Logout",
      href: "/login/",
      icon: LogoutIcon,
    },
  ],
]

export interface sectionType {
  name: string
  href: string
  icon: (props: React.SVGProps<SVGSVGElement>) => JSX.Element
}

function BellNotifications(): React.ReactElement {
  return (
    <Link to="/notifications" className="mr-4 p-1 rounded-full group">
      <div className="relative">
        <BellIcon
          className="h-6 w-6 text-gray-400 group-hover:text-gray-500"
          aria-hidden="true"
        />
        <div
          className="absolute top-0 right-0 h-3 w-3 rounded-full bg-gradient-to-b
          from-pink-300 to-red-400"
        />
      </div>
    </Link>
  )
}

function AccountMenu(): React.ReactElement {
  let history = useHistory()
  const { userInfo, setUserInfo } = useUserContext()

  const handleClick = async (item: sectionType) => {
    if (item.name === "Logout") {
      await logout()
      setUserInfo((userInfo) => ({
        ...userInfo,
        isConnected: false,
      }))
      window.location.href = "/login"
    }
    history.push(`${item.href}`)
  }

  return (
    <Menu as="div" className="relative">
      <Menu.Button
        as="img"
        className="my-2 mx-1 cursor-pointer rounded-full border-2
        border-green-400 hover:border-green-500"
        src={userInfo.user.avatar ?? gravatar}
        height="32"
        width="32"
        alt="gravatar"
      />
      <Transition
        as={Fragment}
        enter="transition ease-out -translate-y-full"
        enterFrom="transform -translate-y-full"
        enterTo="transform duration-150"
        leave="transition ease-in"
        leaveFrom="transform"
        leaveTo="transform -translate-y-full"
      >
        <Menu.Items
          className="absolute right-0 overflow-hidden origin-top-right bg-white
          border-b border-l border-r border-gray-200 divide-y divide-gray-100
          rounded-b-lg shadow-lg focus:outline-none cursor-pointer"
          style={{ zIndex: -1 }}
        >
          {account_sections.map((account_section, index) => (
            <div key={`account_section-${index}`} className="py-1">
              {account_section.map((item) => (
                <Menu.Item key={`${item.name}-${item.href}`}>
                  {({ active }) => (
                    <a
                      className={`${active ? "bg-gray-50" : "text-gray-900"
                        } group flex items-center w-full pl-4 pr-24 py-2 text-sm`}
                      onClick={() => handleClick(item)}
                    >
                      <item.icon className="h-5 w-5 mr-2" aria-hidden="true" />
                      {item.name}
                    </a>
                  )}
                </Menu.Item>
              ))}
            </div>
          ))}
        </Menu.Items>
      </Transition>
    </Menu>
  )
}

export function Navbar(): React.ReactElement {
  const { setShowCreateDappModal } = useModals()
  const { userInfo, setUserInfo } = useUserContext()
  let history = useHistory()

  const handleClick = async (item: sectionType) => {
    if (item.name === "Logout") {
      await logout()
      setUserInfo((userInfo) => ({
        ...userInfo,
        isConnected: false,
      }))
      window.location.href = "/login"
    }
    history.push(`${item.href}`)
  }

  const renderConnected = () => {
    return (
      <Popover className="sticky top-0 bg-white z-40">
        {({ open }) => (
          <>
            <div
              className="
          flex justify-between items-center px-3 md:justify-start
          bg-white border-b"
            >
              <div className="flex justify-start lg:w-0 lg:flex-1">
                <Link to="/">
                  <span className="sr-only">DHost</span>
                  <img
                    className="my-2 mx-1 h-8 w-auto"
                    src={logo}
                    alt="DHost"
                  />
                </Link>
              </div>
              <div className="-mr-2 -my-2 md:hidden">
                <Popover.Button
                  className="bg-white rounded-md p-2 inline-flex items-center
              justify-center text-gray-400 hover:text-gray-500
              hover:bg-gray-100 focus:outline-none"
                >
                  <span className="sr-only">Open menu</span>
                  <MenuIcon className="h-6 w-6" aria-hidden="true" />
                </Popover.Button>
              </div>
              <div
                className="hidden md:flex justify-end md:flex-1 lg:w-0
            items-center"
              >
                <Button
                  className="flex justify-center items-center h-8 mr-4 bg-green-500 hover:bg-green-600 focus:bg-green-700 border-none"
                  onClick={() => {
                    setShowCreateDappModal(true)
                  }}
                >
                  Create Dapp
                </Button>
                <BellNotifications />
                <AccountMenu />
              </div>
            </div>
            <Transition
              show={open}
              as={Fragment}
              enter="duration-200 ease-out"
              enterFrom="opacity-0 scale-95"
              enterTo="opacity-100 scale-100"
              leave="duration-100 ease-in"
              leaveFrom="opacity-100 scale-100"
              leaveTo="opacity-0 scale-95"
            >
              <Popover.Panel
                focus
                static
                className="absolute top-0 inset-x-0 p-2 transition transform
            origin-top-right md:hidden"
              >
                <div
                  className="rounded-lg shadow-lg ring-1 ring-black ring-opacity-5
              bg-white divide-y-2 divide-gray-50"
                >
                  <div className="pt-5 pb-6 px-5">
                    <div className="flex items-center justify-between">
                      <div>
                        <img className="h-8 w-auto" src={logo} alt="DHost" />
                      </div>
                      <div className="-mr-2">
                        <Popover.Button
                          className="
                      bg-white rounded-md p-2 inline-flex items-center
                      justify-center text-gray-400 hover:text-gray-500
                      hover:bg-gray-100 focus:outline-none"
                        >
                          <span className="sr-only">Close menu</span>
                          <XIcon className="h-6 w-6" aria-hidden="true" />
                        </Popover.Button>
                      </div>
                    </div>
                  </div>
                  <div className="py-6 px-5 space-y-6">
                    <div className="grid grid-cols-2 gap-y-4 gap-x-8">
                      {account_sections.map((account_section, index) => (
                        <Fragment key={`account_section-responsive-${index}`}>
                          {account_section.map((item) => (
                            <a
                              key={item.name}
                              onClick={() => handleClick(item)}
                              className="text-base font-medium text-gray-900
                          hover:text-gray-700"
                            >
                              {item.name}
                            </a>
                          ))}
                        </Fragment>
                      ))}
                    </div>
                  </div>
                </div>
              </Popover.Panel>
            </Transition>
          </>
        )}
      </Popover>
    )
  }

  const renderNotConnected = () => {
    return (
      <Popover className="relative bg-white z-40">
        {({ open }) => (
          <>
            <div
              className="
            flex justify-between items-center px-3 md:justify-start
            bg-white border-b"
            >
              <div className="flex justify-start lg:w-0 lg:flex-1">
                <span>
                  <span className="sr-only">DHost</span>
                  <img
                    className="my-2 mx-1 h-8 w-auto"
                    src={logo}
                    alt="DHost"
                  />
                </span>
              </div>
            </div>
          </>
        )}
      </Popover>
    )
  }

  return userInfo.isConnected ? renderConnected() : renderNotConnected()
}
