<template>
  <div>
  <span @click="store.updateTodo(todo.id)" :class="{'is-done': todo.isDone}">
    {{ todo.text }}</span>
  <!-- Todo의 아이디를 삭제한다??? 함수를 발동한다.-->
  <button @click="store.deleteTodo(todo.id)">Delete</button>
  </div>
</template>

<script setup>
import { useCounterStore } from '../stores/counter';
defineProps({
  todo:Object
})

const store = useCounterStore()

</script>

<style scoped>
.is-done {
  text-decoration: line-through;
}

</style>
