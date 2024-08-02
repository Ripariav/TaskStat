module.exports = {
    content: [
        '../templates/**/*.html',
        '../../templates/**/*.html',
        '../../**/templates/**/*.html',
        './staticfiles/**/*.{html,js}'
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
