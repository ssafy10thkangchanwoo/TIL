<template>
    <div class="quiz-create m-3 p-3">
        <h2>퀴즈생성</h2>
        <form>
    <label for="question" class="form-label">문제</label>
    <textarea> type="text" id = 'answer' class="form-control border border-secondary" @input="inputAnswer"></textarea>

    <label for="answer" class="form-label">답안</label>
    <input type="text" id = 'answer' class="form-control border border-secondary" @input="inputAnswer">
        <div class="d-grid gap-1">
            <button>퀴즈 생성 </button>
        </div>
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue'

const question = ref('')
const answer = ref('')

const inputQuestion = function(event) {
    question.value = event.target.value
}

const inputAnswer = function(event) {
    answer.value = event.target.value 
}

const emit = defineEmits(["createQuiz"])
const createQuiz = function() {
    const createQuiz = {
        pk : 0,
        question : question. value, 
        answer : answer.value
    }
    emit('createQuiz', newQuiz)
    question.value
}
</script>

<style scoped>

</style>