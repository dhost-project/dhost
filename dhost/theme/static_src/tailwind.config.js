module.exports = {
  mode: "jit",  // or 'aot'
  purge: [
    /**
     * HTML. Paths to Django template files that will contain Tailwind CSS
     * classes.
     */
    '../templates/**/*.html',
    '../../templates/**/*.html',
    '../../**/templates/**/*.html',

    /**
     * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines
     * and make sure patterns match your project structure.
     */
    // '!../../**/node_modules',
    // '../../**/*.js',

    /**
     * Python: If you use Tailwind CSS classes in Python, uncomment the
     * following line and make sure the pattern below matches your project
     * structure.
     */
    // '../../**/*.py'
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/line-clamp'),
    require('@tailwindcss/aspect-ratio'),
  ],
}
