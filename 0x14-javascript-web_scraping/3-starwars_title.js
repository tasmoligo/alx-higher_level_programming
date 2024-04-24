#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, 'utf-8', (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const filmPart = JSON.parse(body);
    console.log(filmPart.title);
  }
});
