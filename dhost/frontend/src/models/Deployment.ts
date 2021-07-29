export default interface Deployment {
  id: string,
  dapp: string,
  bundle?: string,
  status: string,
  start?: string,
  end?: string,
}
