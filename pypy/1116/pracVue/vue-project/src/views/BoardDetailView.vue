<template>
    <div>
      <h1>Detail</h1>
      
    </div>
  </template>
  
  <script setup>
  import axios from 'axios'
  import { onMounted, ref } from 'vue'
  import { useCounterStore } from '@/stores/counter'
  import { useRoute } from 'vue-router'
  
  const store = useCounterStore()
  const route = useRoute()
  const article = ref(null)
  
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
  