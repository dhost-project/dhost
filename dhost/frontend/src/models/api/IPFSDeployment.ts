import { Deployment } from "./Deployment"

export interface IPFSDeployment extends Deployment {
  ipfs_hash?: string
}
