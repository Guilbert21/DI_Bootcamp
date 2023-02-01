// const list = document.querySelector(".listTasks")
// const listing = document.createElement("ul")
// listing.classList.add("list2")
// // list.appendChild(listing)
// Create an empty array : const tasks = [];
const tasks = []


function addTask(tasks){
if (tasks.value.length == 0){
    return
}

}



let temp;
const div = document.getElementsByClassName(".listTasks")
temp = document.createElement("ul")
temp.className = "myUl"
document.getElementsByTagName("Body")[0].appendChild(temp)
div.appendChild(temp)//was cannnot put the ul inside the div
