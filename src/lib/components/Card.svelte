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
        <div class="title">
            <h3>{nadpis}</h3>
        </div>
        <div class="nazev">
            <div class="icon">
                <img src="{img}" alt="">
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
                <div class="like">
                    <span>{like}</span>
		    <span><img src="images/like.svg" alt="" on:click={async (e) => {change(e.target); toggleVote(Cookies.get("user"), location_id)}}></span>
                </div>
            </div>
            <div class="hodnoceni">
                
            </div>
        </div>
    </div>
</div>
<style lang="stylus">

    .restaurace
        display flex
        justify-content center
        align-items center
        border-radius 10px
        min-height 150px
        box-shadow 0px 2px 10px grey
        padding 10px
        margin-bottom 15px
        gab 15px
        
            

    .icon
        //width 200px
        display flex
        justify-content center
        align-items center

        img
            display flex
            width 100%
            border-radius 10px
            justify-content center

    .nazev
        padding 0 15px
        width 100%
        display flex
        flex-direction column
        align-items center
        justify-content center

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
        display flex
        flex-direction column
        justify-content center
        align-items center


    .Footer-card
        display flex
        justify-content space-between
        flex-direction column
        width 100%
        
        .odkazy
            display flex
            align-items center
            justify-content space-between
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
        margin 15px 0

        img
            width 30px
            cursor pointer

    .like
        display flex
        align-items center


</style>
