const libForm = document.getElementById("libform")
function getInputValue(e){
   e.preventDefault();
    let noun = document.getElementById("noun").value;
    console.log(noun);
    let adjective = document.getElementById("adjective").value;
    console.log(adjective);
    let Name = document.getElementById("person").value;
    console.log(Name);
    let verb = document.getElementById("verb").value;
    console.log(verb);
    let place = document.getElementById("place").value;
    console.log(place);
    submitOK = "true"

    if (noun == "") {
        alert("No noun has been enterd");
        submitOK = "false";
      }

      if (adjective == "") {
        alert("No adjective has been entered");
        submitOK = "false";
      }

      if (Name == "") {
        alert("No name has been entered");
        submitOK = "false";
      }

      if (verb == "") {
        alert("No verb has been entered");
        submitOK = "false";
      }

      if (place== "") {
        alert("No place has been entered");
        submitOK = "false";
      }
    Event.preventDefault();
}
// Form.onsubmit = getInputValue()
getInputValue(Event)



// // const wrapper = document.querySelector(".wrapper"),
// // form = document.querySelector("#libform"),
// // submitInput = form[0].querySelector('input[type = "submit')

// // function getDataForm(e){
// //     e.preventDefault();

// //     let formData = new FormData(form[0]);

// //     console.log(formData.get("#noun") + " " + formData.get("#adjective")+ " " +formData.get("#person")+ " " +formData.get("#verb")+ " " +formData.get("#place"))

// // }
// // document.addEventListener("DOMContentLoaded",function(){
// //     submitInput.addEventListener("click", getDataForm,false)
// // },false)



