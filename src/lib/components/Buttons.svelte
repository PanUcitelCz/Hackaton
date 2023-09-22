<script lang="ts">
    // Declaring props
    export let symbol: string;
    export let bgColor: string;
    
</script>

<button on:click style="background-color: {bgColor}">
    {symbol}
</button>

<style lang="stylus">
    button
        border none
        width 190px
        padding 0.5rem 2rem
        color #fff
        font-size 1.5rem
        border-radius 1rem
        transition all 250ms
        transform-origin: center
        margin 15px

        &:hover 
            cursor pointer
            transform scale(0.975)
            box-shadow 0px 1px 3px rgba(0, 0, 0, 0.25)
    
</style>