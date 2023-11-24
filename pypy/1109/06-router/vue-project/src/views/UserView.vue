<template>
    <div>
<h1> UserView </h1>
<!--  전역속성 route 바로 쓸 수 있음
    $는 vue에 기본적으로 내장되어 있는 메서드, 속성 쓸 수 있음.
    $속성은 vue템플릿에서 사용하는 것. js에서는 사용 불가능
    route속성은 객체로 나왔다
    

-->
<h2>{{  $route.params.id }} 유저의 페이지입니다.</h2>
<h2>{{userId}}번 유저의 페이지입니다.</h2>

<!-- 
{{  $route.params.id }} 
    
    js로 작성한 반응형변수  / 간접적으로 접근
    첫번째 $route.params.id는 직접적으로 접근
현재라우터에서 똑같은 컴포넌트가 재랜더링될 때 
-->

<button @click="goHome">홈으로</button>
<button @click="goAnotherUser">100번유저페이지로</button>
    </div>
</template>

<script setup>
import { useRoute, useRouter, onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router'
// js에서는 import 해야 사용 가능

import {ref} from 'vue'

// vue의 입장에서 하나의 라우트를 계속 그대로 쓰고 있다.
const route = useRoute()


const userId = ref(route.params.id)

// 프로그래밍 방식 네비게이션
const router = useRouter()
const goHome = function() {
    // router.push('/')  아래와 동일
    //push와 route 둘 다 해당 주소로 이동하지만 push는 뒤로가기 가능, 
    // replace는 불가능
    router.push({ name : 'home'})   // 기존의 위치를 history stack에 push 함. 뒤로가기함.
    router.replace({ name: 'home' }) //위치만 바꾸고 기존의 위치를 history stack에 push 하지 않음, ex)로그인 후 
}

// in-component Guard 
// 1. onBeforeRouteLeave
onBeforeRouteLeave((to, from) => {
   const answer = window.confirm('가지마') //팝업창 출력
   if (answer === false) {
    return false 
   }


})

// 2. onBeforeRouteUpdate 
const goAnotherUser = function() {
    router.push({ name : 'user', params : {id:100} })
}

onBeforeRouteUpdate((to, from)=> {
    userId.value = to.params.id
})
 
</script>

<style scoped>

</style>