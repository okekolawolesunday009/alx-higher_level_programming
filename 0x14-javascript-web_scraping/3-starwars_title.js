#!/usr/bin/node
/**js scrapping of star wars appi*/
const request = require('request')
const url = "https://swapi-api.alx-tools.com/api/films/"
const film_id = process.argv[2]

request.get(url + film_id, function (error, response, body) {
	try {
		const filmData = JSON.parse(body);
		console.log(filmData && filmData.title);
	} catch (err) {
		console.error(err);
	}
});
