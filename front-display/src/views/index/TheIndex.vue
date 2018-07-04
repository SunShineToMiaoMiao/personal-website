<template>
  <div class="index-wrapper">
    <aside>
      <!-- 标签 -->
      <the-left-side></the-left-side>
    </aside>
    <section class="app-section">
      <nav class="article-list-nav">
        <h5>热门</h5>
        <!-- 筛选条件 -->
        <ul class="filter-list">
          <router-link tag="li" to="/" class="filter-item">
            <span class="title">阅读数</span>
          </router-link>
          <router-link tag="li" to="/" class="filter-item">
            <span class="title">评论数</span>
          </router-link>
          <router-link tag="li" to="/" class="filter-item">
            <span class="title">点赞数</span>
          </router-link>
          <router-link tag="li" to="/" class="filter-item">
            <span class="title">发布时间</span>
          </router-link>
          <router-link tag="li" to="/" class="filter-item">
            <span class="title">可下载</span>
          </router-link>
        </ul>
        <!-- 小分辨率下的标签下拉框 -->
        <div class="technical-tags"></div>
      </nav>
      <transition name="fade" mode="out-in">
        <!--<router-view/>-->
        <!--文章列表-->
        <article-list></article-list>
      </transition>
    </section>
  </div>
</template>

<script>
  import ArticleList from '../article-list/ArticleList'
  import TheLeftSide from './left-side/TechnicalNav'

  export default {
    name: 'TheIndex',
    components: {TheLeftSide, ArticleList},
    data () {
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
    .app-section{
      flex-grow: 1;
      text-align: left;
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
        .filter-list {
          @include flex-row(baseline, baseline);
          text-align: right;
          margin-left: auto;

          .filter-item {
            margin: 0 10px;
            cursor: pointer;
            list-style: none;
            span {
              font-size: 14px;
              color: #90979c;
            }
          }
        }
      }
    }
  }

  /*a {*/
    /*color: #42b983;*/
  /*}*/
</style>
