<script lang="ts">
    import '../lib/css/normallize.css';
</script>
<main>
    <slot />
</main>


<style lang="stylus">
    
    :global(body)
        font-family 'Bricolage Grotesque', sans-serif
        margin 0
        padding 0
        background-color #E30613

	main
		margin auto
		max-width 1300px
		padding 12px

		@media only screen and (min-width 991px)
			padding 24px

</style>