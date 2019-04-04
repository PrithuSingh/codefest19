<template>
  <div :class="[$style.faqItem, $style[$mq]]">
    <div :class="$style.question" @click="toggleQues">
      <p>
        {{item.question}}
        <i
          class="fa fa-chevron-down"
          :style="chevronRotateStyle"
          aria-hidden="true"
        ></i>
      </p>
    </div>
    <div :class="$style.answer" :style="answerHeightStyle" ref="answer">
      <slot></slot>
    </div>
  </div>
</template>

<script>
import { TweenLite } from "gsap";

export default {
  data() {
    return {
      open: false,
      openProgress: 0,
      maxHeight: -1
    };
  },

  props: {
    item: {
      required: true,
      type: Object
    },
    index: {
      required: true,
      type: Number
    }
  },

  methods: {
    toggleQues: function() {
      this.open = !this.open;
      this.$emit("onToggleQuestion", this.index, this.open);
    }
  },

  computed: {
    height() {
      return this.openProgress * this.maxHeight;
    },
    angle() {
      return this.openProgress * 180;
    },
    answerHeightStyle() {
      return this.maxHeight >= 0 ? { height: ` ${this.height}px` } : {};
    },
    chevronRotateStyle() {
      return { transform: `rotate(${this.angle}deg)` };
    }
  },

  watch: {
    open: function(val) {
      TweenLite.to(this.$data, 0.4, { openProgress: val ? 1 : 0 });
    }
  },
  mounted() {
    this.maxHeight = this.$refs.answer.offsetHeight + 10;
  }
};
</script>

<style lang="stylus" module>
@require '~@styles/theme';
@require '~@styles/anims';
@require '~@styles/mixins';

.faqItem {
  position: relative;
  width: 100%;
  text-align: left;
  clear: both;
  border-bottom: 2px solid $chartreuse;

  a {
    color: $dodger-blue;
  }

  .question {
    font-size: 20px;
    cursor: pointer;
    font-family: 'ubuntu';
    font-weight: bold;

    i {
      position: absolute;
      right: 0px;
    }

    ^[0].xs, ^[0].sm {
      font-size: 15px;
    }
  }

  .answer {
    font-size: 18px;
    overflow: hidden;
    width: 100%;
    clear: both;
    font-family: 'Roboto mono';

    ^[0].xs, ^[0].sm {
      font-size: 13px;
    }
  }
}
</style>