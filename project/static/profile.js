"use strict";
$(window).on("load", () => {

    var leaderboard = document.getElementById("leaderboard-modal");
    var statistics = document.getElementById("statistics-modal");

    
    document.getElementById("leaderboard").onclick = function() {
        leaderboard.style.display = "block";
    };

    document.getElementById("statistics").onclick = function() {
        statistics.style.display = "block";
    };

    document.getElementsByClassName("close")[0].onclick = function() {
        leaderboard.style.display = "none";
    };

    document.getElementsByClassName("close")[1].onclick = function() {
        statistics.style.display = "none";
    };

    window.onclick = function(event) {
        if (event.target == leaderboard) {
            leaderboard.style.display = "none";
        } else if(event.target == statistics) {
            statistics.style.display = "none";
        }
    }
    
    let lifetimeGames = JSON.parse(document.getElementById("average").innerHTML);
    let total = 0;
    for (let l = 0 ; l < lifetimeGames.length ; l++){
        total += lifetimeGames[l];
    }
    document.getElementById("average").innerHTML = "Career average: " + total/lifetimeGames.length;
    document.getElementById("games-played").innerHTML = "Games played: " + lifetimeGames.length;

})
