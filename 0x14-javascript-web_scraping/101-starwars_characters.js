#!/usr/bin/node

const argv = require('process').argv;

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + argv[2];

function GetCharacters (urls) {
  const url = urls.shift();
  request(url, (error, response, body) => {
    if (urls.length) {
      GetCharacters(urls);
    }
    if (error) {
      console.log(error);
    }

    console.log(JSON.parse(body).name);
  });
}

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  const characters = JSON.parse(body).characters;

  GetCharacters(characters);
});
