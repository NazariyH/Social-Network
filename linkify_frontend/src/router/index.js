import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import AuthenticationView from '@/views/AuthenticationView.vue'
import InboxView  from '@/views/InboxView.vue'
import StoriesView from '@/views/StoriesView.vue'

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
    },
    {
      path: '/stories/',
      name: 'stories',
      component: StoriesView
    }
  ]
})

export default router
