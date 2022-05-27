"use strict";
var cur_col = 0;
const MAX_WORD_LENGTH = 15;

$(window).on("load", () => {
    /**
     *
     * @param {integer} numrows - The total number of cells in the grid
     */
    let createGrid = (total) => {
        var grid = document.getElementsByClassName("grid")[0];
        for (let i = 0; i < total; i++) {
            //Create new div
            var cells = document.createElement("div");

            //Set divs created to all have a classname "cell"
            cells.className = "unclicked";

            //adding index to every div in grid
            cells.index = i;

            if (i % 5 == 0) {
                cells.column = 0;
                cells.row = i / 5;
            }
            if (i % 5 == 1) {
                cells.column = 1;
                cells.row = (i - 1) / 5;
            }
            if (i % 5 == 2) {
                cells.column = 2;
                cells.row = (i - 2) / 5;
            }
            if (i % 5 == 3) {
                cells.column = 3;
                cells.row = (i - 3) / 5;
            }
            if (i % 5 == 4) {
                cells.column = 4;
                cells.row = (i - 4) / 5;
            }

            //Generate random letter
            // const letter = generateRandomLetter();

            const letter = "";

            //Set the data to the randomly generated letter
            cells.dataset.word = letter;

            //Display the randomly generated letter
            cells.innerHTML = letter;

            //Call clickedCell function on click
            cells.onclick = clickedCell;

            //Append current cell to grid
            grid.appendChild(cells);
        }
    };

    /**
     *Add all clicked cells to the input box
     */
    function createInput() {
        var input = document.getElementsByClassName("input")[0];

        for (let j = 0; j < MAX_WORD_LENGTH; j++) {
            let inputcell = document.createElement("div");
            inputcell.className = "inputcells";
            input.appendChild(inputcell);
        }
    }

    //Create the grid
    createGrid(40);
    createInput();

    var lettersClicked = [];
    /**
     *
     * @returns a popup window alerting that the max number of letters has been used
     */
    function clickedCell() {
        if (this.innerHTML == "") {
            return;
        }

        //Declare it to be clicked or unclicked
        if (this.className == "unclicked") {
            if (lettersClicked.length == MAX_WORD_LENGTH) {
                console.log("Already have " + MAX_WORD_LENGTH + " letters");
                return;
            }
            this.className = "clicked";

            //Add to array
            lettersClicked.push(
                new clickedLetter(this.dataset.word, this.column, this.row)
            );
        } else {
            this.className = "unclicked";

            for (let i = 0; i < lettersClicked.length; i++) {
                if (
                    lettersClicked[i].row == this.row &&
                    lettersClicked[i].column == this.column
                ) {
                    lettersClicked.splice(i, 1);
                }
            }
        }

        //Call a function which inserts it into the input div
        updateDisplay(lettersClicked);
    }

    document.addEventListener("keydown", KeyHandler);

    function KeyHandler(e) {
        let cells = document
            .getElementsByClassName("grid")[0]
            .getElementsByTagName("div");

        let char = String.fromCharCode(e.keyCode);

        // key was a letter?
        if (/[a-zA-Z]/.test(char)) {
            // let arr = updateGrid(cells)
            for (let i = 0; i < cells.length; i++) {
                if (cells[i].innerHTML == char && cells[i].className == "unclicked") {
                    let keyedCell = clickedCell.bind(cells[i]);
                    keyedCell();
                    return;
                }
            }
        }
        // key was Enter?
        else if (e.keyCode == 13) {
            submitWord();
        }

        // key was Backspace?
        else if (e.keyCode == 8) {
            if (lettersClicked.length == 0) {
                return;
            }
            let c = lettersClicked.pop();
            // console.log(c.row, c.column);
            cells[5 * c.row + c.column].className = "unclicked";
            let keyedCell = clickedCell.bind(c);
            keyedCell();
            return;
        }
    }
    /**
     *
     *
     *    */
    function updateDisplay(lettersClicked) {
        let g = document.getElementsByClassName("inputcells");
        for (let i = 0; i < MAX_WORD_LENGTH; i++) {
            if (i < lettersClicked.length) {
                g[i].innerHTML = lettersClicked[i].letter;
            } else {
                g[i].innerHTML = "";
            }
        }
    }

    //Generating a random letter
    /**
     *
     * @returns a random letter from the alphabet based on letter frequency
     */
    function generateRandomLetter() {
        const WEIGHTS = [
            ["A", 4467],
            ["B", 1162],
            ["C", 1546],
            ["D", 1399],
            ["E", 4255],
            ["F", 661],
            ["G", 1102],
            ["H", 1323],
            ["I", 2581],
            ["J", 163],
            ["K", 882],
            ["L", 2368],
            ["M", 1301],
            ["N", 2214],
            ["O", 2801],
            ["P", 1293],
            ["Q", 84],
            ["R", 3043],
            ["S", 2383],
            ["T", 2381],
            ["U", 1881],
            ["V", 466],
            ["W", 685],
            ["X", 189],
            ["Y", 1605],
            ["Z", 250],
        ];
        let total_weight = 0;
        for (let i = 0; i < WEIGHTS.length; i++) {
            total_weight += WEIGHTS[i][1];
        }
        let roll = Math.floor(Math.random() * total_weight);
        for (let i = 0; i < WEIGHTS.length; i++) {
            roll -= WEIGHTS[i][1];
            if (roll < 0) {
                return WEIGHTS[i][0];
            }
        }
        return "%";
    }

    //Initialising 2d array of letters on the page

    function updateGrid(cells) {
        let arr = [
            [],
            [],
            [],
            [],
            []
        ];

        for (let i = 0; i < 40; i++) {
            arr[i % 5].push(cells[i].innerHTML);
        }
        return arr;
    }

    /**
     * removes the clicked letters and shifts every element down the grid
     *
     */
    function dropdown(arr) {
        var k = document.getElementsByClassName("clicked");

        for (let index = 0; index < k.length; index++) {
            var row = k[index].row;
            var column = k[index].column;
            arr[column][row] = "";

            if (row != 0) {
                for (let j = row; j > 0; j--) {
                    arr[column][j] = arr[column][j - 1];
                }
                arr[column][0] = "";
            }
        }

        while (k.length > 0) {
            k[0].className = "unclicked";
        }

        //make 2d array into 1d array
        //then iterate through 1d array and the divs for the board to edit the inner html

        let temp = [];
        for (let i = 0; i < 8; i++) {
            for (let j = 0; j < 5; j++) {
                var element = arr[j][i];
                temp.push(element);
            }
        }

        //all the divs in the grid
        var griddivs = document
            .getElementsByClassName("grid")[0]
            .getElementsByTagName("div");

        //change grid divs inner html to the cells in the temp arrays string

        for (let i = 0; i < 40; i++) {
            var element = temp[i];
            griddivs[i].innerHTML = element;
            griddivs[i].dataset.word = element;
        }
    }
    //Submitting a possible word
    document
        .getElementById("submit-button")
        .addEventListener("click", submitWord);

    /**
     * Function that checks the submitted word with database, and outputs result of checking
     *
     */
    function submitWord() {
        var cells = document
            .getElementsByClassName("grid")[0]
            .getElementsByTagName("div");
        // var cells = document.getElementsByClassName("unclicked");
        let word = "";
        for (let i = 0; i < lettersClicked.length; i++) {
            word = word.concat(lettersClicked[i].letter);
        }
        // console.log(word);
        if (TRIE.search(word)) {
            //The chosen word exists

            // unclick cells in grid:
            let arr = updateGrid(cells);
            dropdown(arr);
            updateScore(word.length);

            // clear rack
            lettersClicked = [];
            updateDisplay(lettersClicked);
        } else {
            alert("Not a Word");
        }
    }

    var score = 0;
    updateScore(0);
    //Updating the score
    function updateScore(length) {
        score += length;
        document.getElementById("count").innerHTML = "Score: " + score;
    }

    //create variable which start or stops the game
    var gameStart = false;
    var start;

    //Creating a timed tile drop when start is clicked
    document.getElementById("start-button").onclick = function() {
        if (!gameStart) {
            TimedDrop();
            start = setInterval(TimedDrop, 1000);
            gameStart = true;
        } else {
            // alert("Game has already started!");
            return;
        }
    };

    function TimedDrop() {
        let n_cols = 5;
        // let roll = Math.floor(Math.random() * n_cols);
        var roll = cur_col;
        var griddivs = document
            .getElementsByClassName("grid")[0]
            .getElementsByTagName("div");

        const letter = generateRandomLetter();

        griddivs[roll].innerHTML = letter;
        griddivs[roll].dataset.word = letter;
        // griddivs[roll].className = unclickedWord;

        for (let i = roll + 5; i < 40; i = i + 5) {
            var cell = griddivs[i];
            if (griddivs[i].innerHTML == "") {
                cell.innerHTML = letter;
                cell.dataset.word = letter;
                griddivs[i - 5].innerHTML = "";
                griddivs[i - 5].dataset.word = "";
            }
        }
        loss();
        cur_col = (cur_col + 1) % 5;
    }

    //Creating loss condition
    //-when a letter reaches the top of the grid in any of the columns

    function loss() {
        var griddivs = document
            .getElementsByClassName("grid")[0]
            .getElementsByTagName("div");
        for (let i = 0; i < 5; i++) {
            var element = griddivs[i];
            if (element.innerHTML != "") {
                alert("YOU LOSE");
                clearInterval(start);
                updateShare();
                document.getElementById("submit-score").style.visibility = "visible"
            }
        }
    }

    /**
     * Menu Button
     */

    document.getElementById("menuButton").onclick = function() {
        var menuDrop = document.getElementById("menuDropdown");
        if (menuDrop.style.display === "none") {
            menuDrop.style.display = "block";
        } else {
            menuDrop.style.display = "none";
        }
    };

    /**
     * Leaderboard and instructions dropdown
     */
    var leaderboard = document.getElementById("leaderboard-modal");
    var instructions = document.getElementById("instructions-modal");
    var share = document.getElementById("share-modal");

    document.getElementById("leaderboard").onclick = function() {
        leaderboard.style.display = "block";
    };
    document.getElementById("instructions").onclick = function() {
        instructions.style.display = "block";
    };
    document.getElementById("share").onclick = function() {
        share.style.display = "block";
    };

    /**
     * Leaderboard and instructions close button
     */

    document.getElementsByClassName("close")[0].onclick = function() {
        leaderboard.style.display = "none";
    };
    document.getElementsByClassName("close")[1].onclick = function() {
        instructions.style.display = "none";
    };
    document.getElementsByClassName("close")[2].onclick = function() {
        share.style.display = "none";
    };

    window.onclick = function(event) {
        if (event.target == leaderboard) {
            leaderboard.style.display = "none";
        } else if (event.target == instructions) {
            instructions.style.display = "none";
        } else if (event.target == share) {
            share.style.display = "none";
        }
    };

    /**
     * Dynamically update the share sentence
     */
    function updateShare() {
        document.getElementById("share-sentence").innerHTML =
            "My score was " + score + " today!";
    }



    // function submitScore(score) {
    //     const body = new FormData();
    //     body.append("key", score);
    //     return fetch("/submit", { method: "POST", body, credentials: "include" });
    // }

    /** Code for Generating Trie:
     *  to update:
     *    modify the array in wordlist.js
     *    uncomment the below code and reload the webpage
     *    copy and paste the output from the console to the trie.js replacing everything in the {}
     */

    // const word_dict = new Trie();

    // for (let i = 0; i < wordlist.length; i++) {
    //     word_dict.insert(wordlist[i]);
    // }
    // console.log(JSON.stringify(word_dict));

    /* End of section */

    // Intialises RAW_TRIE from trie.js to a Trie datatype that can be searched at runtime
    const TRIE = Object.setPrototypeOf(RAW_TRIE, new Trie());
});

// =========================================================================================================================
// Classes

/* Trie for validating words*/
class Trie {
    constructor() {
        this.root = new TrieNode();

        this.insert = function(key) {
            let length = key.length,
                next = this.root;

            for (let i = 0; i < length; i++) {
                let character = key.charAt(i);
                if (next.c[character] == null) {
                    next.c[character] = new TrieNode();
                }

                next = next.c[character];
            }
            next.w = true;
        };

        this.search = function(key) {
            key = key.toUpperCase();
            let length = key.length,
                next = this.root;

            for (let i = 0; i < length; i++) {
                let character = key.charAt(i);

                if (next && next.c[character]) {
                    next = next.c[character];
                    continue;
                }
                return false;
            }

            return next && next.w;
        };
    }
}

class TrieNode {
    constructor() {
        this.c = {};
        this.w = false;
    }
}

class clickedLetter {
    constructor(letter, column, row) {
        this.letter = letter;
        this.column = column;
        this.row = row;
    }
}