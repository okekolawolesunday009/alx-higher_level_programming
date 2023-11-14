#!/usr/bin/node
const argv  = process.argv.slice(2);

const argOne = parseInt(argv[0]);
const argTwo = parseInt(argv[1]);

function add (a, b) {
     return console.log(a + b);
}
add(argOne, argTwo);
