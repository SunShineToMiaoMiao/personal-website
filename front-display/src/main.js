// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import '@/styles/index.scss' // global css
// 引入iview
import iView from 'iview'
import 'iview/dist/styles/iview.css'
// 导入主题颜色
import './my-theme/index.less'
// SvgIcon
import SvgIcon from '@/components/SvgIcon'
// 引入highlight
import Highlight from '@/directives/highlight'

Vue.config.productionTip = false
Vue.use(iView)
Vue.use(Highlight)
Vue.component('svg-icon', SvgIcon)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
