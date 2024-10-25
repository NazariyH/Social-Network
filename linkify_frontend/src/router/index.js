import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import AuthenticationView from '@/views/AuthenticationView.vue'
import InboxView  from '@/views/InboxView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/account/authentication/',
      name: 'authentication',
      component: AuthenticationView
    },
    {
      path: '/inbox/',
      name: 'inbox',
      component: InboxView
    }
  ]
})

export default router
