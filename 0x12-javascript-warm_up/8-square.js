#!/usr/bin/node
const  argv  = process.argv.slice(2);

var x = argv[0];
if (isNaN(x)) {
     console.log('Mising size');
} else {
    for (let i = 0; i < x; i++) {
         for (let j = 0; i < x; i++) {
             console.log(argv[i][j])
            }  
    }

}
