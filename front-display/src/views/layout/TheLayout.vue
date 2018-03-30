<template>
  <div>

    <!--<header class="app-header">
      <Row>
        <i-col :xs="4" :sm="4" :md="6" :lg="8">
          <the-logo/>
        </i-col>
        <i-col :xs="20" :sm="16" :md="12" :lg="8">
          <the-navbar/>
        </i-col>
        <i-col :xs="24" :sm="4" :md="6" :lg="8">
          <search-box/>
        </i-col>
      </Row>
    </header>

    &lt;!&ndash; 主内容 &ndash;&gt;
    <main class="app-main">
      <section class="app-section warp-pagination">
        <transition name="fade" mode="out-in">
          &lt;!&ndash;文章列表&ndash;&gt;
          &lt;!&ndash;<article></article>&ndash;&gt;
          <router-view/>
        </transition>
      </section>
      &lt;!&ndash; 右边目录区 &ndash;&gt;
      <aside></aside>
    </main>

    &lt;!&ndash; 底部 &ndash;&gt;
    <footer></footer>-->

    <!-- 布局 -->
    <Layout>
      <!-- 头部 -->
      <Header class="app-header">
        <Row>
          <i-col :xs="4" :sm="4" :md="6" :lg="8">
            <the-logo/>
          </i-col>
          <i-col :xs="20" :sm="16" :md="12" :lg="8">
            <the-navbar/>
          </i-col>
          <i-col :xs="24" :sm="4" :md="6" :lg="8">
            <search-box/>
          </i-col>
        </Row>
      </Header>
      <!-- 主内容 -->
      <Content class="app-main">
        <section class="app-section warp-pagination">
          <transition name="fade" mode="out-in">
            <!--文章列表-->
            <!--<article></article>-->
            <router-view/>
          </transition>
        </section>
      </Content>
      <!-- 底部 -->
      <Footer>
        Footer
      </Footer>
    </Layout>

  </div>
</template>

<script>
import SearchBox from './header/SearchBox.vue'
import TheNavbar from './header/TheNavbar.vue'
import TheLogo from './header/TheLogo.vue'
import ICol from '../../../node_modules/iview/src/components/grid/col'

export default {
  name: 'TheLayout',
  components: {
    ICol,
    SearchBox,
    TheNavbar,
    TheLogo
  },
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<style scoped>

</style>
