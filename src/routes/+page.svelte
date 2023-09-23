<script lang="ts">
	import Buttons from "$components/Buttons.svelte";


</script>

<svelte:head>

    <title>Home page</title>

</svelte:head>

   <div class="hero">
        <div class="logo">
            <img src="images/White logo - no background.svg" alt="">
        </div>
        <div class="slogan">
            <span> "Protože hodnotit hvězdičkami je nuda"</span>
        </div>
        <div class="buttons">
            <a href="/login"><Buttons on:click={undefined} symbol={"Přihlásit"} bgColor={"#39c41f"} /></a>
            <a href="/register"><Buttons on:click={undefined} symbol={"Zaregistrovat"} bgColor={"grey"} /></a>
        </div>
        <img src="images/like_green.svg">
   </div>


<style lang="stylus">

    .hero
        position relative
        margin auto
        height 100%
        width 100%
        max-width 1300px
        display flex
        justify-content center
        align-items center
        flex-direction column
        margin-top 15%

    .logo
        width 100%
        display flex
        justify-content center
        align-items center

        img
            width 50%

    .slogan
        display flex
        justify-content center
        font-size 2rem
        color white
        margin-top 35px
        text-align center

        @media $small-wide-up
            font-size 3rem

    .buttons
        display flex
        justify-content center
        flex-direction column
        align-items center
        margin-top 35px

        @media $small-wide-up
            position relative
            flex-direction row
            justify-content center
            align-items center

</style>