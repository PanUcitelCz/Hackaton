<script lang="ts">

    export let nadpis: string;
    export let img: string;
    export let prumer: string;
    export let like: string;

</script>


<div class="restaurace">
    <div class="Header-card">
        <div class="icon">
            <img src="{img}" alt="">
        </div>
        <div class="nazev">
            <div class="title">
                <h3>{nadpis}</h3>
            </div>
                <div class="kadiboudy">
                    <span>{prumer}</span>
                    <span><img src="images/kadibouda.png" alt=""></span>
                    <span><img src="images/kadibouda.png" alt=""></span>
                    <span><img src="images/kadibouda.png" alt=""></span>
                    <span><img src="images/kadibouda.png" alt=""></span>
                </div>
        </div>
        <div class="Footer-card">
            <div class="odkazy">
                <span>
                    <img src="images/web.svg" alt="">
                </span>
                <span>
                    <img src="images/map.svg" alt="">
                </span>
                <span>
                    <img src="images/coments.svg" alt="">
                </span>
            </div>
            <div class="hodnoceni">
                <div class="like">
                    <span>{like}</span>
                    <span><img src="images/like.svg" alt=""></span>
                </div>
            </div>
        </div>
    </div>
</div>
<style lang="stylus">

    .seznam
        width 100%
        box-shadow 0px 2px 5px #8a0c0c
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
        padding 0 5px
        
        

        h3
            padding 5px
            margin 0
            color white

    .restaurace
        display grid
        grid-template-columns: repeat(1, 1fr)
        width calc(100% - 50px)
        border-radius 10px
        min-height 150px
        box-shadow 0px 2px 10px grey
        padding 10px
        margin-bottom 15px
        
            

    .icon
        width 200px
        display flex
        align-items flex-start

        img
            width 200px
            border-radius 10px
            max-height 100px

            @media $large-up
                width 250px

    .nazev
        padding 0 15px
        width 100%
        display flex
        flex-direction column
        align-items start

        @media $large-up
            padding 0 105px

        .title
            display flex
            

        .nadpis
            display flex
            justify-content flex-start
            align-items start



        @media $large-up
                padding 0 40px


    .Header-card
        display grid
        grid-template-columns: 1fr 8fr

    .Footer-card
        display grid
        grid-template-columns repeat(2, 1fr)
        
        .odkazy
            display flex
            align-items center
            gap 6px

            @media $large-up
                gap 15px

            span
                color black

                img
                    width 30px
                    display flex
                    flex-direction row
                    align-items center
                    cursor pointer

    .hodnoceni
        display flex
        justify-content flex-end
        gap 24px
        

        img
            width 30px
            cursor pointer

    .kadiboudy
        display flex
        justify-content center
        align-items center

        img
            width 30px
            cursor pointer

    .like
        display flex
        align-items center


</style>