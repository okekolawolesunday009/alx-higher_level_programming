#!/usr/bin/node

const data = require('100-data')

const newData = data.map((x) =>  {
    x * [0, 1, 2, 3]
})
console.log(newData);