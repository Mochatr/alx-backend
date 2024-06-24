# Queuing System in JS

This project demonstrates the creation and usage of a queuing system using Redis, Node.js, and Express. The system will cover the basics of interacting with a Redis server, managing asynchronous operations, and integrating a queue system using Kue.

## Resources

### Read or Watch:
- [Redis Quick Start](https://redis.io/docs/latest/integrate/)
- [Redis Client Interface](https://redis.io/docs/latest/develop/connect/cli/)
- [Redis Client for Node JS](https://github.com/redis/node-redis)
- [Kue (Deprecated but still used in the industry)](https://github.com/redis/node-redis)

## Learning Objectives

Upon completion of this project, you should be able to:

- Run a Redis server on your machine.
- Perform simple operations with the Redis client.
- Use a Redis client with Node.js for basic operations.
- Store hash values in Redis.
- Handle asynchronous operations with Redis.
- Implement Kue as a queue system.
- Build a basic Express application interacting with a Redis server.
- Construct a basic Express app interacting with both a Redis server and a queue system.

## Requirements

- All code will be run on Ubuntu 18.04, using Node 12.x, and Redis 5.0.7.
- Every file should end with a new line.
- A `README.md` file at the root of the project folder is mandatory.
- Code should use the `.js` extension.

## Required Files for the Project

### `package.json`
```json
{
    "name": "queuing_system_in_js",
    "version": "1.0.0",
    "description": "",
    "main": "index.js",
    "scripts": {
      "lint": "./node_modules/.bin/eslint",
      "check-lint": "lint [0-9]*.js",
      "test": "./node_modules/.bin/mocha --require @babel/register --exit",
      "dev": "nodemon --exec babel-node --presets @babel/preset-env"
    },
    "author": "",
    "license": "ISC",
    "dependencies": {
      "chai-http": "^4.3.0",
      "express": "^4.17.1",
      "kue": "^0.11.6",
      "redis": "^2.8.0"
    },
    "devDependencies": {
      "@babel/cli": "^7.8.0",
      "@babel/core": "^7.8.0",
      "@babel/node": "^7.8.0",
      "@babel/preset-env": "^7.8.2",
      "@babel/register": "^7.8.0",
      "eslint": "^6.4.0",
      "eslint-config-airbnb-base": "^14.0.0",
      "eslint-plugin-import": "^2.18.2",
      "eslint-plugin-jest": "^22.17.0",
      "nodemon": "^2.0.2",
      "chai": "^4.2.0",
      "mocha": "^6.2.2",
      "request": "^2.88.0",
      "sinon": "^7.5.0"
    }
  }


```
$ cat .babelrc
{
  "presets": [
    "@babel/preset-env"
  ]
}
```

Don’t forget to run $ npm install when you have the package.json.

```
$ npm install
```
