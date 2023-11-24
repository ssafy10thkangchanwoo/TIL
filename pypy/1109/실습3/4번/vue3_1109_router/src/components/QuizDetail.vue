<template>
  <div class="quiz-detail w-100 p-3 mb-3">
    <h4>{{ quiz.pk }}번 문제 : {{ quiz.question }}</h4>
    <label :for="'quiz-' + quiz.pk" class="form-label">정답 입력</label>
    <input type="text" :id="'quiz-' + quiz.pk" class="form-control border border-secondary" @input="inputAnswer" @keyup.enter="submitAnwer">
  </div>
</template>

<script setup>
import { ref } from 'vue'
import {useRouter} 


const userAnswer = ref("")

const inputAnswer = function (event) {
  userAnswer.value = event.target.value
}

const submitAnwer = function() {

}
</script>

<style scoped>
.quiz-detail {
  background-color: lightgray;
  border: 1px solid gray;
  border-radius: 10px;
  box-shadow: 5px 5px 5px lightslategray;
}
</style>