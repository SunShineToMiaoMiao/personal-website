<template>
  <div class="app-logo">
    习之
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
  .app-logo{
    color: $appColor;
    font-size: 16px;
    text-space: 1px;
    text-align: center;
  }
</style>
