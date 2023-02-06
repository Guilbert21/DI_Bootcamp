const form = document.getElementById("my-form")
const radius = document.getElementById("radius")
const volume = document.getElementById("volume")
form.addEventListener("submit", handleSubmit)

function handleSubmit(e){
    e.preventDefault()
    const r = Number(radius.value)
    if (Number.isNaN(r))return
    const v = (4/3)*Math.PI * r ** 3
    volume.value = v.toFixed(2)
}
