let reset = document.querySelector("#reset");
let decrease = document.querySelector("#decrease");
let increase = document.querySelector("#increase");
let display = document.querySelector(".Count");
let count = 0;
display.innerHTML = count;
increase.addEventListener("click",() =>{
    count++;
    display.innerHTML = count;
})
decrease.addEventListener("click",() =>{
    (count>0)?count--:count=0;
    display.innerHTML = count;
})
reset.addEventListener("click",() =>{
    count = 0;
    display.innerHTML = count;
})
