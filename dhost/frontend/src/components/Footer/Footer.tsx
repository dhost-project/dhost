const footer_nav_left = [
  {
    name: "Documentation",
    href: "https://github.com/dhost-project/dhost-doc",
    target_blank: true,
  },
  {
    name: "Examples",
    href: "https://github.com/dhost-project/dhost-examples",
    target_blank: true,
  },
  {
    name: "Source code",
    href: "https://github.com/dhost-project/dhost",
    target_blank: true,
  },
  {
    name: "Issues",
    href: "https://github.com/dhost-project/dhost/issues/new",
    target_blank: true,
  },
  {
    name: "Support",
    href: "/support",
    target_blank: true,
  },
]

const DHostFooter = (): React.ReactElement => (
  <span className="group"><span className="text-green-500 group-hover:text-green-700">D</span>Host 2020-2021</span>
)

const footer_nav_right = [
  {
    name: "Privacy",
    href: "/privacy",
    target_blank: false,
  },
  {
    name: "Legal",
    href: "/legal",
    target_blank: false,
  },
  {
    name: <DHostFooter />,
    href: "/",
    target_blank: false,
  },
]

export default function Footer(): React.ReactElement {
  return (
    <footer>
      <div className="flex justify-between border-t border-gray-200 font-light py-2 px-2">
        <div>
          {footer_nav_left.map((item) => (
            <a href={item.href} rel="noreferrer" target="_blank" className="mx-2 text-gray-500 hover:text-gray-700">
              {item.name}
            </a>
          ))}
        </div>
        <div>
          {footer_nav_right.map((item) => (
            <a href={item.href} rel="noreferrer" target="_blank" className="mx-2 text-gray-500 hover:text-gray-700">
              {item.name}
            </a>
          ))}
        </div>
      </div>
    </footer>
  )
}
