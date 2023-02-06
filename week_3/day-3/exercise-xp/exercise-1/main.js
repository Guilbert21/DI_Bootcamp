const h1 = document.getElementsByTagName("h1")
console.log(h1)

const article = document.querySelector("article")
article.lastElementChild.remove()

const h2 = getFirstH2()

function changeBackground(){
    h2.classList.add("red")
}

const h3 = getfirstH3()

function hideElement(){
    h3.classList.add("hide")
}

addButton()
function addButton(){
    const button = document.createElement("button")
    button.textContent = "Make text bold"
    const article = article.firstElement("article")
    article.appendChild(button)
}