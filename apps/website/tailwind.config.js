/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  darkMode: 'class', // Add this line to enable class-based dark mode
  theme: {
    extend: {
      colors: {
        primary: '#F55B1F',
        danger: '#dc3545',
        danger_text: '#ff3c78',
        green: '#3cd278',
        grey: '#8e8e8e',
        muted: '#547593',
        midnight_text: '#102d47',
        border: '#dfebfc',
        darkmode: '#08162b',
        hero_bg: '#f3f9fd',
        dark_hero_bg: '#121c2e',
        darkheader: '#141d2f',
        dark_border: '#253c50',
        foottext: '#668199',
        search: '#163858',
        dark_b: '#1b2c44',
      },
      fontSize: {
        '13': '0.8125rem',
        '14': '0.875rem',
        '16': '1rem',
        '18': '1.125rem',
        '19': '1.1875rem',
        '20': '1.25rem',
        '22': '1.375rem',
        '24': '1.5rem',
        '25': '1.5625rem',
        '28': '1.75rem',
        '35': '2.1875rem',
        '40': '2.5rem',
        '48': '3rem',
        '50': '3.125rem',
      },
      spacing: {
        '47': '304px',
        '49': '350px',
        '150': '750px',
        '6_25': '6.25rem',
      }
    },
  },
  plugins: [
    function ({ addUtilities }) {
      addUtilities({
        '.outline-hidden': {
          outline: 'none',
          '-webkit-tap-highlight-color': 'transparent',
        }
      })
    }
  ],
}