<script lang="ts">
    import Header from '$lib/components/Header.svelte';
    import Footer from '$components/Footer.svelte';
</script>

<svelte:head>
	<link rel="preconnect" href="https://fonts.googleapis.com" />
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="" />
	<link
		href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@10..48,200;10..48,600&display=swap"
		rel="stylesheet"
	/>
</svelte:head>

<Header />

<main>
    <slot />
</main>

<Footer />

<style lang="stylus">
	:global(body)
		background-color white !important

	main
		margin auto
		max-width 1300px
		padding 12px

		@media only screen and (min-width 991px)
			padding 24px

</style>