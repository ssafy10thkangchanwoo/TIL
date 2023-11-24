<template>
    <div>
        <h1>게시글 목록</h1>
        <ul>
            <li v-for="article in articles" :key="article.id">
                <RouterLink :to="{ name: 'BoardDetailView', params: { id: article.id } }">
                 {{ article.id }} 
                </RouterLink>
            
            </li>
        </ul>
    </div>
</template>
  
<script setup>
import {onMounted} from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import { useCounterStore } from '../stores/counter';

const store = useCounterStore()

onMounted(() => {
    store.getArticles()
    console.log(store)
})
const articles = store.articles
// console.log(store.articles)


</script>
  
<style  scoped></style>