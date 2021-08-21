import { Dapp } from "models/Dapp"

export interface IPFSDapp extends Dapp {
  ipfs_gateway?: string
  ipfs_hash?: string
}
