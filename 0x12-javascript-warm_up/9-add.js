#!/usr/bin/node
const  argv  = process.argv.slice(2);

const arg_1 = parseInt(argv[0]);
const arg_2 = parseInt(argv[1]);

function add (a, b) {
     return console.log(a + b);
}
add(arg_1, arg_2);
