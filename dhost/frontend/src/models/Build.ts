export default interface Build {
  id: string
  is_success?: boolean
  logs?: string
  bundle?: string
  start: string
  end?: string
}
