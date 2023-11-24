<template>
  <div style="border: 1px solid black;">
    <h1>App</h1>
    <!-- input이벤트가 발생하면 changeAppData 함수를 실행시킨다. -->
    <input type="text" @input="changeAppData">
    <p>Parent Data : {{ parentData }}</p>
    <p>Parent Child Data : {{ parentChildData }}</p>
    <Parent 
    :app-data="appData"
    @parent-data-changed="onParentDataChanged"
    @parent-child-data-changed="onParentChildDataChanged"
    />
    <!-- 부모 컴포넌트에서 수신시 케밥케이스 -->
  </div>
</template>




<script setup>
// 자식컴포넌트
import Parent from "@/components/Parent.vue"
import {ref} from 'vue'

//동기적데이터인 appData의 value값을 현재 input값으로 할당한다.



// 동기적 데이터 
const appData = ref("")
const parentData = ref("")
const parentChildData = ref("")


const changeAppData = function(event) {
  appData.value = event.target.value
}

const onParentDataChanged = function(data) {
  parentData.value = data
}

const onParentChildDataChanged = function(data) {
  parentChildData.value = data
}

</script>

<style scoped>
* {
  text-align: center;
}
</style>