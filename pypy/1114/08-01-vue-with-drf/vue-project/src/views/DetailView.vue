<template>
  <div>
    <h1>Detail</h1>
    <div v-if="article"> 
    <p>글 번호 : {{  article.id }}</p>
      <p>제목 : {{  article.title }}</p>
  </div>

  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue';
import { useCounterStore } from '../stores/counter';
import { useRoute } from 'vue-router'; 

const store = useCounterStore()
const route = useRoute()

const article = ref({})

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`
  })
    .then((res) => {
      // console.log(res.data)
      article.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
})


</script>

<style>

</style>
