let num1 = 4;
let num2 = 5;
document.getElementById("num1-el").textContent = num1;
document.getElementById("num2-el").textContent = num2;

let sumEl = document.getElementById("sum-el");

function add() {
    let result = num1 + num2;
    sumEl.textContent = "Sum: " + result;
}

function sub() {
    let result = num1 - num2;
    sumEl.textContent = "Sum: " + result;
}

function divi() {
    let result = num1 / num2;
    sumEl.textContent = "Sum: " + result;
}

function mul() {
    let result = num1 * num2;
    sumEl.textContent = "Sum: " + result;
}
