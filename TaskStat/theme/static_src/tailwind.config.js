/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        '../templates/**/*.html',
        '../../templates/**/*.html',
        '../../**/templates/**/*.html',
        './scr/**/*.{html,js}'
    ],
    theme: {
        extend: {
            spacing: {
                '120': '28rem',
                '124': '30rem',
                '128': '32rem',
              },
            fontFamily:{
                sans:['Roboto', 'sans-serif']
            }
        },
    },
    plugins: [
        require('tailwind-scrollbar'),
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
