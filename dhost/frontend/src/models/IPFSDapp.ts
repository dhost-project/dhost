import Dapp from "models/Dapp"

export default interface IPFSDapp extends Dapp {
  ipfs_gateway?: string,
  ipfs_hash?: string,
}
