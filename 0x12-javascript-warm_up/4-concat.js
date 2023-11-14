#!/usr/bin/node
const { argv } = require("node:process")

var arg_1 = argv[1];
var arg_2 = argv[2];

console.log(`${arg_1} is ${arg_2}`);