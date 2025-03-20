//Ex 1 & 2
const prompt = require('prompt-sync')();

let name = prompt("enter your Name:");
let age = parseInt(prompt("enter your Age:"));

if (isNaN(age)) {
    console.log("Invalid age! Please enter a number.");
} else {
   if (age >= 18) {
    console.log("You are eligible to vote.");

    if (age === 100) {
        console.log("Wow! A century old!");
    }
    } else {
    console.log("You are too young to vote.");

    if (age < 16) {
        console.log("You are too young to drive too.");
    }
    }
}


//ex 3
let topics = ["Machine Learning", "Neural Networks", "Computer Vision", "NLP", "Robotics"]

for (topic of topics) {
    console.log(topic);
}

//ex 4
function calculatePower(watts, hours) {
    return watts * hours;
  }
  
  let fridge = calculatePower(200, 24);
  let dryer = calculatePower(1500, 0.5);
  let fan = calculatePower(75, 10);
  
  console.log(`Fridge: ${fridge} Wh`);
  console.log(`Dryer: ${dryer} Wh`);
  console.log(`Fan: ${fan} Wh`);

  //ex 5

let distanceToStop = 40;
let speed = 10;
let brakingPower = 2;

while (distanceToStop > 0) {
  console.log(`Distance to stop: ${distanceToStop} meters, Speed: ${speed} m/s`);
  
  speed = Math.max(speed - brakingPower, 1);  
  distanceToStop = Math.max(distanceToStop - speed, 0); 
}

console.log("Stopping...");
