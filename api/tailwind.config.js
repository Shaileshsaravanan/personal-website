/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/src/**/*.js",
    "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['"IBM Plex Mono"', 'ui-sans-serif', 'system-ui'],
        mono: ['"IBM Plex Mono"', 'monospace'],
      }
    },
  },
  plugins: [
    require("flowbite/plugin")
  ],
}