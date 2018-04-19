<template>
  <div>
    <article-list-item></article-list-item>
    <hr class="article-hr">
    <article-list-item></article-list-item>
    asdfffffffffffffffff
  </div>
</template>

<script>
  import ArticleListItem from './ArticleListItem'

  export default {
    name: 'ArticleList',
    components: {ArticleListItem}
  }
</script>

<style scoped>
.article-hr{
  border: 0.5px solid #E9EAEC;
}
</style>
