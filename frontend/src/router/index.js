import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

import problem from '@/components/frontendtest/problem'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/problem-1',
      name: 'Liga de Padel',
      component: problem
    }
  ],
  mode: 'history'
})
