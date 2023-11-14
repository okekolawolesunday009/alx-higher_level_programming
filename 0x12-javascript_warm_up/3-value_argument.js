#!/usr/bin/node
const { argv } = require("node:process");

if (argv[0] == 0) {
    return "No argument";
} else {
    argv.forEach((val) => {
       return  console.log(val);
    })
}