<template>
  <div class="technical-nav">
    <h5>标签</h5>
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
  }

</style>
