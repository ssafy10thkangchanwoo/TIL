// pinia 구성요소 5가지
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'


export const useCounterStore = defineStore('counter', () => {
  let id = 0
  const todos = ref([
    { id: id++, text: '할 일 1', isDone: false},
    { id: id++, text: '할 일 2', isDone: false}
  ])

  const addTodo = function(todoText) {
    todos.value.push({
      id: id++,
      text: todoText,
      isDOne: false
    })
  }
  
  const deleteTodo = function(todoId) {
    // todos 배열에서 몇번째 인덱스가 삭제되었는가?
    const index = todos.value.findIndex((todo) => todo.id === todoId)
    // 찾은  index값을 통해 원본 배열에서 요소를 제거 후 원본 배열 업데이트
    todos.value.splice(index,1)
  }

  const updateTodo = function() {
    todos.value = todos.value.map((todo) => {
      if (todo.id === todoId) {
        todo.isDone = !todo.isDone
      }
      return todo
    })
  }

  const doneTodoCount = computed(() => {
    return todos.value.filter((todo) => todo.isDone).length
  })
  return {todos, addTodo, deleteTodo, updateTodo, doneTodoCount}
})
// // 1. store: 중앙저장소
// export const useCounterStore = defineStore('counter', () => {
//   // 상태
//   // 2. ref() === state(상태)
//   const count = ref(0)

//   //3. computed() === getters 계산된 값
//   const doubleCount = computed(() => count.value * 2)

//   // 기능
//   // 4. function() === actions Pinia 구성 요소
//   function increment() {
//     count.value++
//   }

//   return { count, doubleCount, increment }
// })

// 기타 추가 모듈 5. plugin