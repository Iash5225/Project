function createGrid(numrows){
    var grid = document.getElementsByClassName("grid")[0];
      for (let i = 0; i < numrows; i++) {
        var cells = document.createElement("div");
        grid.appendChild(cells);
      }
}

createGrid(40);
