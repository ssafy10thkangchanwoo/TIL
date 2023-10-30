

console.log('라면끓이기')


// 물=> 스프, 면 => 게란, 각 과정에는 시간이 걸림


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