<template>
  <div>
    <!-- 头部 -->
    <header></header>

    <!-- 主内容 -->
    <main>
      <section>
        <!--文章列表-->
        <article></article>
      </section>
      <!-- 右边目录区 -->
      <aside></aside>
    </main>

    <!-- 底部 -->
    <footer></footer>
  </div>
</template>

<script>
export default {
  name: 'Layout',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

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
