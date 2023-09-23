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
		img: "https://restaurace.ugigantu.cz/wp-content/uploads/2018/08/p7280088-1.jpg",
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
    <h1 on:click={() => {test.push(6); console.log("aa")}}>Vítejte {profile}</h1>
</div>

<div class="container">
    
        <div class="Nadpis">
            <h3>Dostupné restaurace v okolí</h3>
        </div>
        <div class="hlasovaci_container" id="eyo" use:eyo>
        </div>
     <!--   <div class="hlasovaci_container" id="eyo" use:eyo>
        </div>-->


    

    <section class="side_bar">
        
    </section>
</div>
<style lang="stylus">

    .nadpis
        display flex
        justify-content center
        padding 0 15px
        width 100%

        h1
            color black
            
    .container
        display flex
        width 100%
        flex-direction column
        justify-content center
        align-items center
        gap 10px

    .hlasovaci_container
        display grid
        grid-template-columns: repeat(3, 3fr)
        justify-content: center;
        align-content: center;
        width 100%
        padding 0
        gap 25px
    


    .Nadpis
        margin 0px
        margin-bottom 15px
        background-color #8a0c0c
        border-radius 10px
        padding 15px
        width 100%
        
        
        

        h3
            padding 5px
            margin 0
            color white
            text-align center

            
</style>
