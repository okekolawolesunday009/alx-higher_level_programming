#!/usr/bin/node
/** request to print error code */
const request = require('request');

const url = process.argv[2];
try {
  request.get(url).on('response', function (response) {
    console.log('code:', response && response.statusCode);
  });
} catch (err) {
  console.log(err);
}
