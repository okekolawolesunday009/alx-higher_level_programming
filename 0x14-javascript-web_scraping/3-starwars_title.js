#!/usr/bin/node
/** js scrapping of star wars appi */
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const filmId = process.argv[2];

request.get(url + filmId, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  try {
    const filmData = JSON.parse(body);
    console.log(filmData && filmData.title);
  } catch (err) {
    console.error(err);
  }
});
