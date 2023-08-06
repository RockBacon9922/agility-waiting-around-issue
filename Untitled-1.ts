import { faker } from "@faker-js/faker";
import { Solve, IModel } from "@ellbur/javascript-lp-solver";

console.log("Hello World");

type Dog = {
  name: string;
};
type Runner = {
  name: string;
  dogs: Dog[];
};

type Class = {
  name: string;
  dogs: Dog[];
};

type Ring = {
  id: number;
  classes: Class[];
};
type Show = {
  name: string;
  rings: Ring[];
};

const randomNumberGenerator = (min: number, max: number): number => {
  return Math.floor(Math.random() * (max - min + 1) + min);
};

// create a random number of runners and put them in a an array
const createRunners = (numRunners: number): Runner[] => {
  let runners: Runner[] = [];
  for (let i = 0; i < numRunners; i++) {
    // create a random number of dogs
    let numDogs = randomNumberGenerator(1, 3);
    let dogs: Dog[] = [];
    for (let j = 0; j < numDogs; j++) {
      dogs.push({ name: faker.animal.dog() });
    }
    runners.push({ name: faker.person.fullName(), dogs });
  }
  return runners;
};

const createClasses = (numClasses: number, dogsTemplate: Dog[]): Class[] => {
  // create a copy of dogs
  let dogs = dogsTemplate;
  // each class
  let classes: Class[] = [];
  for (let i = 0; i < numClasses; i++) {
    // choose a random set of runners
    let numDogs = randomNumberGenerator(1, dogs.length);
    let classDogs: Dog[] = [];
    for (let j = 0; j < numDogs; j++) {
      // choose a random runner
      let dogIndex = randomNumberGenerator(0, dogs.length - 1);
      classDogs.push(dogs[dogIndex]);
      // remove the dog from the list
      dogs.splice(dogIndex, 1);
    }
    classes.push({ name: faker.commerce.productName(), dogs: classDogs });
  }
  return classes;
};

const createRing = (id: number, classes: Class[]): Ring => {
  return { classes: classes, id };
};

const createShow = (rings: Ring[], name: string): Show => {
  return { name: name, rings };
};

const runners = createRunners(500);
// get all the dogs from the runners
const rings = [
  createRing(1, createClasses(4, runners)),
  createRing(2, createClasses(4, runners)),
  createRing(3, createClasses(4, runners)),
  createRing(4, createClasses(4, runners)),
  createRing(5, createClasses(4, runners)),
  createRing(6, createClasses(4, runners)),
];

const show = createShow(rings, "My Show");

console.log(show);
