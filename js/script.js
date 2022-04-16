function createGrid(){
      for (let i = 0; i < 6; i++) {
        var row = document.createElement("tr");
        for (let j = 0; j < 5; j++) {
          var box = document.createElement("td");
          row.appendChild(box);
        }
        table.appendChild(row);
      }
}