<template>
    <div>
        <div class="app-menu-list flex-row-center">
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
    /* 一级导航的字体大小 */
    $firstLevel: 16px;
    .app-menu-list {
        font-size: $firstLevel;
        .app-menu-item {
            &:hover{
                background: #F3F3F3;
            }
            padding: $commonPadding;
            color: #B8B8B8;
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
</style>
