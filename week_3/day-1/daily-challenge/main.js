// Create an array which value is the planets of the solar system.
const planetsArray = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
let temp;

const section = document.querySelector(".listPlanets")
// For each planet in the array, create a <div> using createElement. This div should have a class named "planet".
for (let i = 0; i < planetsArray.length; i++) {
    temp = document.createElement("div")
    temp.className = "planet color-" +[i + 1]
    temp.innerHTML = planetsArray[i]
    document.getElementsByTagName("Body")[0].appendChild(temp)
   
    section.appendChild(temp)
}
