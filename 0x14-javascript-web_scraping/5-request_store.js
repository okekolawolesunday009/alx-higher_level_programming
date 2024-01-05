#!/usr/bin/node
/** readme */
const fs = require('fs');
const request = require('request');
const filePath = process.argv[3];
const url = process.argv[2];

request.get(url, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  try {
    fs.writeFileSync(filePath, body, 'utf8');
  } catch (err) {
    console.error(`Error writing to file: ${err.message}`);
  }
});
