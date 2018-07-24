import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import TheLayout from '@/views/layout/TheLayout' // 布局

import TheIndex from '@/views/index/TheIndex' // 首页
import Article from '@/views/article/TheArticle' // 首页

Vue.use(Router)

const routes = [
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
        path: 'index',
        name: 'index',
        hidden: true,
        component: TheIndex
      },
      {
        path: 'article/:id', // 动态路径参数 以冒号开头
        name: 'article',
        component: Article
      }
    ]
  }

]
// new Router({})

export default new Router({
  routes
})
