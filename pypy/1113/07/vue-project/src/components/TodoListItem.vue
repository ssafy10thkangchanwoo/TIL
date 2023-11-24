<template>
    <div>
        <!-- {{  todoData }} -->
        <span @click="store.updateTodo(todoData.id)" 
        ></span>
       <span> {{  todoData.text }}</span>
       <button @click="store.deleteTOdo(todoData.id)"></button>
    </div>
</template>

<script setup>

import { useCounterStore } from '@/stores/counter';
defineProps({
    todoData: Object
})

</script>

<style scoped>

</style>