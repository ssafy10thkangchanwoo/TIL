/*
 라면 == 화면
 라면 재료 준비 == 화면을 보여주는데 필요한 데이터들
 다 완성되면 서빙 == 다 준비되면 화면 보여주기


 promise 객체 사용법
 new Promise((resilve) => {
    if (비동기작업 완료 조건) {
        return resolve(value) // 비동기작업이 성공했을 때 리턴하고 싶은 값이 있으면 value
    } else if (비동기작업 실패 조건) {
        return reject(value) // 비동기작업이 실패했을 때 리턴하고 싶은 값이 있으면 value
    }

    axios()
    .then()과 .catch()는 Promise 객체에 사용하는 메소드
 })
*/
console.log('라면끓이기')


// 물=> 스프, 면 => 게란, 각 과정에는 시간이 걸림

const water = function(ramen) {
    return new Promise((resolve,reject)=> {
        setTimeout(() => {
            console.log('1 물을 끓인다')
            ramen.push('물')
            return resolve(ramen)
        },3000)
    })
}

const soupAndNoddle = function(ramen) {
    return new Promise((resolve,reject)=> {
        setTimeout(() => {
            console.log('2 스프와 면')
            ramen.push('스프')
            ramen.push('면')
            return resolve(ramen)
        },2000)
    })
}

const egg = function(ramen) {
    return new Promise((resolve,reject)=> {
        setTimeout(() => {
            console.log('3egg')
            ramen.push('egg')
            return resolve(ramen)
        },1000)
    })
}

const ramen = []

water(ramen)
.then((ramen) => {
    return soupAndNoddle(ramen)
})
.then((ramen) => {
    return egg(ramen) })
.then((ramen) => { 
    console.log('라면 완성 ', ramen) 
}) 
.catch(error => {
    console.log('라면 에러 ' , err)
})



setTimeout( () => {
    console.log('1. 물을 끓인다.')
}, 3000)

// 스프랑 면을 2초 

setTimeout( () => {
    console.log('2. 스프 면 넣는다.')
}, 2000)

//계란 1
setTimeout( () => {
    console.log('3. 계란.')
}, 1000)

console.log('라면 완성') 