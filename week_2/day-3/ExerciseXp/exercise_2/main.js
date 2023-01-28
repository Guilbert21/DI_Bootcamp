// Create an array called colors where the value is a list of your five favorite colors.
const color = ["black", "blue", "grey", "purple", "white"]

// Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .
for (let i = 0; i < color.length; i++) {
    console.log(`My #${i + 1} choice is ${color[i]}`)
}

// Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the correct suffix for each number.
// didn't got it