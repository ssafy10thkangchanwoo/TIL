<template>
  <div class="main d-flex justify-content-center flex-wrap">
    <div class="header">
      <div class="header-title d-flex align-items-center justify-content-center">
        <h1 class="fw-bold">Quiz 퀴즈</h1>
      </div>
      <div class="header-desc d-flex justify-content-center align-items-center">
        <div>
          여기는 퀴즈의 나라! 놀라운 퀴즈들이 기다리고 있어요. 지금 바로 도전해보세요!
        </div>
      </div>
    </div>
    <nav class="mt-4 d-flex justify-content-center align-items-center">
      <RouterLink :to="{ name: 'home' }">Home</RouterLink> |
      <RouterLink :to="{ name: 'quiz' }">Quiz</RouterLink> |
    </nav>

  </div>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'


</script>

<style scoped>
.main {
  width: 80%;
  margin: 0 auto;
  padding: 30px 0;
  background-color: gainsboro;
}

nav > a {
  margin:0 20px;
  color: white;
  text-decoration: none;
}

nav > a:hover {
  color: red;
}

.header {
  width: 80%;
  text-align: center;
}

nav {
  width: 80%;
  height: 50px;
  background-color: black;
  color: white;
}

.header-title {
  height: 100px;
  border: 1px solid gray;
  border-bottom: 0px;
  border-radius: 10px 10px 0 0;
  background-color: orange;
  color: white;
}

.header-desc {
  background-color: white;
  height: 150px;
  border: 1px solid gray;
  border-radius: 0 0 10px 10px;
}
</style>