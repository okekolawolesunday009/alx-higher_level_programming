#!/usr/bin/node
/** readme */
const request = require('request');
const url = process.argv[2];

request.get(url, function (err, res, body) {
  if (err) {
    console.log(err);
    return;
  }
  try {
    const dataArray = JSON.parse(body);
    const userCounts = {};
    for (let i = 0; i < dataArray.length; i++) {
      const obj = dataArray[i];
      if (obj.completed === true) {
        if (obj.completed === true) {
          const userId = obj.userId || 1;
          userCounts[userId] = (userCounts[userId] || 0) + 1;
        }
      }
    }
    console.log(userCounts);
  } catch (err) {
    console.error(err);
  }
});
