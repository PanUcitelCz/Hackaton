<script lang="ts">
    import '../lib/css/normallize.css';
</script>

<svelte:head>
	<link rel="preconnect" href="https://fonts.googleapis.com" />
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="" />
	<link
		href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@10..48,200;10..48,600&display=swap"
		rel="stylesheet"
	/>
</svelte:head>

<main>
    <slot />
</main>


<style lang="stylus">
    
    :global(body)
        font-family 'Bricolage Grotesque', sans-serif

	main
		margin 0 auto
		max-width 1300px
		padding 12px

		@media only screen and (min-width 991px)
			padding 24px

</style>