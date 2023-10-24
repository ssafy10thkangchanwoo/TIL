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