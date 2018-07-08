<template>
  <div class="technical-nav">
    <h5 class="technical-nav-title">标签</h5>
    <!--<router-link to=""></router-link>-->

    <technical-nav-item to="" icon-class="vuejs">vue</technical-nav-item>
    <technical-nav-item to="" icon-class="python1">python</technical-nav-item>
    <technical-nav-item to="" icon-class="Sass">sass</technical-nav-item>
    <technical-nav-item to="" icon-class="biaoqian">更多标签</technical-nav-item>
  </div>
</template>

<script>
  import TechnicalNavItem from './TechnicalNavItem'

  export default {
    name: 'TechnicalNav',
    components: {TechnicalNavItem}
  }
</script>

<style lang="scss" scoped>

  .technical-nav {
    text-align: left;
    width: 8rem;
    margin-right: 2rem;
    &-title {
      margin-bottom: 0.5rem;
      /*margin-top: 1rem;*/
    }
    &-title::after {
      position: absolute;
      content: '';
      border-bottom: 1px solid #eee;
      width: 6.2rem;
      margin-left: 0.2rem;
      margin-top: 0.5rem;
    }
  }

  /* 技术标签 start */
  @media screen and (min-width: 980px) {
    .technical-nav {
      display: block;
    }
  }

  @media screen and (max-width: 979px) {
    .technical-nav {
        display: none;
    }
  }
  /* 技术标签 end */

</style>
