<template>
    <div>
        <h1> 메인페이지</h1>
        <div v-if="productIsEmpty" class="product-list">
            <div v-for = "product in products" :key="product.id" class="product-card">
                <!-- {{  product }} -->
                <img :src="product.image" alt="">
                <strong> {{  product.title }}</strong>
                <p>가격 : ${{  product.price }}</p>

                <button @click="getDetail(product)">상세페이지로 이동</button>
                <button @click="addCart(product)">장바구니 추가</button>

            </div>

        </div>
    </div>
</template>

<script setup>
import {ref, computed} from 'vue'
import axios from 'axios'
import {useRouter} from 'vue-router'

const router = useRouter()

const products = ref([])
const storeURL = 'https://fakestoreapi.com/products'

axios.get(storeURL)
.then((response) => {
    // console.log(response)
    products.value = response.data

}).catch((error) => {
    console.error(error)
})

const productIsEmpty = computed(() => {
    return products.value.length > 0 ? true : false 
})

const getDetail = (product) => {
    router.push(`/${product.id}`)
}

const addCart = (product) => {
    localStorage.setItem("cart", JSON.stringfy(product))

}
</script>

<style scoped>
.product-list {
    display : flex;
    flex-wrap: wrap;
    gap: 10px; 

}
.product-card { 
    border : 1px solid black;
    width: 205px;
}
.product-card img {
    width : 200px;
    height : 200px;
    object-fit: fill;

}
</style>
<style>
.product-card { 
    border : 1px solid black;
    width: 205px;
}
</style>