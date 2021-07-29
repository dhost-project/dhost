import Deployment from "models/Deployment"

export default interface IPFSDeployment extends Deployment {
  ipfs_hash?: string
}
