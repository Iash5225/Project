"use strict";

$(window).on("load", () => {
  function createGrid(numrows) {
    var grid = document.getElementsByClassName("grid")[0];
    for (let i = 0; i < numrows; i++) {
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
      const letter = generateRandomLetter();

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

  function createInput() {
    var input = document.getElementsByClassName("input")[0];
    // console.log(input);
    for (let j = 0; j < 5; j++) {
      let inputcell = document.createElement("div");
      inputcell.className = "inputcells";
      input.appendChild(inputcell);
    }
  }

  createInput();

  //Storing every letter clicked
  var lettersClicked = [];
  var count = 0;
  var ind = [];

  function clickedCell() {
    if (count == 5) {
      alert("Already have 5 letters");
      return;
    }

    //Add to array
    lettersClicked.push(this.dataset.word);
    ind.push(this.row);
    ind.push(this.column);

    //Declare it to be clicked or unclicked
    if (this.className == "unclicked") {
      this.className = "clicked";
    } else {
      removeLetter(count);
      this.className = "unclicked";
    }
    // console.log(lettersClicked);
    // console.log(ind);

    //Call a function which inserts it into the input div
    addToInput(this.dataset.word, count);
    count++;
    if (lettersClicked.length == 5) {
      dropdown();
    }
  }

  function addToInput(word, count) {
    var g = document.getElementsByClassName("inputcells");
    // console.log(count);
    g[count].innerHTML = word;
  }

  //Generating a random letter
  function generateRandomLetter() {
    const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    return alphabet[Math.floor(Math.random() * alphabet.length)];
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

  //Intialises RAW_TRIE from trie.js to a Trie datatype that can be searched at runtime
  const TRIE = Object.setPrototypeOf(RAW_TRIE, new Trie());
  // console.log("hello exists: " + TRIE.search("hello"));
  // console.log("hello1 does not exist: " + TRIE.search("hello1"));

  //Initialising 2d array of letters on the page
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


  //removes the clicked letters and shifts every element down the array
  function dropdown() {
    var k = document.getElementsByClassName("clicked");
    for (let index = 0; index < 5; index++) {
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
    console.log(arr);
  }

  //TODO 
  //Iterate through divs and replace array string with inner html
  
});

/* Menu button */
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

/* Trie for validating words*/
class Trie {
  constructor() {
    this.root = new TrieNode();

    this.insert = function (key) {
      let length = key.length,
        next = this.root;

      for (let i = 0; i < length; i++) {
        let character = key.charAt(i);
        if (next.children[character] == null) {
          next.children[character] = new TrieNode();
        }

        next = next.children[character];
      }
      next.isValidWord = true;
    };

    this.search = function (key) {
      let length = key.length,
        next = this.root;

      for (let i = 0; i < length; i++) {
        let character = key.charAt(i);

        if (next && next.children[character]) {
          next = next.children[character];
          continue;
        }
        return false;
      }

      return next && next.isValidWord;
    };
  }
}

class TrieNode {
  constructor() {
    this.children = {};
    this.isValidWord = false;
  }
}
