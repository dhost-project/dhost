/**
 * @param command Command used during the build process
 * @param docker Container used for the build process
 */
export interface BuildOptions {
  command?: string
  docker?: string
}
