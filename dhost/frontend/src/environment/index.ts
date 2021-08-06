interface EnvironmentConfig {
  API_URL: string
}

export const env: EnvironmentConfig = (process.env.REACT_APP_ENV = "production")
  ? {
      API_URL: "",
    }
  : {
      API_URL: "http://localhost:8000",
    }
