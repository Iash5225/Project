"use strict";

$(window).on("load", () => {
  function createGrid(numrows) {
    var grid = document.getElementsByClassName("grid")[0];
    for (let i = 0; i < numrows; i++) {
      //Create new div
      var cells = document.createElement("div");

      //Set divs created to all have a classname "cell"
      cells.className = "unclicked";

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
    console.log(input);
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

  function clickedCell() {
    if (count == 5) {
      alert("Already have 5 letters");
      return;
    }

    //Add to array
    lettersClicked.push(this.dataset.word);

    //Declare it to be clicked or unclicked
    if (this.className == "unclicked") {
      this.className = "clicked";
    } else {
      removeLetter(count);
      this.className = "unclicked";
    }
    console.log(lettersClicked);

    //Call a function which inserts it into the input div
    addToInput(this.dataset.word, count);
    count++;
  }

  function addToInput(word, count) {
    var g = document.getElementsByClassName("inputcells");
    console.log(count);
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


  // Intialises RAW_TRIE from trie.js to a Trie datatype that can be searched at runtime
  const TRIE = Object.setPrototypeOf(RAW_TRIE, new Trie());
  console.log("hello exists: " + TRIE.search("hello"));
  console.log("hello1 does not exist: " + TRIE.search("hello1"));

  
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
        if (next.c[character] == null) {
          next.c[character] = new TrieNode();
        }

        next = next.c[character];
      }
      next.w = true;
    };

    this.search = function (key) {
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
