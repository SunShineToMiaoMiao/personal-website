<template>
  <div class="sidebar-box">
    <div v-if="_title" class="sidebar-box-title">
      <p>{{ _title }}</p>
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
  &-title{
    font-size: 14px;
    border-bottom: 1px solid #ececec;
    padding: 14px 16px;
    line-height: 1;
  }
  &-container{
    text-align: left;
    padding: 1.2rem;
  }
}
</style>
