export default function gravatar_url(
  gravatar_hash: string = "",
  size: number = 40
): string {
  var gravatar_url = "https://www.gravatar.com/avatar/" + gravatar_hash
  gravatar_url += encodeURI("?s=" + size)
  return gravatar_url
}
