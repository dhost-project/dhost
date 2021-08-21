interface EnvironmentConfig {
  API_URL: string
}

export const env: EnvironmentConfig = {
  API_URL:
    process.env.REACT_APP_ENV === "production" ? "" : "http://localhost:8000",
}
