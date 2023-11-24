import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserView from '@/views/UserView.vue'
import LoginView from '@/views/LoginView.vue'
// 컴포넌트만들고, 라우트 등록해주고, 거기에 이동할 라우트 링크 작서앟고

const isAuthenticated = true
 
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  // url과 컴포넌트를 매핑, django의 url와 유사한 기능을 하는 듯
  routes: [
    {
      path: '/',
      // path: App.vue에서 RouterLink 들어감
      name: 'home',
      // Named Routes 경로에 이름을 지정하는 라우팅

      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
                            //콜백함수형태?
    },
    {
      // :변수명
      path: '/user/:id',
      name: 'user',
      component: UserView,
      // 다른 라우터에서 user라우터에 들어갈 때만 발동
      beforeEnter: (to, from) => {
        console.log(to) 
        console.log(from)
      }
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      beforeEnter: (to, from) => {
        if (isAuthenticated === true) {
          console.log('이미 로그인되어 있습니다.')
          return { name : 'home' }
        }
      }
    }
  ]
})

// router.beforeEach((to, from) => {
//   console.log(to)
//   console.log(from) 
// })

// 전역가드
// router.beforeEach((to, from) => {
//   const isAuthenticated = false
//   // 비로그인 사용자라면
//   if (!isAuthenticated && to.name !== 'login') {
//     console.log('로그인이 필요합니다')
//     return { name : 'login' }
//   }
// })

export default router
