#!/usr/bin/node

const request = require('request');

const apiURL = String(process.argv[2]);

const WA_URL = 'https://swapi-api.alx-tools.com/api/people/18/';

request(apiURL, (error, response, body) => {
  let count = 0;
  if (error) {
    console.log(error);
  } else {
    let i = 0;
    const movie = JSON.parse(body);
    while (i < movie.results.length) {
      if (movie.results[i].characters.includes(WA_URL)) {
        count++;
      }
      i++;
    }
  }
  console.log(count);
});