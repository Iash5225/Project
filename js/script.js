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
        //Find the input div
        var input = document.getElementsByClassName("input")[0];
        
        //Run loop 5 times to create 5 input slots
        for(let j = 0 ; j < 5 ; j++){
            //Create a new div
            let inputcell = document.createElement("div");

            //Set class name to inputcells
            inputcell.className = "inputcells";

            //Append to input
            input.appendChild(inputcell);
        }

    }

    //Create input on load
    createInput();

    //Storing every letter clicked
    var lettersClicked = [];
    var count = 0;
    
    function clickedCell(){
        if(count == 5){
            alert("Already have 5 letters");
            return;
        }

        //Declare it to be clicked or unclicked
        if(this.className == "unclicked"){
            this.className = "clicked";

            //Add to array
            lettersClicked.push(this.dataset.word);
            this.value = count;
            count++;

        } else{
            this.className = "unclicked";
            
            //Removes the first instance of the selected letter
            var inputcelllist = document.getElementsByClassName("inputcells");
            for(let k = 0 ; k < 5 ; k++){
                if(inputcelllist[k].dataset.word == this.dataset.word){
                    inputcelllist[k].parentNode.removeChild(inputcelllist[k]);
                    break;
                }
            }
            //Create a new div
            let inputcell = document.createElement("div");

            //Set class name to inputcells
            inputcell.className = "inputcells";
            console.log(inputcell);

            document.getElementsByClassName("input")[0].appendChild(inputcell);

            count--;
        }

        //Call a function which inserts it into the input div
        addToInput(this.dataset.word , count-1);
        
    }

    function addToInput(word , count){
        var g = document.getElementsByClassName("inputcells");
        var h = document.getElementsByClassName("grid");
        
        g[count].innerHTML = word;
        g[count].dataset.word = word;
        count++;
    }

    //Generating a random letter
    function generateRandomLetter() {
        //Create array of all possible choices
        const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        //Return a random one from the array
        return alphabet[Math.floor(Math.random() * alphabet.length)]
      }
});

/* Menu button */
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
  }