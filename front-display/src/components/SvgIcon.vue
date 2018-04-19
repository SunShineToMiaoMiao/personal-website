<template>
  <svg class="icon" :class="iconStyle" aria-hidden="true">
    <use :xlink:href="iconName"></use>
  </svg>
</template>

<script>
  import '../assets/iconfont'
  export default {
    name: 'SvgIcon',
    props: {
      iconClass: {
        type: String,
        required: true
      },
      iconStyle: String
    },
    computed: {
      iconName () {
        return `#icon-${this.iconClass}`
      }
    }
  }
</script>
<style scoped>
  .icon {
    width: 1.5em;
    height: 1.5em;
    vertical-align: -0.15em;
    fill: currentColor;
    overflow: hidden;
  }
</style>
