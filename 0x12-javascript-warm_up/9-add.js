#!/usr/bin/node
const { argv } = require("node:process")

var arg_1 = argv[1];
var arg_2 = argv[2];

function add(a, b) {
    return console.log(a + b);
}
add(arg_1, arg_2);
