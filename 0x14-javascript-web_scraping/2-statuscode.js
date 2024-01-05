#!/usr/bin/node
/**request to print error code*/
const request = require('request');

const url = process.argv[2];

request.get(url, function (error, response, body) {
	console.log("code:", response && response.statusCode);
});

