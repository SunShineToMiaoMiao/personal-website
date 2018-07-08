<template>
    <div class="filter-nav">
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
        <!--readNum commentNum upNum publishedTime downloadable-->
        </ul>

      <!-- 小分辨率下的筛选下拉框 -->
      <div class="filter-drop-down">
        <Dropdown trigger="click" @on-click="onSelectedFilter">
          <a href="javascript:void(0)" class="filter-title">
            {{filterTitle}}
            <Icon type="arrow-down-b"></Icon>
          </a>
          <DropdownMenu slot="list">
            <DropdownItem name="阅读数">阅读数</DropdownItem>
            <DropdownItem name="评论数">评论数</DropdownItem>
            <DropdownItem name="点赞数">点赞数</DropdownItem>
            <DropdownItem name="发布时间">发布时间</DropdownItem>
            <DropdownItem name="可下载">可下载</DropdownItem>
          </DropdownMenu>
        </Dropdown>
      </div>

      <!-- 小分辨率下的标签下拉框 -->
      <div class="tag-drop-down">
        <Dropdown trigger="click" @click="onSelectedFilter">
          <a href="javascript:void(0)" class="filter-title">
            <!---->
            <span><svg-icon icon-class="biaoqian"></svg-icon></span>
            <span>标签</span>
            <Icon type="arrow-down-b"></Icon>
          </a>
          <DropdownMenu slot="list">
            <DropdownItem name="vue">
              <span><svg-icon icon-class="vuejs"></svg-icon></span>
              <span class="tech-tag-name">vue</span>
            </DropdownItem>
            <DropdownItem name="python">
              <span><svg-icon icon-class="python1"></svg-icon></span>
              <span class="tech-tag-name">python</span>
            </DropdownItem>
            <DropdownItem name="sass">
              <span><svg-icon icon-class="Sass"></svg-icon></span>
              <span class="tech-tag-name">sass</span>
            </DropdownItem>
            <!--<DropdownItem name="element">-->
            <!--</DropdownItem>-->
          </DropdownMenu>
        </Dropdown>
      </div>
    </div>
</template>

<script>
  export default {
    name: 'FilterNav',
    components: {},
    data() {
      return {
        filterTitle: '筛选'
      }
    },
    methods: {
      // 选择筛选条件
      onSelectedFilter(val) {
        console.log(val)
        this.filterTitle = val
        // space-before-function-paren
      }
    }
  }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
  @import "../../styles/variables";
  @import "../../styles/mixin";

  .filter-nav {
    @include flex-row(flex-start, flex-start);
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
    .filter-drop-down {
      margin: 0 1rem;
      .filter-title {
        color: #333333;
      }
    }

    .tag-drop-down {
      /*display: inline;*/
      .filter-title {
        color: #333333;
        /*line-height: 18px;*/
        height: 1.5em;
        span:first-of-type {
          vertical-align: sub;
        }
      }
      .tech-tag-name {
        vertical-align: super;
        margin-left: 0.1rem;
      }
    }
  }

  /* 标签 start */
  @media screen and (min-width: 980px) {
    .filter-nav {
      .tag-drop-down {
        display: none !important;
      }
    }
  }

  @media screen and (max-width: 979px) {
    .filter-nav {
      .tag-drop-down {
        display: block;
      }
    }
  }
  /* 标签end */

  /* 筛选 start */
  /*720分辨率（大于480px，小于767px）*/
  @media screen and (min-width: 767px) {
    .filter-nav {
      .filter-list {
        display: inherit;
      }
      .filter-drop-down {
        display: none;
      }
    }
  }
  /*440分辨率以下（小于479px）*/
  @media only screen and (max-width: 768px) {
    .filter-nav {
      .filter-list {
        display: none !important;
      }
      .filter-drop-down {
        display: block;
      }
    }
  }

  /* 筛选 end */

</style>
