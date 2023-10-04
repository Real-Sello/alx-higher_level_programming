#!/usr/bin/node

const argv = require('process').argv;

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  const characters = JSON.parse(body).characters;
  for (const x in characters) {
    request(characters[x], (error, response, body) => {
      if (error) {
        console.log(error);
      }

      const name = JSON.parse(body).name;
      console.log(name);
    });
  }
});
