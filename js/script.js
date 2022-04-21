'use strict'

$(window).on('load', () => {

    function createGrid(numrows){
        var grid = document.getElementsByClassName("grid")[0];
            for (let i = 0; i < numrows; i++) {
                //Create new div
                var cells = document.createElement("div");

                //Set divs created to all have a classname "cell"
                cells.className = "clickable";

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

    //Storing every letter clicked
    var lettersClicked = [];

    function clickedCell(){
        //Add to array
        lettersClicked.push(this.dataset.word);

        //Declare it to be clicked
        this.className = "clicked";
        console.log(lettersClicked);

        //Call a function which inserts it into the input div
        addToInput();
    }

    function addToInput(){
        console.log("Hi");
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