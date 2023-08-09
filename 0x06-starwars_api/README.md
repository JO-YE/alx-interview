i# Star Wars API Project (0x06)
This project interacts with the Star Wars API to retrieve and display character names from a specific Star Wars movie. The project is implemented using Node.js and the `request` module.


- The line `const characterPromises = characters.map(characterUrl => {` iterates through each character URL in the characters array, and for each URL, it creates a promise that will fetch the character data from the URL. This constructs an array of promises that can later be resolved using Promise.all() to fetch and process character data concurrently

- `Promise.all(characterPromises):`
	- Promise.all() is a method that takes an array of promises and returns a new promise that resolves when all the promises in the array have resolved, or rejects if any of the promises reject. In this case, characterPromises is an array of promises that fetch character data from different URLs.

- `.then(characterNames => { ... }):`
	- The .then() method is called on the promise returned by Promise.all(). It specifies a callback function that will be executed when all the promises in characterPromises have resolved successfully. This callback receives an array of resolved values from the promises, which, in this case, are the character names.

- `characterNames.forEach(name => { ... }):`
	- Inside the .then() callback, the array of resolved character names is iterated using the .forEach() method. For each character name, the provided callback function is executed. This callback function receives the character name as the name parameter.


.
