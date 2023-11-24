<template>
    <div style="border: 1px solid red;">
        <h1>Parent Child</h1>
    <input type="text" @input="changeParentChildData">

    <p>App Data : {{ appData }}</p>
    <p>Parent Data : {{ parentData }}</p>

        <!-- 클락하면 someEvent를 emit 하면 Parent가 알아챈다 -->
        <!-- 여기서 someEvent는 그냥 변수명? -->
        <button @click="$emit('someEvent')">클릭</button>

        <!-- 클릭하면 buttonClick 함수가 실행된다. 이 함수는 someEvent를 emit한다.. -->
        <!-- script에서는 $emit접근할 수 없다..라? -->
        <button @click="buttonClick">클릭</button>

        <button @click="emitArgs">N클릭</button>


    </div>
  </template>
  
  <script setup>

defineProps({
    appData : String,
    parentData : {
        type : String,
        required : true,
        default : 'good' }
})

// emit 이벤트 선언 
// defineEmit()를 사용하면 명시적으로 발신한 이벤트를 선언할 수 있음
// emit 대신 사용할 수 있는 동등한 함수를 반환 @click="$emit('someEvent')" 이거 대신 정도인 듯?

const emit = defineEmits(
    ['someEvent', 'emitArgs', 'parentChildDataChanged'])


    // 입력이 발생하면 발생하는 함수 
    // parentChildDataChanged 라는 이벤트인자와 input.value의 이벤트인자가 emit됨
    // emit( eventname, args..) 

    const changeParentChildData = function(event) {
  emit("parentChildDataChanged", event.target.value)
}




const buttonClick=function() {
    emit('someEvent')
}
const emitArgs = function() {
    // 이벤트인자
    emit('emitArgs', 1, 2, 3)
}
  </script>
  
  <style scoped>
  
  </style>