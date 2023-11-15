#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
    for (let i = 0; i < list.length; i++) {
        let count = 0;
        if (list[i] === searchElement) {
            count++;
        } 
        console.log(count);
    }

}