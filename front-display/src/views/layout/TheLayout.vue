<template>
  <div class="app-container">
    <!-- 布局 -->
    <!-- 头部 -->
    <div class="header-wrapper">
      <header class="app-header">
        <div class="header-container container">
          <!-- logo -->
          <the-logo/>
          <nav>
            <!-- 一级菜单 -->
            <the-navbar/>
            <div class="header-operation">
              <!-- 搜索框 -->
              <search-box/>
              <!-- 登录按钮 -->
              <login-or-register></login-or-register>
            </div>
          </nav>
        </div>
      </header>
    </div>
    <!-- 主内容 -->
    <main class="app-main">
      <!--<Layout>-->
      <transition name="fade" mode="out-in">
        <!--<div class="container">-->
          <router-view/>
        <!--</div>-->
      </transition>
      <!--</Layout>-->
    </main>
    <!-- 底部 -->
    <footer class="app-footer">
      <Footer>
        Footer
      </Footer>
    </footer>
  </div>
</template>

<script>
  import SearchBox from './header/SearchBox.vue'
  import TheNavbar from './header/TheNavbar.vue'
  import TheLogo from './header/TheLogo.vue'
  import LoginOrRegister from '../user/LoginOrRegister'

  // import ICol from '../../../node_modules/iview/src/components/grid/col'

  export default {
    name: 'TheLayout',
    components: {
      LoginOrRegister,
      SearchBox,
      TheNavbar,
      TheLogo
    },
    data() {
      return {
        msg: 'Welcome to Your Vue.js App'
      }
    }
  }
</script>

<style lang="scss" scoped>


</style>
