<template>
    <div style="border: 1px solid blue;">
    <h1>Parent</h1>
    <input type="text" @input="changeParentData">

    <p>App Data : {{ appData }} </p>
    <p>Parent Child Data : {{ parentChildData }}</p>


    <ParentChild :app-data="appData"
     :parent-data="parentData"
      @some-event="someCallback"
      @emit-args="getNumbers"
      @parent-child-data-changed="onParentChildDataChanged"
      />
    </div>
  </template>
  
  <script setup>
// 자식컴포넌트설정
import ParentChild from "@/components/ParentChild.vue"
import { ref } from "vue"

defineProps({
    appData : String
})

const parentData = ref("")
const parentChildData = ref("")

const emit = defineEmits(["parentDataChanged", "parentChildDataChanged"])
const changeParentData = function(event) {
  parentData.value = event.target.value
  emit("parentDataChanged", parentData.value)
}

const onParentChildDataChanged = function (data) {
    // console.log(data) event.target.value를 ParentChild에서 인자로 받아옴  
  parentChildData.value = data 
  emit("parentChildDataChanged", data)
}



const someCallback = function() {
    console.log('parentchild이벤트수신')
}

const getNumbers = function (...args) {
    console.log(args)
    console.log(`이걸 얻었다 ${args}`)
}
  </script>
  
  <style scoped>
  
  </style>