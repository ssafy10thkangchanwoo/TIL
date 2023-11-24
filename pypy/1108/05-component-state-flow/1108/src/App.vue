<template>
  <div style = "border:1px solid black;">
    <h1>App</h1>
    <input type="text" @input="changeAppData">
    <p>Parent Data: </p>
    <p>Parent Child Data: </p>
    <!-- 자식 컴포넌트 -->
    <!-- appData를 보낸다.
    <Parent :prop이름 : "prop값" /> 
    :app-data="appData"를 props로 보낼 건데 appData가 동적으로 변함에 따라서
    Parent는 다른 데이터를 받겠지 그리고 parent-data-changed 
            -->
    <Parent :app-data="appData" @parent-data-changed="onParentDataChanged"/>
  </div>
</template>

<script setup>
import Parent from "@/components/Parent.vue"
import { ref } from 'vue'
const appData = ref('')
const parentData = ref('')
const parentChilddata = ref('')
const changeAppData = function(event) {
  appData.value = event.target.value
}

const onParentDataChanged = function(data) {
  parentData.value = data
}


</script>

<style scoped>

</style>