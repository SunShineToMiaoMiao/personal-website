<template>
  <div class="container main-container">

    <section class="app-section">
      <nav class="article-list-nav">
        <h5>热门</h5>
        <!-- 筛选条件 -->
        <filter-nav></filter-nav>
      </nav>
      <transition name="fade" mode="out-in">
        <!--<router-view/>-->
        <!--文章列表-->
        <article-list></article-list>
      </transition>
    </section>

    <aside class="app-right-aside">
      <sidebar-box>
        <!-- 标签 -->
        <technical-nav></technical-nav>
      </sidebar-box>
    </aside>
  </div>
</template>

<script>
  import ArticleList from '../article-list/ArticleList'
  import FilterNav from './FilterNav'
  import SidebarBox from '../../components/SidebarBox'
  import TechnicalNav from './left-side/TechnicalNav'

  export default {
    name: 'TheIndex',
    components: {TechnicalNav, SidebarBox, FilterNav, ArticleList},
    data() {
      return {
        msg: 'Welcome to Your Vue.js App'
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style rel="stylesheet/scss" lang="scss" scoped>
  @import "../../styles/variables";
  @import "../../styles/mixin";

  .article-list-nav {
    @include flex-row(space-between);
    background-color: #fff;
    padding: 0.5rem 1rem;
    border-bottom: 1px solid #f6f6f6;
    h5 {
      margin: 0;
      font-size: 16px;
      font-weight: 500;
    }
  }
</style>
