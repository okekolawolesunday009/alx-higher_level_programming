#!/usr/bin/node
const { argv } = require("node:process")

var x = argv[0];
if (isNaN(x)) {
    return "Mising size"
} else {
    for (let i = 0; i < x; i++) {
        for (let j = 0; i < x; i++) {
            console.log(argv[i][j])
        }  
    }

}
