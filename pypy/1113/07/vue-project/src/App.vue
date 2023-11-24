<template>
<div>
  <h1> Todo PJT </h1>
  <h2> 완료된 Todo : {{  store.doneTodoCount }}</h2>
  <TodoForm />
  <TodoList />
</div>

 </template>
 



 <script setup>
import TodoForm from '@/components/TodoForm.vue';
import TodoList from '@/components/TodoList.vue';

 import { useCounterStore } from '@/stores/counter';
 
 const store = useCounterStore()
 
 </script>
 
 



 <style scoped>
 
 </style>
 







<!-- <template>
 <div>
  <p>{{  store.count }}</p>
  <p>{{ newNumber }}</p>
  <p> {{  store.doubleCount }}</p>
  <button @click = "store.increment()"> 버튼</button>
 </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()

// store instance로 state에 접근하여 읽고 쓸 수 있음
// 없는 state는 새로 추가할 수 없음
// satae 조작은 actions측에서 해야함.
// store.count = 100 // 이런 식의 접근은 중앙저장소 데이터 오염 우려가 큼

console.log(store.count)



const newNumber = store.count + 1

console.log(store.doubleCount)
</script>


<style scoped>

</style> -->
