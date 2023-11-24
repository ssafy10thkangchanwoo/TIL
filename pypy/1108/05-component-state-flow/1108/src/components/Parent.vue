<template>

    <div style = "border:1px solid blue;">
        <h1>Parent</h1>
        <input type="text" @input="changeParentData">
        <p>App Data : {{  appData  }}</p>
        <p>Parent Child Data {{   }}</p>
        <ParentChild :app-data="appData"
         :parent-data="parentData" 
         @parent-child-data-changed="onParentDataChanged"/>

         
         
        <!-- 
            Props: 부모 컴포넌트에서 자식 컴포넌트로 데이터를 저장하는데 사용되는 속성
            부모 컴포넌트에서 보낸 props를 사용하기 위해서는 
            자식컴포넌트에서 명시적인 props 선언 필요

            Parent에서 ParentChild에 보낼 Props 작성 
            <ParentChild prop이름 : "prop값" /> 

            선언 및 템플릿 참조 시 camelCase
            자식컴포넌트로 전달 시 kebab-case, html표기법특성상

         -->
    </div>
</template>
<!-- 
 -->

<script setup>
import ParentChild from "@/components/ParentChild.vue"
import { ref } from "vue"
defineProps({
    addData : String
})


// emit 이벤트 선언
// defineEmits()를 사용하여 명시적으로 발신할 이벤트 선언 가능 
// script에서 $emit 메서드를 접근할 수 없기 때문에 defineEmits()는 
// $emit 대신 사용할 수 있는 동등한 함수를 반환
// parentDataChanged함수반환
const emit = defineEmits(["parentDataChanged"])

const parentData = ref('')
const parentChildData = ref('')

// event.target.value를 parentData.value로 하고
//emit
const changeParentData = function(event) {
    parentData.value = event.target.value
    emit("parentDataChanged", parentData.value)
}

const onParentDataChanged = function(data) {
    parentChildData.value = data
    emit('parentChildDataChanged', data)
}
</script>

<style coped>

</style>