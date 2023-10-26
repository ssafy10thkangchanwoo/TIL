const arr =[]

arr[4] = 4

for (const i in arr) {
    console.log(i)
}

const i = 1

console.log("=================")

for (const i of arr) {
    console.log(i)
}

console.log(arr[7])

//for문은 새로운 변수가 선언된 것이다? -> const는 재선언 불가능? 

const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

rl.on('line',(line) { 
    console.log('input:', line);
    rl.close();
})

rl.on('close', () {
    process.exit();
})