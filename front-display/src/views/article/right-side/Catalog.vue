<template>
  <!--<div>-->

  <!--</div>-->
  <!--<sidebar-box title='目录'>-->
          <!---->
      <!--</sidebar-box>-->
  <sidebar-box title="目录">
    <ul class="catalog">
      <li><a href="#heading_1">1. 应用场景</a></li>
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
.catalog{
  position: relative;
  a{
    display: block;
    position: relative;
    padding: 4px 0 4px 12px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    &:before{
      left: 5px;
    margin-top: -3px;
    width: 6px;
    height: 6px;
        content: "";
    position: absolute;
    top: 50%;
    /*<!--left: 0;-->*/
    /*<!--margin-top: -2px;-->*/
    /*<!--width: 4px;-->*/
    /*<!--height: 4px;-->*/
    background-color: lightseagreen;
    border-radius: 50%;
    }
  }
  &-second-level{
    padding: 2px 10px;
    position: relative;
    &-three-level{
      padding: 2px 10px;
      position: relative;
    }
  }
}
</style>
