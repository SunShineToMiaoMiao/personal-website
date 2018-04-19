<template>
  <div class="left-side">
    标签
    <router-link to=""></router-link>

    <a class="tech-tag-item" href="/bc">
      <span class="tech-tag-item-icon">
        <svg-icon icon-class="vuejs"></svg-icon>
      </span>
      <span>vue</span>
    </a>
    <a class="tech-tag-item" href="/bc">
      <span class="tech-tag-item-icon">
        <svg-icon icon-class="python1"></svg-icon>
      </span>
      <span>python</span>
    </a>
    <a class="tech-tag-item" href="/bc">
      <span class="tech-tag-item-icon">
        <svg-icon icon-class="Sass"></svg-icon>
      </span>
      <span>sass</span>
    </a>
    <a class="tech-tag-item" href="/bc">
      <span class="tech-tag-item-icon">
        <svg-icon icon-class="biaoqian"></svg-icon>
      </span>
      <span>更多标签</span>
    </a>

  </div>
</template>

<script>
  export default {
    name: 'TheLeftSide'
  }
</script>

<style lang="scss" scoped>
  @import "../../styles/variables";
  .left-side{
    /*<!--z-index: $fixedZindex;-->*/
    .tech-tag-item {

    height: 34px;
    display: flex;
    align-items: center;
    color: #757575;
    text-decoration: none;
    margin-bottom: 1px;
    border-radius: 4px;
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
  }


</style>
