<script lang="ts">
    import Cookies from 'js-cookie'

    export let nadpis: string;
    export let location_id: string;
    export let img: string;
    export let prumer: number;
    export let like: number;
    var voteToggled = "remove-vote"

    async function change(el)
{if(el.style.backgroundColor == "green"){
		    //el.style.backgroundColor = "white"
		    el.src = "../../../static/images/like.svg"
		    el.parentElement.parentElement.firstChild.innerHTML = +el.parentElement.parentElement.firstChild.innerHTML -1
		    }
		    else{
		    //el.style.backgroundColor = "green"
		    el.src = "../../../static/images/like_green.svg"
		    el.parentElement.parentElement.firstChild.innerHTML = +el.parentElement.parentElement.firstChild.innerHTML +1
		    }
		    }
    async function toggleVote(username: string, location_id: string){ 

	var time = prompt("cas kolik?")
	
	if(voteToggled == "add-vote"){
	    voteToggled = "remove-vote"
	    //document.getElementById("voteButton").style.backgroundColor = "white"
	}
	else{
	    voteToggled = "add-vote"
	    //document.getElementById("voteButton").style.backgroundColor = "green"
	}

	const rawResponse = await fetch(`http://localhost:5000/${voteToggled}`, {
	    method: 'POST',
	    headers: {
	      'Accept': 'application/json',
	      'Content-Type': 'application/json',
	      'Access-Control-Allow-Origin': '*'
	    },
	    body: JSON.stringify({"username": username, "location_id": location_id, "time": time})
	});

	const content = rawResponse;

	content.text().then(e=>{
	    e=JSON.parse(e)

	    console.log(e)
	    
	    
	}); 
    } 
</script>


<div class="restaurace">
    <input id="location_id" value={location_id} hidden/>
    <div class="Header-card">
        <div class="icon">
            <img src="{img}" alt="">
        </div>
        <div class="nazev">
            <div class="title">
                <h3>{nadpis}</h3>
            </div>
                <div class="kadiboudy">
                    <span>{prumer} </span>
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
		    <span><img src="images/like.svg" alt="" on:click={async (e) => {change(e.target); toggleVote(Cookies.get("user"), location_id)}}></span>
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
