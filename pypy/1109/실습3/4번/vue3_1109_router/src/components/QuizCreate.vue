<template>
  <div class="quiz-create my-3 p-3 border border-secondary">
    <h2>퀴즈 생성</h2>
    <form @submit.prevent="createQuiz">
      <div class="mb-3">
        <label for="question" class="form-label">문제</label>
        <textarea class="form-control border border-secondary" id="question" rows="3" @input="inputQuestion" :value="question" ></textarea>
      </div>
      <div class="mb-3">
        <label for="answer" class="form-label">답안</label>
        <input type="text" id="answer" class="form-control border border-secondary" @input="inputAnswer" :value="answer">
      </div>
      <div class="d-grid gap-1">
        <button class="btn btn-primary">퀴즈 생성</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import {ref} from "vue"

const question = ref("")
const answer = ref("")

const inputQuestion = function(event) {
  question.value = event.target.value
}

const inputAnswer = function(event) {
  answer.value = event.target.value
}

const emit = defineEmits(["createQuiz"])

const createQuiz = function() {
  const newQuiz = {
    pk : 0,
    question: question.value,
    answer: answer.value
  }

  emit("createQuiz", newQuiz)
  question.value = ""
  answer.value = ""
}

</script>

<style scoped>
.quiz-create {
  background-color: lightgray;
  width: 70%;
  border-radius: 10px;
  margin: 0 auto;
}
</style>