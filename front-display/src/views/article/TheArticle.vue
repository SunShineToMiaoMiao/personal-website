<template>
  <div class="main-container container article-wrapper">

    <!-- 左边侧边栏 -->
    <operation-panel></operation-panel>

      <!-- 文章内容 -->
    <section class="app-section article">
      <h1>基于vue+element实现的修改密码的单文件组件：changePassword.vue</h1>
      <ul class="article-info">
        <li>127 次阅读</li>
        <li>12 评论</li>
        <li>2 已应用

        <li>2018-04-13 12:03</li>
      </ul>
      <div class="article-tag">
        <label class="technical-tag">原创</label>
        <label class="technical-tag">vue</label>
        <label class="technical-tag">element</label>
        <!--<Tag checkable color="#41B883">vue</Tag>-->
        <!--<Tag checkable color="#409EFF">element</Tag>-->
        <!--<time>2018-03-22</time>-->
      </div>
      <article class="article-content">
        <h2 id="heading_1" data-id="heading_1">1. 应用场景</h2>
        <h3 id="heading_1_0" data-id="heading_1_0">1.1 web端管理系统</h3>
        <p>最近在做基于vue+element的web端后台管理项目，遇到登录用户可以修改密码的需求，于是整理出一个修改密码的单文件组件：changePassword.vue</p>
        <h2 id="heading_2" data-id="heading_2">2. 代码</h2>
        <pre v-highlightA>
          <!-- 需要用v-text指令，否则会编译里面的代码 -->
          <code v-text="html">
          </code>
        </pre>
        <pre v-highlightA>
          <code v-text="JavaScriptHtml">
          </code>
        </pre>
      </article>
    </section>

    <!-- 右边侧边栏 -->
    <aside class="app-right-aside">
      <catalog></catalog>
    </aside>
    <!--</div>-->
  </div>
</template>

<script>
  import OperationPanel from './left-side/OperationPanel'
  import SidebarBox from '../../components/SidebarBox'
  import Catalog from './right-side/Catalog'

  export default {
    name: 'TheArticle',
    components: {Catalog, SidebarBox, OperationPanel},
    data() {
      return {
        html: '<div class="el-form-item el-form-item--feedback">\n' +
        '            <label class="el-form-item__label"\n' +
        '                   style="width: 200px;font-size: 16px; color: rgb(23, 156, 233);">我的账号：</label>\n' +
        '            <div class="el-form-item__content" style="margin-left: 200px;">\n' +
        '              <span class="change-password-user-phone">{{loginUserPhone}}</span>\n' +
        '            </div>\n' +
        '          </div>' + '<div class="el-form-item el-form-item--feedback">\n' +
        '            <label class="el-form-item__label"\n' +
        '                   style="width: 200px;font-size: 16px; color: rgb(23, 156, 233);">我的账号：</label>\n' +
        '            <div class="el-form-item__content" style="margin-left: 200px;">\n' +
        '              <span class="change-password-user-phone">{{loginUserPhone}}</span>\n' +
        '            </div>\n' +
        '          </div>' + '<div class="el-form-item el-form-item--feedback">\n' +
        '            <label class="el-form-item__label"\n' +
        '                   style="width: 200px;font-size: 16px; color: rgb(23, 156, 233);">我的账号：</label>\n' +
        '            <div class="el-form-item__content" style="margin-left: 200px;">\n' +
        '              <span class="change-password-user-phone">{{loginUserPhone}}</span>\n' +
        '            </div>\n' +
        '          </div>',
        JavaScriptHtml: 'function is32Bit(c) {\n' +
        '  return c.codePointAt(0) > 0xFFFF;\n' +
        '}\n' +
        '\n' +
        'is32Bit("𠮷") // true\n' +
        'is32Bit("a") // false'
      }
    },
    beforeRouteUpdate(to, from, next) {
      // react to route changes...
      // don't forget to call next()
      const i = 0
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../styles/variables";
  @import "../../styles/mixin";

  .article-wrapper{
    display: -webkit-box;
  }

  .article {
    text-align: left;
    padding: 1.6rem;
    background-color: #FFFFFF;

    h1 {
      font-size: 32px;
      font-weight: 500;
      line-height: 42px;
    }
    &-info {
      list-style: none;
      @include flex-row($alignY:flex-start,$alignX:baseline);
        white-space: nowrap;
      margin: 1rem 0;
      li:not(:last-child):after {
        content: "\B7";
        margin: 0 .4em;
        color: #8f969c;
      }
    }
    &-tag {
      @include flex-row(flex-start,flex-start);
      /*margin: 0.5rem 0;*/
      margin-bottom: 2rem;

      label {
        color: $appColor;
        border: solid 1px;
        padding: 0 10px;
        border-radius: 5px;
        margin-right: 5px;
      }
    }
    /* 文章内容 */
    &-content {
      word-break: break-word;
      line-height: 1.75;
      font-weight: 400;
      font-size: 15px;
      color: #333333;

      h2, h3 {
        line-height: 1.5;
        font-weight: 500;
        margin: 1rem 0;
      }
      h2 {
        padding-bottom: 0.8rem;
        font-size: 1.8rem;
        border-bottom: 1px solid #ececec;
      }
      h3 {
        font-size: 1.2rem;
        padding-bottom: 0;
      }
      pre{
        position: relative;
        /*line-height: 1.75;*/
        /*font-family: Menlo, Monaco, Consolas, Courier New, monospace;*/
        overflow: auto;
        display: flex;
        border-radius: 5px;
      }
      code{
        border-radius: 5px;
        width: 100%;
      }
    }
  }

</style>
