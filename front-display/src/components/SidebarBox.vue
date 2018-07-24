<template>
  <div class="sidebar-box">
    <div v-if="_title" class="sidebar-box-title">
      <p>技术标签</p>
    </div>
    <div class="sidebar-box-container">
      <slot></slot>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'SidebarBox',
    props: {
      title: {
        type: String
      }
    },
    created() {
      this._title = this.title
    },
    data() {
      return {
        _title: ''
      }
    }

  }
</script>

<style scoped lang="scss">
.sidebar-box{
  border-radius: 2px;
  background-color: #FFFFFF;
  &-tilte{
    /*width: ;*/
    border-bottom: #dddddd;
  }
  &-container{
    text-align: left;
    padding: 1.2rem;
  }
}
</style>
