
setTimeout( () => {
    console.log('1물')
    setTimeout(() => {
        console.log('2.면스프')
        setTimeout(()=> {
            console.log('3.계란')
        },1000)
    },2000)
},3000)