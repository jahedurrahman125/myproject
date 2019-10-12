let name

if (name === undefined){
    console.log('Please provide a name')
}else{
    console.log(name)
}


//Undefined  for Function arguments
//Undefined  as Function return default value
let greatUser = function(num){
    console.log(num)
}
let result = greatUser()
console.log(result)

// Null as assined value

let age = 27
age = null
console.log(age)