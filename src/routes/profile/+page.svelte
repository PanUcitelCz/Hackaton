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
        <div class="hlasovaci_container">
            <div class="Nadpis">
                <h3>Hodnocení</h3>
            </div>

            <div class="restaurace">
                <div class="icon">
                    <img src="https://lh5.googleusercontent.com/p/AF1QipPjMAY9OvOWdck9_IIk_w7HC27hcbcFAHxFYYdl=w122-h92-k-no" alt="">
                </div>
                <div class="nazev">
                    <span>Restaurace</span>
                </div>
            </div>
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
        position relative
        display flex
        justify-content center

        h1
            color white

    section
        width 100%
        display flex
        justify-content center
        padding 0

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
        border 1px solid white
        min-height 150px
        width 90%
        border-radius 10px
        position relative
        padding 0
        background white
        gap 24px
        padding 5px 0

        .Nadpis
            position absolute
            left 0
            top 0
            width 100%
            background-color #abbbba 
            border-radius 10px 10px 0 0
            

            h3
                padding 5px
                margin 0
                color black

        .restaurace
            display flex
            width 95%
            border-radius 10px
            margin-top 35px
            min-height 150px
            padding 5px
            box-shadow 0px 2px 5px black
            

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
