
// async, await
// await키워드는 async 함수 안에서만 사용 가능 
// async함수 안에서 await 키워드를 만나면 async함수는 await한 Promise가 완료(이행 또는 거절)될 때까지 일시정지

const myfunction= async function() {
    console.log('hi')

    await new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log('working..')
            resolve()
        }, 3000)
    })
    console.log('bye')
}
myfunction()