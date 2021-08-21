import { Deployment } from "models/Deployment"

export interface IPFSDeployment extends Deployment {
  ipfs_hash?: string
}
