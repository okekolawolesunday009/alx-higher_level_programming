#!/usr/bin/node
const { argv } = require("node:process");

if (argv[0] == 0) {
    return "No argument";
} else {
    return "Argument found";
}