#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterId = '18';
let characterCount = 0;

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const res = JSON.parse(body);
    res.results.forEach((film) => {
      film.characters.forEach((actor) => {
        if (actor.includes(characterId)) {
          characterCount += 1;
        }
      }); 
    }); 
    console.log(characterCount);
  }
});
