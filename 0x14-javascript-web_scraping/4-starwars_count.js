#!/usr/bin/node

const request = require('request');

const apiURL = 'https://swapi-api.alx-tools.com/api/films/';
const WA_URL = 'https://swapi-api.alx-tools.com/api/people/18/';

request(apiURL, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const films = JSON.parse(body).results;
  let count = 0;

  films.forEach((film) => {
    if (film.characters.includes(WA_URL)) {
      count++;
    }
  });

  console.log(count);
});
