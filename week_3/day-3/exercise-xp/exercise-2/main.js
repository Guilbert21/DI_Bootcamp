const form = document.querySelector("form")
console.log(form)

const firstName = document.querySelector("#fname").value
const lastName = document.querySelector("#lname").value
// console.log(firstName, lastname)
log()

function log(){
    console.log(firstName, lastName)
}

const button  = document.querySelector("#submit")

if (firstName==="" || lastName===""){
    alert("empty fill it")
}else{
    const ul = document.querySelector(".usersAnswer")
    const firstLi = document.createElement("li")
    const secLi = document.createElement("li")
    firstLi.innerText = firstName
    secLi.innerText = lastName
    ul.append(firstLi, secLi)


}
button.addEventListener("submit", log)



