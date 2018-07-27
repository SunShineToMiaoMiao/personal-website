<template>
  <sidebar-box class="catalog">
    <p class="catalog-title">目录</p>
    <ul class="catalog-first-level">
      <li><a href="#heading_1">1. 应用场景啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦</a></li>
      <li>
        <a href="#heading_1_0">2. 思路</a>
        <ul class="catalog-second-level">
          <li><a href="#heading_1_0">2.1 布局</a></li>
          <li>
            <a href="#heading_1_0">2.2 流程</a>
            <ul class="catalog-three-level">
              <li><a href="#heading_1_0">2.2.1 验证表单</a></li>
              <li><a href="#heading_1_0">2.2.2 注意点</a></li>
            </ul>
          </li>
        </ul>
      </li>
      <li><a href="#heading_2">3. 代码</a></li>
    </ul>
  </sidebar-box>
</template>

<script>
  import SidebarBox from '../../../components/SidebarBox'

  export default {
    name: 'catalog',
    components: {SidebarBox}
  }
</script>

<style lang="scss" scoped>
  @import "../../../styles/variables";

  .catalog {
    position: relative;
    &-title {
      font-size: 16px;
      font-weight: bold;
      line-height: 1.8;
    }
    a {
      display: block;
      position: relative;
      padding: 4px 0 4px 21px;
      white-space: nowrap;
      overflow: hidden;
      /*&:before {
        left: 5px;
        margin-top: -3px;
        width: 6px;
        height: 6px;
        content: "";
        position: absolute;
        top: 50%;
        background-color: $linkColor;
        border-radius: 50%;
      }*/
    }
    &-first-level a {
      /*display: block;*/
      /*position: relative;*/
      /*!*padding: 4px 0 4px 12px;*!*/
      /*padding: 4px 0 4px 21px;*/
      /*white-space: nowrap;*/
      /*overflow: hidden;*/
      /*text-overflow: ellipsis;*/
      &:before {
        left: 5px;
        margin-top: -3px;
        width: 6px;
        height: 6px;
        content: "";
        position: absolute;
        top: 50%;
        background-color: $linkColor;
        border-radius: 50%;
      }
    }
    &-second-level a {
      display: block;
      position: relative;
      /*padding: 4px 0 4px 12px;*/
      padding: 4px 0 4px 21px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      &:before {
        left: 5px;
        margin-top: -3px;
        width: 5px;
        height: 5px;
        content: "";
        position: absolute;
        top: 50%;
        background-color: $linkColor;
        border-radius: 50%;
      }
    }
    &-three-level a {
      display: block;
      position: relative;
      /*padding: 4px 0 4px 12px;*/
      padding: 4px 0 4px 21px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      &:before {
        left: 5px;
        margin-top: -3px;
        width: 4px;
        height: 4px;
        content: "";
        position: absolute;
        top: 50%;
        background-color: $linkColor;
        border-radius: 50%;
      }
    }
    &-second-level, &-three-level {
      padding: 0 10px;
      position: relative;
    }
    /*&-three-level{*/
    /*padding: 0 10px;*/
    /*position: relative;*/
    /*}*/
  }
</style>
