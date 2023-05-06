#!/usr/bin/node

const request = require('request');

const MOVIE_ID = process.argv[2];
const URL = `https://swapi.dev/api/films/${MOVIE_ID}/`;

request(URL, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const characters = JSON.parse(body).characters;
  printCharacters(characters, 0);
});

function printCharacters(characters, index) {
  if (index >= characters.length) {
    return;
  }
  request(characters[index], function (error, response, body) {
    if (error) {
      console.error(error);
      return;
    }
    console.log(JSON.parse(body).name);
    printCharacters(characters, index + 1);
  });
}
