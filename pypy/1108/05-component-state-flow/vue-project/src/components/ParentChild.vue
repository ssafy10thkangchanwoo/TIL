<template>
    <div>
        {{ myMsg }}
        {{ dynamicProps }}
        <!-- 선언 및 참조할때는 CamelCase-->
        <ParentGrandChild 
        :my-msg="myMsg" 
        @update-name = "updateName"
        />
     <!-- 동적으로 처리되어야 함 -->
     <!-- <button @click=$emit('someEvent')">클릭</button> 왜안되지 -->
    <button @click="buttonClick">클릭</button>
    <button @click="emitARgs">추가인자전달</button>

    </div>
</template>

<script setup>

defineProps({
    MyMsg: {
    type:String, 
    required: true,
    // validator(value){
    //     // 기본적으로 콘솔에 원인출력
    //     return ['success', 'warning', 'danger'].includes(value)
    // }
    validator(value){
        const validValues = ['success', 'warning', 'danger']
        if (!validValues.includes(value)){
        console.error('에러입니다.')
        return false }

        return true
    }
    
}})
// import ParentGrandChild from '@/components.ParentGrandChild.vue'
// defineProps(['myMsg'])

// defineProps({
//     myMsg: String, 
    
//     // 유효성검사
//     // myMsg: {
//     //     type: String, 
//     //     required: true,
//     // }
// })
// props 데이터를 script에서 사용하려면 
const props = defineProps({
    myMsg: String, 
    dynamicProps: String,
})
console.log(props)

// emit 선언 방식
const emit = defineEmits(['someEvent', 'emitARgs'])

const buttonClick = function() {
    emit('someEvent')
}

const emitARgs = function() {
    emit('emitArgs', 1,2,3)
}

const updateName = function () {
    emit('updateName')
}
</script>


<style scoped>

</style>