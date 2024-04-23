#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

res = request.get(url, (err, response) => {
  if (err) {
    console.log(err)
  } else {
    console.log('code: ${response.StatusCode}')
  }
})
