<template>
  <div class="operation-panel">
    <!--<div class="like-btn panel-btn with-badge" badge="1.4K"></div>
    <div class="comment-btn panel-btn with-badge" badge="91"></div>
    <div class="collect-btn panel-btn">&lt;!&ndash;&ndash;&gt;</div>
    <div class="share-title">分享</div>
    <div class="weibo-btn share-btn panel-btn"></div>
    <div class="qq-btn share-btn panel-btn"></div>
    <div class="wechat-btn share-btn panel-btn">
      <img src="" class="wechat-qr-code-img shadow" style="display: none;"></div>-->
    <operation-panel-item to="" icon-class="youyong"></operation-panel-item>
    <operation-panel-item to="" icon-class="pinglun"></operation-panel-item>
  </div>
</template>

<script>
  import OperationPanelItem from './OperationPanelItem'
  export default {
    name: 'OperationPanel',
    components: {OperationPanelItem}
  }
</script>

<style lang="scss" scoped>
.operation-panel {
  position: fixed;
  margin-left: -7rem;
  top: 16rem;
}
</style>
