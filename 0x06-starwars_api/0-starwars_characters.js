#!/usr/bin/node
// A script that prints all characters of a Star Wars movie

// Importing the 'request' module
const request = require('request');

/* checking if the correct number of arguments is provided */
if (process.argv.length !== 3) {
  console.log('Kindly provide your movie ID');
  process.exit(1);
}

/*Extracting the Movie ID from command line arguments */
const movieId = process.argv[2];

/* Constructing the URL for the movie's API endpoint */
const url = `https://swapi.dev/api/films/${movieId}/`;

/* Performing the request to the movie's API endpoint */
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error('API Error:', body);
    return;
  }
  /* Parsing  the JSON response */
  const movieData = JSON.parse(body);

  // Fetching and displaying character names
  const characters = movieData.characters;
  fetchAndDisplayCharacters(characters);
});

 /* Function to fetch and display character names */
  function fetchAndDisplayCharacters(characters) {
    const Promises = characters.map(individualUrl) => {
      request(individualUrl, (error, response, body) => {
        if(error) {
          reject(error);
          return;
	}

        if (response.statusCode !== 200) {
          reject('API Error for ${individualUrl}')
          return;
	}

        const characterData = JSON.parse(body);
        resolve(characterData.name);
      });
    });
  };

  Promise.all(Promises)
    .then(characterNames => {
      /* Displaying character names*/
      characterNames.forEach(name => {
        console.log(name);
      });
    })
    .catch(error => {
      console.error('Error fetching character data:', error);
    });
  


