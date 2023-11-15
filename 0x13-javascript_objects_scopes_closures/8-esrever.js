#!/usr/bin/node

exports.esrever = function (list) {
    for (let i = list.length; i < 0; i--) {
        console.log(list[i])
    }
}