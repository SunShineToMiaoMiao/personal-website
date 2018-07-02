<template>
  <div class="app-search-box">
    <Input v-model="searchText" class="search-input"
           icon="ios-search"
           placeholder="搜索习之"
    />
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
  .search-input {
    /*width: 300px;*/
  }

  /* 1280分辨率以上（大于1200px） */
  @media screen and (min-width: 1200px) {
    .search-input {
    width: 600px;
  }
  }

  /*1100分辨率（大于960px，小于1199px）*/

  @media screen and (min-width: 960px) and (max-width: 1199px) {
    .search-input {
      width: 600px;
    }
  }

  /*880分辨率（大于768px，小于959px）*/

  @media screen and (min-width: 768px) and (max-width: 959px) {
    .search-input {
      width: 380px;
    }
  }

  /*720分辨率（大于480px，小于767px）*/

  @media only screen and (min-width: 480px) and (max-width: 767px) {
    .search-input {
      /*width: 380px;*/
      display: none;
    }
  }

  /*440分辨率以下（小于479px）*/

  @media only screen and (max-width: 479px) {
    .search-input {
      /*width: 280px;*/
      display: none;
    }
  }

</style>
