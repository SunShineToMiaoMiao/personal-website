<template>
  <div>
    <div class="menu-list flex-row-center">
      <router-link tag="div" to="/index">
        首页
      </router-link>
      <router-link tag="div" to="/common">
        常用
      </router-link>
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
  .menu-list {
    /*height: 50px;
    position: fixed;
    width: 100%;
    z-index: 999;
    top: 0;
    line-height: 50px;
    border-radius: 0 !important;
    color: #949494 !important;*/

    /*.screenfull {
      position: absolute;
      right: 90px;
      top: 16px;
      color: red;
    }
    .avatar-container {
      height: 50px;
      display: inline-block;
      position: absolute;
      right: 55px;
      .avatar-wrapper {
        cursor: pointer;
        margin-top: 5px;
        position: relative;
        .user-avatar {
          width: 40px;
          height: 40px;
          border-radius: 10px;
        }
        .el-icon-caret-bottom {
          position: absolute;
          right: -20px;
          top: 25px;
          font-size: 12px;
        }
      }
    }*/
  }
  /*.flex-center {
    display: flex;
    justify-content: space-around;
    flex-flow: row nowrap;
    align-items: center;
    align-content: flex-start;
  }*/
</style>
