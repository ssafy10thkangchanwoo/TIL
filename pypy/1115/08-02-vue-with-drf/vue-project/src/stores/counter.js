import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false 
    } else {
      return true 
    }
  })

  // DRF에 article 조회 요청을 보내는 action
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      // 인증과 권한이 필요한 요청에 헤더스를 붙여줘야 한다
      headers: {
        Authrization: `Token ${token.value}`
      }
    })
      .then((res) =>{
        // console.log(res)
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const signUp = function(payload) {
    // 잡기술 : 구조분해할당으로 단축속성활용
    const { username, password1, password2 } = payload
    axios({
      method : 'post', 
      url: `${API_URL}/accounts/signup/`,
      // data: {
      //   username: payload.username,
      //   password1:payload.password1,
      //   password2:payload.password2,
      // }
      data: {
        username, password1, password2
      }
    })
    .then((res) => {
      console.log(res)
    })
    .catch((err) => {
      console.log(err)
    })
  }

  const logIn = function(payload) {
    const { username, password } = payload
    axios({
      method : 'post', 
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
    .then((res) => {
      token.value = res.data.key
      console.log(res.data)
    })
    .catch((err) => {
      console.log(err)
    })
  }
  return { articles, API_URL, getArticles, signUp, logIn, token, isLogin }
}, { persist: true })
