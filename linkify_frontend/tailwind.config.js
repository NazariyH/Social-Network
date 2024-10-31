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
			spacing: {
				'post-file': '36rem',
				'profile-view': 'calc(100% - 80px)' // 80px - size of the side navbar
			}
		},
	},
	plugins: [],
}
