<template>
  <div class="article">
    <operation-panel></operation-panel>

    <h1>基于vue+element实现的修改密码的单文件组件：changePassword.vue</h1>
    <div class="type-tag-time flex-row-center">
      <label>原创</label>
      <Tag checkable color="#41B883">vue</Tag>
      <Tag checkable color="#409EFF">element</Tag>
      <time>2018-03-22</time>
    </div>
    <hr class="hr">
  </div>
</template>

<script>
  import OperationPanel from './left-side/OperationPanel'

  export default {
    name: 'article',
    components: {OperationPanel},
    beforeRouteUpdate (to, from, next) {
      // react to route changes...
      // don't forget to call next()
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../styles/variables";

  .article {
    text-align: left;
    h1 {
      font-size: 24px;
      font-weight: 500;
      height: 42px;
    }
    .type-tag-time {
      label {
        color: $appColor;
        border: solid 1px;
        padding: 0 10px;
        border-radius: 5px;
        margin-right: 5px;
      }
    }
    hr{
      margin: 20px 0;
    }
  }

</style>
