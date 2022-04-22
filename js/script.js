'use strict'

$(window).on('load', () => {

    function createGrid(numrows){
        var grid = document.getElementsByClassName("grid")[0];
            for (let i = 0; i < numrows; i++) {
                //Create new div
                var cells = document.createElement("div");

                //Set divs created to all have a classname "cell"
                cells.className = "unclicked";

                //Generate random letter
                const letter = generateRandomLetter()

                //Set the data to the randomly generated letter
                cells.dataset.word = letter;

                //Display the randomly generated letter
                cells.innerHTML = letter;

                //Call clickedCell function on click
                cells.onclick = clickedCell;

                //Append current cell to grid
                grid.appendChild(cells);
            }
    }

    //Create the grid
    createGrid(40);

    function createInput(){
        var input = document.getElementsByClassName("input")[0];
        console.log(input);
        for(let j = 0 ; j < 5 ; j++){
            let inputcell = document.createElement("div");
            inputcell.className = "inputcells";
            input.appendChild(inputcell);
        }
    }

    createInput();

    //Storing every letter clicked
    var lettersClicked = [];
    var count = 0;

    function clickedCell(){
    if(count == 5){
        alert("Already have 5 letters");
        return;
    }

        //Add to array
        lettersClicked.push(this.dataset.word);

        //Declare it to be clicked or unclicked
        if(this.className == "unclicked"){
            this.className = "clicked";
        } else{
            this.className = "unclicked";
        }
        console.log(lettersClicked);

        //Call a function which inserts it into the input div
        addToInput(this.dataset.word , count);
        count++;
    }

    function addToInput(word , count){
        var g = document.getElementsByClassName("inputcells");
        console.log(count);
        g[count].innerHTML = word;
    }

    //Generating a random letter
    function generateRandomLetter() {
        const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return alphabet[Math.floor(Math.random() * alphabet.length)]
      }
});

/* Menu button */
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
  }