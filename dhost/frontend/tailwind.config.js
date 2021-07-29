module.exports = {
  // mode: 'jit',
  purge: [
    "./src/**/*.{js,jsx,ts,tsx}",
    "./public/index.html",
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        primary: {
          light: '#cfff95',
          DEFAULT: '#9ccc65',
          dark: '#6b9b37',
        },
        secondary: {
          light: '#fffffb',
          DEFAULT: '#d7ccc8',
          dark: '#a69b97',
        },
        success: "#86EFAC",
        info: "#7DD3FC",
        danger: "#F87171",
        warning: "#FCD34D",
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
