<script lang="ts">
    export let profile: string;
    import Cookies from 'js-cookie'

    profile = String(Cookies.get("user"))

</script>

<svelte:head>
    <title>{profile}</title>
</svelte:head>

<div class="nadpis">
    <h1>Výtejte {profile}</h1>
</div>

<div class="container">
    <section class="seznam">
        <div class="Nadpis">
            <h3>Hodnocení</h3>
        </div>
        <div class="hlasovaci_container">
            <div class="restaurace">
                <div class="icon">
                    <img src="https://lh5.googleusercontent.com/p/AF1QipPjMAY9OvOWdck9_IIk_w7HC27hcbcFAHxFYYdl=w122-h92-k-no" alt="">
                </div>
                <div class="nazev">
                    <span>Restaurace</span>
                </div>
            </div>
            <figure class="restaurace">
                <div class="icon">
                    <img src="https://lh5.googleusercontent.com/p/AF1QipPjMAY9OvOWdck9_IIk_w7HC27hcbcFAHxFYYdl=w122-h92-k-no" alt="">
                </div>
                <div class="nazev">
                    <span>Restaurace</span>
                </div>
            </figure>
        </div>
    </section>

    <section class="seznam">
        <div class="hlasovaci_container">
            <div class="Nadpis">
                <h3>Hodnocení</h3>
            </div>
        </div>
    </section>

    <section class="side_bar">
        
    </section>
</div>
<style lang="stylus">
    .nadpis
        display flex
        justify-content center

        h1
            color black


    .seznam
        width 100%
        box-shadow 0px 2px 5px black
        border-radius 11px

    .container
        display flex
        width 100%
        flex-direction column
        justify-content center
        align-items center
        gap 24px

    .hlasovaci_container
        display flex
        flex-direction column
        justify-content center
        align-items center
        min-height 150px
        width 100%
        padding 0


    .Nadpis
        margin 0px
        margin-bottom 15px
        width 100%
        background-color #8a0c0c
        border-radius 10px 10px 0 0
        

        h3
            padding 5px
            margin 0
            color white

    .restaurace
        display flex
        width calc(100% - 50px)
        border-radius 10px
        min-height 150px
        box-shadow 0px 2px 5px black
        padding 10px
        
            

    .icon
        width 100px
        display flex
        align-items flex-start

        img
            width 75%
            width 100px
            border-radius 10px
            max-height 100px

    .nazev
        padding 0 15px

</style>
