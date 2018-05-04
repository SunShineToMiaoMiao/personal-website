<template>
  <router-link :to="to" class="technical-nav-item">
      <span class="technical-nav-item-icon">
        <svg-icon :icon-class="iconClass"></svg-icon>
      </span>
    <span><slot></slot></span>
  </router-link>
</template>

<script>
  export default {
    name: 'TechnicalNavItem',
    props: {
      to: {
        type: String
      },
      iconClass: {
        type: String
      }
    },
    data () {
      return {}
    }
  }
</script>

<style lang="scss" scoped>
.technical-nav-item {

      height: 34px;
      display: flex;
      align-items: center;
      color: #757575;
      text-decoration: none;
      margin-bottom: 1px;
      border-radius: 4px;
      span:last-child{
        font-size: 13px;
        height: 22px;
      }
      &-icon {
        img {
          width: 16px;
          height: 16px;
        }
        width: 35px;
        text-align: center;
        color: #999;
      }
    }
</style>
