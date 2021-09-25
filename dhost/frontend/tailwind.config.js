module.exports = {
  mode: "jit",
  purge: [
    "./src/**/*.{js,jsx,ts,tsx}",
    "./public/index.html",
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        primary: {
          light: "#cfff95",
          DEFAULT: "#9ccc65",
          dark: "#6b9b37",
        },
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
