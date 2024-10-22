/** @type {import('tailwindcss').Config} */
export default {
	content: [
		'./src/**/*.html',
		'./src/**/*.js',
		'./src/**/*.vue'
	],
	theme: {
		extend: {
			fontFamily: {
				body: ['Quicksand'],
				navBrand: ['Playwrite GB S'],
			},
		},
	},
	plugins: [],
}
