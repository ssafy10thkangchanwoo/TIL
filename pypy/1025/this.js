
    // // 1.1 단순 호출
    // const myFunc = function () {
    //   return this
    // }
    // console.log(myFunc()) // window

    // // 1.2 메서드 호출
    // const myObj = {
    //   data: 1,
    //   myFunc: function () {
    //     return this
    //   }
    // }
    // console.log(myObj.myFunc()) // myObj

    // // 2. Nested
    // // 2.1 일반 함수
    // const myObj2 = {
    //   numbers: [1, 2, 3],
    //   myFunc: function () {
    //     this.numbers.forEach(function (number) {
    //       console.log(this) // window
    //     })
    //   }
    // }
    // console.log(myObj2.myFunc())

    // // 2.2 화살표 함수
    // const myObj3 = {
    //   numbers: [1, 2, 3],
    //   myFunc: function () {
    //     this.numbers.forEach((number) => {
    //       console.log(this) // myObj3
    //     })
    //   }
    // }
    // console.log(myObj3.myFunc())

    // 객체의 메소드에서는 화살표 함수 사용 ㄴ 
    const myObj4 = {
        numbers: [1, 2, 3],
        myFunc: () => {
         
            console.log(this) // myObj3
          }}
        
      
    myObj4.myFunc()
