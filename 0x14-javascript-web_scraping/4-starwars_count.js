#!/usr/bin/node

const request = require('request');

const apiURL = String(process.argv[2]);
const WA_URL = 'https://swapi-api.alx-tools.com/api/people/18/';

request(apiURL, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const movieData = JSON.parse(body);
  const wedgeAntillesMovies = movieData.results.filter(movie => {
    return movie.characters.includes(WA_URL);
  });

  console.log(wedgeAntillesMovies.length);
});
