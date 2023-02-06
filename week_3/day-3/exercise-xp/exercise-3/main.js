let allBoldItems;

function getAllBoldItems(){
    allBoldItems = document.getElementsByTagName("strong")

}

function highlight(){
    getAllBoldItems()
    for(const boldItem of allBoldItems)
    boldItem.style.color = "blue"
}
highlight()

function returnNormal(){
    getAllBoldItems()
    for (const item of allBoldItems){
        item.style.color = "black"
    }
}
returnNormal()

const para = document.querySelector("p")
para.addEventListener("mouserover", highlight)