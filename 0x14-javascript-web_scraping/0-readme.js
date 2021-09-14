#!/usr/bin/node
/* This script print the content of a file */
var fs = require('fs')
fs.readFile(process.argv[2], 'utf-8', (err, data) => {
    if (err) {
        return console.error(err)
    }
    console.log(data)
})