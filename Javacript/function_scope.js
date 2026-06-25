
//Funcion 
function add (num1, num2)
{
    let sum = num1 + num2;
    return sum;
}

console.log(add(1945, 1984));

//Scope 
let globalVar = 'I am a global var'
function printAllVar()
{
    
    let localVar = 'I am a local var'
    console.log(localVar)
    console.log(globalVar)
}

printAllVar()

//console.log(localVar)
console.log(globalVar)


