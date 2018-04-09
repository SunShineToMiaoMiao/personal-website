<template>
    <div>
        <div class="app-menu-list">
            <div>
                <router-link  to="/index" class="app-menu-item">
                    首页
                </router-link>
            </div>
            <div>
                <router-link  to="/common" class="app-menu-item">
                    常用
                </router-link>
            </div>
            <div></div>

        </div>

        <!--<Menu mode="horizontal" theme="light" active-name="1">-->
            <!--<div class="layout-logo"></div>-->
            <!--<div class="layout-nav">-->
                <!--<MenuItem name="1">-->
                    <!--&lt;!&ndash;<Icon type="ios-navigate"></Icon>&ndash;&gt;-->
                    <!--首页-->
                <!--</MenuItem>-->
                <!--<MenuItem name="2">-->
                    <!--&lt;!&ndash;<Icon type="ios-keypad"></Icon>&ndash;&gt;-->
                    <!--常用-->
                <!--</MenuItem>-->
            <!--</div>-->
        <!--</Menu>-->
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
    .app-menu-list {
        display: flex;
        flex-flow: row nowrap;
        align-items: flex-start;
        justify-content: center;
        /*text-align: left;*/
        /*height: 50px;
        position: fixed;
        width: 100%;
        z-index: 999;
        top: 0;
        line-height: 50px;
        border-radius: 0 !important;
        color: #949494 !important;*/
        .app-menu-item {
            &:hover{
                background: #d3dce6;
            }
            padding: $commonPadding;
            width: 60px;
            height: 40px;
            flex: none;
        }
        div:last-child{
            flex: 1;
        }

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
