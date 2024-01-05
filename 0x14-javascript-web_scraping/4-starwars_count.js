#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  try {
    const data = JSON.parse(body).results;
    console.log(data.reduce((count, movie) => {
      return movie.characters.find(cast => cast.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  } catch (err) {
    console.log(err);
  }
});
