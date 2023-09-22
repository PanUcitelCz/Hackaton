<script lang="ts">
    import { onMount } from "svelte";

    let desktop: MediaQueryList

    onMount(() => {
        desktop = window.matchMedia('(min-width: 991px)')
    })

    const resize = () => {
        if (desktop.matches) {
            isOpen = false
        }
    }

    const changeOpenState = () => {
        isOpen = !isOpen
    }

    let isOpen = false
</script>

    <svelte:window on:resize={resize} />

    <header class="Header">
        <div class="wrapper">
            <div class="logo">
                
            </div>
            <button class="Hamburger" class:isOpen on:click={changeOpenState}>
                <span class="Hamburger-stick" />
                <span class="Hamburger-stick" />
                <span class="Hamburger-stick" />
            </button>
            <nav>
                <ul>
                    <li><a href="#">Home-page</a></li>
                    <li><a href="#">Test</a></li>
                    <li><a href="#">Test1</a></li>
                </ul>
            </nav>
        </div>
    </header>




<style lang="stylus">

    .Header
        position relative
        width 100%
        height 96px
        background-color grey

        .wrapper
            max-width 1300px
            display flex
            justify-content center
            min-height: 96px

        nav
            position absolute
            display flex
            justify-content center
            align-items center
            background-color grey
            width 100%
            

            ul
                //margin 0
                //margin-top 10px
                padding 0
                list-style-type none
                display flex
                align-items center
                justify-content center
                gap 35px
                flex-direction column
                width 100%

                
                li
                    color blue
                    width 100%
                    display flex
                    align-items center
                    justify-content center

                    a
                        text-decoration none
                        color black

                        &:hover
                            color red
                            
        .Hamburger
            display block
            position absolute
            z-index 4
            width 35px
            height 25px
            right 35px
            top 35px
            cursor pointer
            z-index 100
            background none
            border none

            @media $large-up
                display none

            &.isOpen
                .Hamburger-stick
                    &:nth-child(1)
                        transform: rotate(45deg) translate(8px,8px)

                    &:nth-child(2)
                        opacity 0
                        transform: translateX(-30px)

                    &:nth-child(3)
                        transform rotate(-45deg) translate(7px,-7px)

            &-stick
                position absolute
                display flex
                width 100%
                background #F7F7F7
                height 3px
                border-radius 5px
                opacity 1
                transition $easeOutExpo transform .6s, $easeOutExpo opacity 1s

                &:nth-child(1)
                    top 0
                
                &:nth-child(2)
                    top 50%
                    transform translateY(-50%)

                &:nth-child(3)
                    bottom 0
                    




</style>