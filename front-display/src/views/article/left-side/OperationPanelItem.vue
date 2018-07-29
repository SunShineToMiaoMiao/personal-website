<template>
  <div class="operation-button">
    <svg-icon :icon-class="iconClass"></svg-icon>
  </div>
</template>

<script>
  export default {
    name: 'OperationPanelItem',
    props: {
      to: {
        type: String
      },
      iconClass: {
        type: String
      }
    },
  }
</script>

<style lang="scss" scoped>
  .operation-button{
    background-color: #FFFFFF;
    /*border: solid 1px #cccc;*/
    padding: 0.5rem;
    border-radius: 50%;
    margin:0.8rem 0;
    line-height: 0.5rem;
  }

</style>
