<script lang="ts">
    import { onMount } from "svelte";
    import Cookies from 'js-cookie'

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


    function logout(){
	Cookies.set("session_id", "")
	Cookies.set("user", "")
	window.location.href = "./login"
    }

</script>

    <svelte:window on:resize={resize} />

    <header class="Header">
        <div class="wrapper">
            <div class="logo">
                <img src="images/White logo - no background.svg" alt="">
            </div>
            <button class="Hamburger" class:isOpen on:click={changeOpenState}>
                <span class="Hamburger-stick" />
                <span class="Hamburger-stick" />
                <span class="Hamburger-stick" />
            </button>
            <nav class:isOpen>
                <ul>
                    <li><a href="/profil">Home-page</a></li>
                    <li><a href="/login">Chat</a></li>
                    <li><a href="#" on:click={logout}>Odhlásit</a></li>
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
        z-index 10
        display flex

        .logo
            position relative
            display flex
            flex-direction flex-start
            width 105px
            z-index 10
            margin-left 10px

            img
                width 80px
                z-index 10

        .wrapper
            width 100%
            margin auto
            max-width 1300px
            display flex
            min-height: 96px
            background #e30613
            z-index 10

            &:after
                content ""
                position absolute
                z-index 1
                left 50%
                width 100%
                height 100%
                background-color #e30613
                transform translateX(-50%)
                
                @media $large-up
                    display none

        nav
            position absolute
            background-color #e30613
            z-index 1
            top 0
            left 0
            width 100%
            transform translateY(-100%)
            transition transform .6s $easeOutExpo

            &.isOpen
                transform translateY(60%)

            @media $large-up
                position static
                transition none
                transform none
                display flex
                
            
            ul
                padding 0
                list-style-type none
                display flex
                align-items center
                justify-content center
                align-items center
                gap 35px
                flex-direction column
                width 100%

                @media $large-up
                    padding 0
                    display flex
                    flex-direction row
                    justify-content flex-end
                    gap 24px
                    margin-right 24px

                
                li
                    color blue
                    display flex
                    align-items center
                    justify-content center

                    a
                        text-decoration none
                        color white

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
