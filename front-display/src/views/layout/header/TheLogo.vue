<template>
  <div class="app-logo">
    学而时习之
  </div>
</template>

<script>
  export default {
    name: 'TheLogo',
    data () {
      return {
        msg: 'Welcome to Your Vue.js App'
      }
    }
  }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
  @import "../../../styles/variables";

  .app-logo {
    color: $appColor;
    letter-spacing: 1px;
    font-size: 16px;
    text-space: 1px;
    font-weight: 600;
    text-align: center;
  }
</style>
