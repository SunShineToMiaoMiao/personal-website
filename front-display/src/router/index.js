import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
// 布局
import TheLayout from '@/views/layout/TheLayout'
// 首页
import index from '@/views/index/index'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'layout',
      component: TheLayout,
      redirect: '/index',
      hidden: true,
      children: [
        {
          path: 'helloWorld',
          name: 'HelloWorld',
          component: HelloWorld
          // meta: { title: '用户一览', icon: 'table' }
        },
        {
          path: '/index',
          name: 'index',
          component: index
          // meta: { title: '用户分析', icon: 'tree' }
        }
      ]
    }

  ]
})
