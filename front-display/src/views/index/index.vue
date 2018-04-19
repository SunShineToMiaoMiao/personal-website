<template>
  <div>
    <!--文章列表-->
    <article-list></article-list>
  </div>
</template>

<script>
  import ArticleList from '../../components/articleList/ArticleList'

  export default {
    name: 'HelloWorld',
    components: {ArticleList},
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
