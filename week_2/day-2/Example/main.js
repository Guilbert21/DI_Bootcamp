// let newsfeed = [{
//     username:"Guilbert",
//     password:"1234"
// }
// ]

// let database = obj
// newsfeed.username = "alexis"
// newsfeed.timeline = "null"

// let age = prompt("how old are you?")

// age = parseInt(age)

// console.log(age)

let str = "Happy BirthDay";
let patt = /birthday/i;
let result = str.match(patt);
console.log(result); //returns true

if (result){
    console.log('Yes')
} else{
    console.log('No');
}