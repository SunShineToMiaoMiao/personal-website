<template>
  <div class="index-wrapper">

    <section class="app-section">
      <nav class="article-list-nav">
        <h5>热门</h5>
        <filter-nav></filter-nav>
        <!-- 筛选条件 -->
        <!--<ul class="filter-list">-->
        <!--<router-link tag="li" to="/" class="filter-item">-->
        <!--<span class="title">阅读数</span>-->
        <!--</router-link>-->
        <!--<router-link tag="li" to="/" class="filter-item">-->
        <!--<span class="title">评论数</span>-->
        <!--</router-link>-->
        <!--<router-link tag="li" to="/" class="filter-item">-->
        <!--<span class="title">点赞数</span>-->
        <!--</router-link>-->
        <!--<router-link tag="li" to="/" class="filter-item">-->
        <!--<span class="title">发布时间</span>-->
        <!--</router-link>-->
        <!--<router-link tag="li" to="/" class="filter-item">-->
        <!--<span class="title">可下载</span>-->
        <!--</router-link>-->
        <!--</ul>-->
        <!--&lt;!&ndash; 小分辨率下的标签下拉框 &ndash;&gt;-->
        <!--<div class="technical-tags">-->
        <!--<Dropdown trigger="click" on-click="onSelectedFilter">-->
        <!--<a href="javascript:void(0)">-->
        <!--筛选-->
        <!--<Icon type="arrow-down-b"></Icon>-->
        <!--</a>-->
        <!--<DropdownMenu slot="list">-->
        <!--<DropdownItem>阅读数</DropdownItem>-->
        <!--<DropdownItem>评论数</DropdownItem>-->
        <!--<DropdownItem>点赞数</DropdownItem>-->
        <!--<DropdownItem>发布时间</DropdownItem>-->
        <!--<DropdownItem>可下载</DropdownItem>-->
        <!--</DropdownMenu>-->
        <!--</Dropdown>-->
        <!--</div>-->
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

  .index-wrapper {
    @include flex-row(flex-start, flex-start);
    margin-top: 1.6rem;
    border-radius: 2px;
    .app-section {
      flex-grow: 1;
      text-align: left;
      background-color: #FFFFFF;
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
    }

    .app-right-aside {
      margin-left: 1.6rem;
      /*background-color: #FFFFFF;*/
    }
  }

  /* 右边侧边栏 start */
  @media screen and (min-width: 980px) {
    .app-right-aside {
      display: block;
    }
  }

  @media screen and (max-width: 979px) {
    .app-right-aside {
        display: none;
    }
  }
  /* 右边侧边栏 end */
</style>
