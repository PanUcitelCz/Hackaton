<script lang="ts">
	import Card from "$components/Card.svelte";

    export let profile: string;
    export let data = [{"location_id": 0, "name": "0"}, {"location_id": 0, "name": "0"}];
    export let test = [1, 5, 3]
    import Cookies from 'js-cookie'
    import { onMount } from 'svelte'

    profile = String(Cookies.get("user"))
    var voteToggled = "remove-vote"

    function eyo(nadpis, like, img, prumer, location_id){
    new Card({target: document.querySelector("#eyo"),
	    props :{
		nadpis: nadpis,
		like: like,
		img: img,
		prumer: prumer,
		location_id: location_id

	    }})
    }

    onMount(async () => {
	if(Cookies.get("session_id") == ""){
	    window.location.href = "./login"
	}


	const rawResponse = await fetch('http://localhost:5000/find-closest', {
	    method: 'GET',
	    headers: {
	      'Accept': 'application/json',
	      'Content-Type': 'application/json',
	      'Access-Control-Allow-Origin': '*'
	    }
	});

	const content = rawResponse;

	content.text().then(e=>{
	    console.log("recieved")
	    console.log(e)

	    data = JSON.parse(e)
	    data.forEach(restaurace => {
		eyo(restaurace.name, restaurace.vote_count, "", restaurace.average, restaurace.location_id)
	    })
	    console.log("")
	});
    });


</script>

<svelte:head>
    <title>{profile}</title>
</svelte:head>

<div class="nadpis">
    <h1 on:click={() => {test.push(6); console.log("aa")}}>Výtejte {profile}</h1>
</div>

<div class="container">
    <section class="seznam">
        <div class="Nadpis">
            <h3>V poslední době hodnoceno</h3>
        </div>
        <div class="hlasovaci_container" id="eyo" use:eyo>
        </div>
    </section>

    

    <section class="side_bar">
        
    </section>
</div>
<style lang="stylus">
    .nadpis
        display flex
        justify-content center
        padding 0 15px

        h1
            color black


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
        width 100px
        display flex
        align-items flex-start

        img
            width 100px
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
