const num = 50
// let stars = ""
// for (let x = 0; x < num; x++) {
//     stars = stars + " * " 
//     console.log(stars)
// }

for (let x = 0;x < num; x++) {
    const stars = x + 1;
    let starsLine = ""
    for (let y = 0; y < stars; y++) {
        starsLine = starsLine + " * "
}
 console.log(starsLine)
}