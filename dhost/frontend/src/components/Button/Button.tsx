export interface ButtonProps extends React.HTMLAttributes<HTMLElement> {
  children: any
  active?: boolean
  variant?: string
  size?: "sm" | "lg"
  type?: string
  href?: string
  disabled?: boolean
  target?: any
}

export function Button({
  active = false,
  disabled = false,
  ...props
}: ButtonProps): React.ReactElement {
  return props.href ? (
    <a
      href={props.href}
      className={`border-2 border-indigo-primary-light bg-primary text-white p-2 rounded-md py-2 px-4 ${
        active ? "active relative" : "hover:text-gray-600"
      }`}
    >
      {props.children}
    </a>
  ) : (
    <button className="border-2 border-indigo-primary-light bg-primary text-white rounded-md py-2 px-4">
      {props.children}
    </button>
  )
}
