<template>
  <div class="quiz-list">
    <QuizCreate @create-quiz="updateQuiz" />
    <QuizDetail v-for="quiz in sortedQuizList" :quiz="quiz" />
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import QuizDetail from '../components/QuizDetail.vue'
import QuizCreate from '../components/QuizCreate.vue'

let pk = 1

const quizList = ref([
  {
    pk: pk++,
    question: 'Python 웹 프레임워크 중 하나로, 마이크로 웹 프레임워크로 빠른 개발을 지원하는 것은?',
    answer: 'flask'
  },
  {
    pk: pk++,
    question: 'HTML에서 텍스트 입력란을 만드는 데 사용되는 요소는?',
    answer: 'input'
  },
  {
    pk: pk++,
    question: '웹 애플리케이션에서 클라이언트의 데이터를 서버로 전송할 때 주로 사용되는 HTTP메서드는?',
    answer: 'post'
  },
  {
    pk: pk++,
    question: 'Python의 가상 환경을 만들어 프로젝트 별로 라이브러리 의존성을 격리시키는 명령어는?',
    answer: 'virtualenv'
  },
  {
    pk: pk++,
    question: '웹 애플리케이션을 개발할 때, 사용자의 브라우저에 보여지는 부분을 렌더링하는 언어는 무엇인가요?',
    answer: 'html'
  },
])
const updateQuiz = function (newQuiz) {
  newQuiz.pk = quizList.value.length + 1
  quizList.value.push(newQuiz)
}

const sortedQuizList = computed(() => {
  // toSorted는 새로운 배열을 생성(원본 배열을 수정하지 않는다)
  return quizList.value.toSorted((a, b) => b.pk - a.pk)
})


</script>

<style scoped>
.quiz-list {
  width: 90%;
  margin: 20px auto;
}
</style>