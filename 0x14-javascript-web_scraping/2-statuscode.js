#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, function (error, url) {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ' + url.statusCode);
  }
});
