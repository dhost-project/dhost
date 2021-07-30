export default function gravatar_url(gravatar_hash: string = ""): string {
  var gravatar_url = "https://www.gravatar.com/avatar/" + gravatar_hash
  gravatar_url += encodeURI("?s=40")
  return gravatar_url
}
