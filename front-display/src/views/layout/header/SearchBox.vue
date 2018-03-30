<template>
  <div class="app-search-box">
    <Input v-model="searchText"
           icon="ios-search"
           placeholder="搜索关键字"/>
  </div>
</template>

<script>
export default {
  name: 'SearchBox',
  data () {
    return {
      searchText: '',
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<style scoped>

</style>
