import { Dapp } from "./Dapp"

export interface IPFSDapp extends Dapp {
  ipfs_gateway?: string
  ipfs_hash?: string
}

/**
 * @param slug string <= 256 characters ^[-a-zA-Z0-9_]+$
 * @param ipfs_gateway string <uri> <= 200 characters Nullable
 */
export interface IPFSDappParams {
  slug: string
  ipfs_gateway?: string
}