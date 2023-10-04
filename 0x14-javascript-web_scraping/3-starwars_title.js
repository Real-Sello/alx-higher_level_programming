#!/usr/bin/node

const argv = process.argv;
const movieId = argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

const request = require('request');

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  } else {
    console.error(`Failed to fetch movie data. Status code: ${response.statusCode}`);
  }
});
