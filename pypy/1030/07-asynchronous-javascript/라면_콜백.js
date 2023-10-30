
setTimeout( () => {
    console.log('1물')
    settimeout(() => {
        console.log('2.면스프')
        settimeout(()=> {
            console.log('3.계란')
        },1000)
    },2000)
},3000)