#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
request(url, function (error, url, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(process.argv[3], body, 'utf-8', function (err) {
      if (err) console.log('error');
    });
  }
});
