<template>
  <div class="article-wrapper">

    <!-- 左边侧边栏 -->
    <operation-panel></operation-panel>

    <!-- 文章内容 -->
    <div class="article">
      <h1>基于vue+element实现的修改密码的单文件组件：changePassword.vue</h1>
      <div class="type-tag-time flex-row-center">
        <label>原创</label>
        <Tag checkable color="#41B883">vue</Tag>
        <Tag checkable color="#409EFF">element</Tag>
        <time>2018-03-22</time>
      </div>
      <article class="article-content">
        <h2>1. 应用场景</h2>
        <h3>1.1 web端管理系统</h3>
        <p>最近在做基于vue+element的web端后台管理项目，遇到登录用户可以修改密码的需求，于是整理出一个修改密码的单文件组件：changePassword.vue</p>
        <h2>2. 代码</h2>
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
    </div>

    <!-- 右边侧边栏 -->
    <aside></aside>
  </div>
</template>

<script>
  import OperationPanel from './left-side/OperationPanel'

  export default {
    name: 'TheArticle',
    components: {OperationPanel},
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
    // directives: {
    //   'v-highlight': (el) => {
    //     let blocks = el.querySelectorAll('pre code')
    //     blocks.forEach((block) => {
    //       hljs.highlightBlock(block)
    //     })
    //   }
    // },
    beforeRouteUpdate(to, from, next) {
      // react to route changes...
      // don't forget to call next()
      const i = 0
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../styles/variables";

  .article {
    text-align: left;
    h1 {
      font-size: 32px;
      font-weight: 500;
      /*height: 42px;*/
      line-height: 42px;
    }
    .type-tag-time {
      margin: 0.5rem 0;
      label {
        color: $appColor;
        border: solid 1px;
        padding: 0 10px;
        border-radius: 5px;
        margin-right: 5px;
      }
    }
    hr {
      margin: 20px 0;
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
