import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import AuthenticationView from '@/views/AuthenticationView.vue'
import InboxView  from '@/views/InboxView.vue'
import StoriesView from '@/views/StoriesView.vue'
import StoreView from '@/views/StoreView.vue'
import ProfileView from '@/views/ProfileView.vue'
import NotFoundView from '@/views/NotFoundView.vue'
import PostDetailView from '@/views/PostDetailView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/post/:id/',
      name: 'post-detail',
      component: PostDetailView
    },
    {
      path: '/account/authentication/',
      name: 'authentication',
      component: AuthenticationView
    },
    {
      path: '/account/profile/:id/',
      name: 'profile',
      component: ProfileView
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
    },
    {
      path: '/store/',
      name: 'store',
      component: StoreView
    },
    {
      path: '/:catchAll(.*)',
      name: 'NotFound',
      component: NotFoundView
    }
  ]
})

export default router
