// let name = "Vadapav"
// let greeting = "Hi there"
// document.getElementById("count").innerText = 5

// let firstBatch = 5
// let secondBatch = 7
// let count = firstBatch + secondBatch
// console.log(count)

// let myAge=19
// let humanDogRatio=7 
// let myDogAge= myAge*humanDogRatio
// console.log(myDogAge)


// let bonusPoints=50
// console.log(bonusPoints)
// bonusPoints+=50
// console.log(bonusPoints)
// bonusPoints-=75
// console.log(bonusPoints)
// bonusPoints+=45
// console.log(bonusPoints)

// Setting up the the race
// function countdown(){console.log(5)
//     console.log(4)
//     console.log(3)
//     console.log(2)
//     console.log(1)
//     }
// // GO
// countdown()
// Players are running the race 
// Race is finished


// function fourtwo(){
//     console.log(42)

// }
// fourtwo()

// let lap1=34
// let lap2=33
// let lap3=36
// function totallap(){
//     console.log(lap1+lap2+lap3)
// }
// totallap()



// let lapsCompleted=0

// function increment(){
//     lapsCompleted=lapsCompleted+1
//     console.log(lapsCompleted)
// }
// increment()
// increment()
// increment()




// intialize the count as 0
let count=0

// listen for clicks on the increment button
let countEl= document.getElementById("count-el")
let saveEl=document.getElementById("save-el")


console.log(saveEl)
// increment the count variable when the button is clicked 
function increment(){
    count=count+1
    countEl.textContent=count
}
// change the count-el in the HTML to reflect the new count

function save(){
    let pre= count + " - "
    saveEl.textContent+= pre
    countEl.textContent=0
    count=0
}




