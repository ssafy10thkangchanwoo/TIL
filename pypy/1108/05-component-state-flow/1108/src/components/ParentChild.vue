<template>
    <div style = "border:1px solid red;">
        <h1>Parent Child</h1>
        <input type="text" @input="ChangeParentChildData">
        <p>App Data : {{  appData }}</p>
        <ParentGrandChild my-msg="myMsg"/>
        
        <!-- 탬플릿에서 반응형 변수와 같은 방식으로 선언된 props사용
            
        -->
        <p>Parent Data : {{  parentData }} </p>
</div>
</template>

<script setup>
import { ref } from "vue"
import ParentGrandChild from "@/components/ParentGrandChild.vue"

//  부모 컴포넌트에서 보낸 props를 사용하기 위해서는 
//             자식컴포넌트에서 명시적인 props 선언 필요
// defineProps()를 사용하여 props를 선언방식 2개
// 1. 문자열 배열을 이용한 선언
// defineProps(['myMsg'])

// 2. 객체를 이용한 선언 <권장>
// 객체 선언 문법의 각 객체 속성의 key는 props의 이름이 됨
defineProps({
    appData : String,
    parentData : String
})

const emit = defineEmits(['parentChildDataChanged'])
const ChangeParentChildData = function(event) {
    emit('parentChildDataChanged', event.target.value)

}
</script>

<style coped>

</style>