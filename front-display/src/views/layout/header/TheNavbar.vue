<template>
  <div class="app-menu-list">
    <!-- 全部菜单 -->
    <div class="menu-all">
      <div>
        <router-link to="/index" class="app-menu-item">
          首页
        </router-link>
      </div>
      <div>
        <router-link to="/common" class="app-menu-item">
          常用
        </router-link>
      </div>
      <div></div>
    </div>
    <!-- 小分辨率下的下拉菜单 -->
    <div class="menu-drop-down">
      <Menu mode="horizontal" active-name="1">
        <Submenu name="1">
          <template slot="title">
            首页
          </template>
          <MenuItem name="3-4">常用</MenuItem>
        </Submenu>
      </Menu>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'TheNavbar',
    data () {
      return {
        msg: 'Welcome to Your Vue.js App'
      }
    }
  }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
  @import "../../../styles/variables";
  @import "../../../styles/mixin";
  /* 一级导航的字体大小 */
  $firstLevel: 16px;
  .app-menu-list {
    @include flex-row();
    font-size: $firstLevel;
    .menu-all {
      .app-menu-item {
        &:hover {
          background: #F3F3F3;
        }
        padding: $commonPadding;
        color: #B8B8B8;
        width: 60px;
        height: 40px;
        flex: none;
      }
    }
    .menu-drop-down{
      /*<!--font-size: $firstLevel !important;-->*/
      margin-left: 1rem;
    }
/*
    div:last-child {
      flex: 1;
    }*/
  }

  @media screen and (min-width: 980px) {
    .app-menu-list {
      .menu-all {
        display: -webkit-box;
      }
      .menu-drop-down {
        display: none !important;
      }
    }
  }

  @media screen and (max-width: 979px) {
    .app-menu-list {
      .menu-all {
        display: none !important;
      }
      .menu-drop-down {
        display: -webkit-box;
      }
    }
  }
</style>
