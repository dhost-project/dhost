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
  if (props.href) {
    return (
      <a
        href={props.href}
        className={`border-2 border-indigo-primary-light bg-primary p-2 rounded-md py-2 px-4 ${
          active ? "active relative" : "hover:text-gray-600"
        }`}
      >
        {props.children}
      </a>
    )
  }

  return (
    <button className="border-2 border-indigo-primary-light bg-primary rounded-md py-2 px-4">
      {props.children}
    </button>
  )
}
