import { Menu, Popover, Transition } from "@headlessui/react"
import {
  BeakerIcon,
  BellIcon,
  CogIcon,
  LogoutIcon,
  MenuIcon,
  SearchIcon,
  ShieldCheckIcon,
  UserGroupIcon,
  XIcon,
} from "@heroicons/react/outline"
import { Fragment } from "react"

import logo from "assets/logo.svg"

import gravatar_url from "utils/gravatar"

// TODO remove, for test only
const gravatar = gravatar_url("7bc5dd72ce835d2a2868785729c0f176")

const account_sections = [
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
  ],
  [
    {
      name: "Dapps",
      href: "/dapps",
      icon: BeakerIcon,
    },
    {
      name: "Teams",
      href: "/404",
      icon: UserGroupIcon,
    },
  ],
  [
    {
      name: "Logout",
      href: "/404",
      icon: LogoutIcon,
    },
  ],
]

function BellNotifications(): React.ReactElement {
  return (
    <a href="/notifications/" className="mr-4 p-1 rounded-full group">
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
    </a>
  )
}

export default function Navbar(): React.ReactElement {
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
              <a href="/">
                <span className="sr-only">DHost</span>
                <img className="my-2 mx-1 h-8 w-auto" src={logo} alt="DHost" />
              </a>
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
            <div className="hidden md:flex md:flex-1 px-16">
              <input
                type="text"
                className="flex-grow px-2 rounded-l border text-gray-700"
                placeholder="Search dapps"
              />
              <button
                className="flex-none px-2 text-gray-500 rounded-r border-r
                border-b border-t hover:bg-gray-100"
              >
                <SearchIcon className="h-5" />
              </button>
            </div>
            <div
              className="hidden md:flex justify-end md:flex-1 lg:w-0
              items-center"
            >
              <BellNotifications />
              <div>
                <Menu as="div" className="relative">
                  <Menu.Button
                    as="img"
                    className="my-2 mx-1 cursor-pointer rounded-full border-2
                    border-green-400 hover:border-green-500"
                    src={gravatar}
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
                      className="
                      absolute right-0 overflow-hidden w-56 origin-top-right
                      bg-white border-b border-l border-r border-gray-200
                      divide-y divide-gray-100 rounded-b-lg shadow-lg
                      focus:outline-none"
                      style={{ zIndex: -1 }}
                    >
                      {account_sections.map((account_section) => (
                        <div className="py-1">
                          {account_section.map((item) => (
                            <Menu.Item>
                              {({ active }) => (
                                <a
                                  className={`${
                                    active ? "bg-gray-50" : "text-gray-900"
                                  } group flex items-center w-full px-4 py-2 text-sm`}
                                  href={item.href}
                                >
                                  <item.icon
                                    className="h-5 w-5 mr-2"
                                    aria-hidden="true"
                                  />
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
              </div>
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
              className="absolute top-0 inset-x-0 p-2 transition transform origin-top-right md:hidden"
            >
              <div className="rounded-lg shadow-lg ring-1 ring-black ring-opacity-5 bg-white divide-y-2 divide-gray-50">
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
                    {account_sections.map((account_section) => (
                      <>
                        {account_section.map((item) => (
                          <a
                            key={item.name}
                            href={item.href}
                            className="text-base font-medium text-gray-900 hover:text-gray-700"
                          >
                            {item.name}
                          </a>
                        ))}
                      </>
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
