"use strict";

$(window).on("load", () => {
  /**
   *
   * @param {interger} numrows - The total number of cells in the grid
   */
  function createGrid(total) {
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
  }

  //Create the grid
  createGrid(40);
  TimedDrop();

  /**
   *
   */
  function createInput() {
    var input = document.getElementsByClassName("input")[0];

    for (let j = 0; j < 5; j++) {
      let inputcell = document.createElement("div");
      inputcell.className = "inputcells";
      input.appendChild(inputcell);
    }
  }

  createInput();

  //Storing every letter clicked
  // var ind = [];
  var lettersClicked = [];
  /**
   *
   * @returns a popup window alerting that the max number of letters has been used
   */
  function clickedCell() {
    //Declare it to be clicked or unclicked
    if (this.className == "unclicked") {
      if (lettersClicked.length == 5) {
        console.log("Already have 5 letters");
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

    // console.log(lettersClicked);
  }

  /**
   *
   * @param {string} word -
   * @param {integer} count -
   */
  function updateDisplay(lettersClicked) {
    let g = document.getElementsByClassName("inputcells");
    for (let i = 0; i < 5; i++) {
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
  /** Code for Generating Trie:
   *  to update:
   *    modify the array in wordlist.js
   *    uncomment the below code and reload the webpage
   *    copy and paste the output from the console to the trie.js replacing everything in the {}
   */

  // const word_dict = new Trie();

  // for (let i = 0; i < wordlist.length; i++) {
  //   word_dict.insert(wordlist[i]);
  // }
  // console.log(JSON.stringify(word_dict));

  /* End of section */

  // Intialises RAW_TRIE from trie.js to a Trie datatype that can be searched at runtime
  const TRIE = Object.setPrototypeOf(RAW_TRIE, new Trie());
  // console.log("hello exists: " + TRIE.search("treat"));
  // console.log("hello1 does not exist: " + TRIE.search("hello1"));

  //Initialising 2d array of letters on the page

  function updateGrid() {
    let col0 = [];
    let col1 = [];
    let col2 = [];
    let col3 = [];
    let col4 = [];

    for (let i = 0; i < 40; i = i + 5) {
      var cells = document.getElementsByClassName("unclicked")[i];
      col0.push(cells.innerHTML);
    }

    for (let i = 1; i < 40; i = i + 5) {
      var cells = document.getElementsByClassName("unclicked")[i];
      col1.push(cells.innerHTML);
    }

    for (let i = 2; i < 40; i = i + 5) {
      var cells = document.getElementsByClassName("unclicked")[i];
      col2.push(cells.innerHTML);
    }

    for (let i = 3; i < 40; i = i + 5) {
      var cells = document.getElementsByClassName("unclicked")[i];
      col3.push(cells.innerHTML);
    }

    for (let i = 4; i < 40; i = i + 5) {
      var cells = document.getElementsByClassName("unclicked")[i];
      col4.push(cells.innerHTML);
    }
    let arr = [col0, col1, col2, col3, col4];
  }
  // let col0 = [];
  // let col1 = [];
  // let col2 = [];
  // let col3 = [];
  // let col4 = [];

  // for (let i = 0; i < 40; i = i + 5) {
  //   var cells = document.getElementsByClassName("unclicked")[i];
  //   col0.push(cells.innerHTML);
  // }

  // for (let i = 1; i < 40; i = i + 5) {
  //   var cells = document.getElementsByClassName("unclicked")[i];
  //   col1.push(cells.innerHTML);
  // }

  // for (let i = 2; i < 40; i = i + 5) {
  //   var cells = document.getElementsByClassName("unclicked")[i];
  //   col2.push(cells.innerHTML);
  // }

  // for (let i = 3; i < 40; i = i + 5) {
  //   var cells = document.getElementsByClassName("unclicked")[i];
  //   col3.push(cells.innerHTML);
  // }

  // for (let i = 4; i < 40; i = i + 5) {
  //   var cells = document.getElementsByClassName("unclicked")[i];
  //   col4.push(cells.innerHTML);
  // }
  // let arr = [col0, col1, col2, col3, col4];

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
    }
  }
  //Submitting a possible word
  document
    .getElementById("submit-button")
    .addEventListener("click", submitWord);
  function submitWord() {
    var cells = document
      .getElementsByClassName("grid")[0]
      .getElementsByTagName("div");
    // var cells = document.getElementsByClassName("unclicked");
    let word = "";
    for (let i = 0; i < lettersClicked.length; i++) {
      word = word.concat(lettersClicked[i].letter);
    }
    
    if (TRIE.search(word)) {
      console.log("in the database");
      updateScore(word.length);
      dropdown();

      let col0 = [];
      let col1 = [];
      let col2 = [];
      let col3 = [];
      let col4 = [];

      for (let i = 0; i < 40; i = i + 5) {
        // var cells = document.getElementsByClassName("unclicked")[i];
        col0.push(cells[i].innerHTML);
      }

      for (let i = 1; i < 40; i = i + 5) {
        // var cells = document.getElementsByClassName("unclicked")[i];
        col1.push(cells[i].innerHTML);
      }

      for (let i = 2; i < 40; i = i + 5) {
        // var cells = document.getElementsByClassName("unclicked")[i];
        col2.push(cells[i].innerHTML);
      }

      for (let i = 3; i < 40; i = i + 5) {
        // var cells = document.getElementsByClassName("unclicked")[i];
        col3.push(cells[i].innerHTML);
      }

      for (let i = 4; i < 40; i = i + 5) {
        // var cells = document.getElementsByClassName("unclicked")[i];
        col4.push(cells[i].innerHTML);
      }
      let arr = [col0, col1, col2, col3, col4];
      dropdown(arr);
    } else {
      alert("Not a Word");
    }
  }

  var score = 0;
  updateScore(0);
  //Updating the score
  function updateScore (length){
    score += length;
    document.getElementById("count").innerHTML = "Score: " + score;
  }


  //Creating a timed tile drop

  var gameStart = setInterval(TimedDrop, 4000);

  function TimedDrop() {
    let total_weight = 5;
    let roll = Math.floor(Math.random() * total_weight);
    // let roll=1;

    var griddivs = document
      .getElementsByClassName("grid")[0]
      .getElementsByTagName("div");

    const letter = generateRandomLetter();

    griddivs[roll].innerHTML = letter;
    griddivs[roll].dataset.word = letter;

    for (let i = roll + 5; i < 40; i = i + 5) {
      var cell = griddivs[i];
      if (griddivs[i].innerHTML == "") {
        cell.innerHTML = letter;
        cell.dataset.word = letter;
        griddivs[i - 5].innerHTML = "";
        griddivs[i - 5].dataset.word = "";
      }
    }
    // var droppingDown = setInterval(droppingDownAnimation , 100);
    loss();
  }

  // function droppingDownAnimation(){
 
  // }

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
        clearInterval(gameStart);
        clearInterval(droppingDown);
      }
    }
  }
});

/**
 * Menu Button
 */
function menuDropdown() {
  document.getElementById("myDropdown").classList.toggle("show");
}

// =========================================================================================================================
// Classes

/* Trie for validating words*/
class Trie {
  constructor() {
    this.root = new TrieNode();

    this.insert = function (key) {
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

    this.search = function (key) {
      key = key.toLowerCase();
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
