import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import BoardView from '../views/BoardView.vue'
import BoardDetailView from '../views/BoardDetailView.vue'
import DepositView from '../views/DepositView.vue'
import ExchangeRateCalView from '../views/ExchangeRateCalView.vue'
import MapView from '../views/MapView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomeView',
      component: HomeView
    },
    {
      path: '/board',
      name: 'BoardView',
      component: BoardView
    },
    {
      path: '/boarddetail/',
      name: 'BoardDetailView',
      component: BoardDetailView
    },
    {
      path: '/deposit',
      name: 'DepositView',
      component: DepositView
    },
    {
      path: '/exchange',
      name: 'ExchangeRateCalView',
      component: ExchangeRateCalView
    },
    {
      path: '/map',
      name: 'MapView',
      component: MapView
    },
  ]
})

export default router
