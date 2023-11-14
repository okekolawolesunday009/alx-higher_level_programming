#!/usr/bin/node
const  argv  = process.argv.slice(2);

const arg_1 = argv[1];
const arg_2 = argv[2];

function add (a, b) {
     return console.log(a + b);
}
add(arg_1, arg_2);
