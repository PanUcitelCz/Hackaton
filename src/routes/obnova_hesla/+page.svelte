<script lang="ts">
	import Buttons from "$lib/components/Buttons.svelte";


</script>

<svelte:head>
    <title>Login</title>
</svelte:head>

    <div class="container">
        <div class="label">
            <h3>Obnovení hesla</h3>
        </div>
        <div class="group">
            <input type="text" id="emial" class="input" required="true">
            <span class="highlight"></span>
            <span class="bar"></span>
            <!-- svelte-ignore a11y-label-has-associated-control -->
            <label>Email</label>
        </div>
        <div class="group">
            
            <input type="text"  id="Nick" class="input" required="true">
            <span class="highlight"></span>
            <span class="bar"></span>
            <!-- svelte-ignore a11y-label-has-associated-control -->
            <label>Nick</label>
        </div>
        <div class="butt">
            <Buttons on:click={undefined} symbol={"Požádat"} bgColor={"grey"} />
            
        </div>
    </div>

<style lang="stylus">

    .container
        margin auto
        display flex
        flex-direction column
        justify-content center
        align-items center
        margin-top 36px

    .label
        color white

    .butt
        margin-top 15px
        display flex
        flex-direction column

        @media $large-up
            flex-direction row
    
    .group
        position relative
        margin-top 34px

    .input
        font-size 16px
        padding 10px 10px 10px 5px
        display block
        width 185px
        border none
        border-bottom 1px solid white
        background transparent
        color white

        &:focus
            outline none

    label
        color white
        font-size 18px
        font-weight normal
        position absolute
        pointer-events none
        left 5px
        top 10px
        transition 0.2s ease all
        -moz-transition 0.2s ease all
        -webkit-transition 0.2s ease all

    .input:focus ~ label
        top -20px
        font-size 12px
        color white
    
    .input:valid ~ label
        top -20px
        font-size 12px
        color white
    
   .bar
        position relative
        display block
        width 200px
       
        &:before &:after
            content ""
            height 2px
            width 0
            bottom 1px
            position absolute
            background #0e94f4
            transition 0.2s ease all
            -moz-transition 0.2 ease all
            -webkit-transition 0.2 ease all

        &:before
            left 50%

        &:after
            right 50%

        .input:focus ~ .bar:before
            top -20px
            font-size 12px
            color #0e94f4

        .input:focus ~ .bar:after
            top -20px
            font-size 12px
            color #0e94f4
        
        .highlight
            position absolute
            height 60%
            width 0px
            top 25%
            left 0
            pointer-events none
            opacity 0.5

        .input:focus ~ .hightlight
            animation input-focus 0.5s ease
            
        @keyframes input-focus
            from
                background #1486d7

            to
                width 185px
                background transparent

</style>


