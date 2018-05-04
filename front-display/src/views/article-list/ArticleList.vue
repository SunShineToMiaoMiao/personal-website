<template>
  <div>
    <article-list-item></article-list-item>
    <hr class="hr">
    <article-list-item></article-list-item>
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
.hr{
  border: 0.5px solid #E9EAEC;
}
</style>
