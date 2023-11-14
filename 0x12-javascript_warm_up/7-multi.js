#!/usr/bin/node
const { argv } = require("node:process")

var x = argv[0];

if (x == 0) {
    return "Missing number of occurrences";
} else  {

    for (let i = 0; i < x; i++) {
       return  console.log("C is fun");
    }
}

