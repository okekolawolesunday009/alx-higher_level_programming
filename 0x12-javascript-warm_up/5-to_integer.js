#!/usr/bin/node
const { argv } = require("node:process");

if (isNaN(argv[0])) {
    return "Not a number";
} else {
    argv.forEach((val) => {
       return  console.log(`My number : ${val}`);
    })
}