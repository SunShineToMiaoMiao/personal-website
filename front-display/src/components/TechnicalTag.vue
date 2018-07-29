<template>
  <div class="technical-tag">

  </div>
</template>

<script>
  export default {
    name: 'TechnicalTag',
    props: {
      color: {
        type: String
      }
    },
    created() {
      this._color = this.color;
    }
  }
</script>

<style scoped>

</style>
