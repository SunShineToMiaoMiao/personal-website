<template>
  <div>
    <Layout>
      <aside>
        <!-- 标签 -->
        <Sider hide-trigger>
          <the-left-side></the-left-side>
        </Sider>
      </aside>
      <Content>
        <section class="app-section warp-pagination">
          <Card class="app-card" title="热门" padding="0">
            <ul slot="extra" class="filter-list">
              <li class="filter-item">
                <span class="title">阅读数</span>
              </li>
              <li class="filter-item">
                <span class="title">评论数</span>
              </li>
              <li class="filter-item">
                <span class="title">点赞数</span>
              </li>
              <li class="filter-item">
                <span class="title">发布时间</span>
              </li>
              <li class="filter-item">
                <span class="title">可下载</span>
              </li>
            </ul>
            <transition name="fade" mode="out-in">
              <!--<router-view/>-->
              <!--文章列表-->
              <article-list></article-list>
            </transition>
          </Card>
        </section>
      </Content>
    </Layout>
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
<style scoped>
  h1, h2 {
    font-weight: normal;
  }

  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    display: inline-block;
    margin: 0 10px;
  }

  a {
    color: #42b983;
  }
</style>
