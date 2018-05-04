<template>
  <div class="article-list-item">
    <!-- 标题 -->
    <div>
      <router-link to="/article/one">
        基于vue+element实现的修改密码的单文件组件：changePassword.vue
      </router-link>
    </div>
    <!-- 标签 -->
    <div>
      <Tag checkable color="#41B883">vue</Tag>
      <Tag checkable color="#409EFF">element</Tag>
    </div>
    <!-- 主要信息 -->
    <div>
      <ul>
        <li>127 次阅读</li>
        <li>12 评论</li>
        <li>2 已应用</li>
        <li>2018-04-13 12:03:03</li>
      </ul>
    </div>
    <!--<span>127 次阅读 | 12 评论 | 2 已应用 | 2018-04-13 12:03:03 </span>-->
    <!--127 次阅读 <span>.</span> 12 评论 <span>|</span> 2 已应用 <span>|</span> 2018-04-13 12:03:03-->
  </div>
</template>

<script>
  export default {
    name: 'ArticleListItem'
  }
</script>

<style lang="scss" scoped>
  @import "../../styles/variables";

  .article-list-item {
    padding: 16px;
    div:first-child {
      font-size: 16px;
      a {
        color: black;
      }
      a:hover {
        text-decoration: underline;
        font-weight: 600;
        /*<!--color: $appColor;-->*/
      }
    }
    div:nth-child(2) div{
      font-size: 12px;
    }
    div:last-child {
      font-size: 13px;
      /*span {*/
      /*color: #E9EAEC;*/
      /*}*/
      ul {
        list-style: none;
        display: flex;
        -webkit-box-align: baseline;
        -ms-flex-align: baseline;
        align-items: baseline;
        white-space: nowrap;
      }
      ul > li:not(:last-child):after {
        content: "\B7";
        margin: 0 .4em;
        color: #8f969c;
      }
    }
  }
</style>
