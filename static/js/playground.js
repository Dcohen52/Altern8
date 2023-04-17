// Constants
const notebookContainer = document.querySelector('.notebook-container');

// Function to clear the input and output of the first cell
function clearCell() {
  document.querySelector("#input-1").value = "";
  document.querySelector("#output-1").innerHTML = "";
}

function Docs() {
  document.querySelector("#output-1").innerHTML = `Welcome to Altern8's docs!
  
General:
Altern8 is a unique blend of different programming paradigms. 
It has the familiarity of JavaScript in terms of reserved words and the structured coding flow of C++. 
Altern8 is kind of a mix of JavaScript, Python, and C++. 

For now, Altern8 support only double-quotes ("), we currently working on support for (') single-quotes.

Commands:
  Built-in functions:
      -------------------------GENERAL------------------------
    - clear(): Clean the screen - Linux/macOS/Web systems.
    - cls(): Clear the screen - Windows/Web systems.
    - null(): Return nothing.
    
      -----------------------PRINT & VAR----------------------
    - print({something}, "{divider}"): Print something to the console.
    - Variable declaration: var x = 5, for example.
    
      ------------------------CHECKING------------------------
    - is_num(): Returns boolean value whether the input is a num or not (0/1).
    - is_str(): Returns boolean value whether the input is a string or not (0/1).
    - is_list(): Returns boolean value whether the input is a list or not (0/1).
    - is_func(): Returns boolean value whether the input is a function or not (0/1).
    
      -------------------------LISTS--------------------------
    - append(): Appends to list.
    - len(): Return the length of the variable.
    - pop(): Remove item from a list.
    - extend(): Combine two lists.
    
      -------------------------READ---------------------------
    - read(): Read string input from the user. 
    - read_int(): Read numerical input from the user. 

  General:
    - docs: Enter the documentation.
    - close/quit: Close the interpreter CLI.
  `;
}

// Function to execute code in a cell
function runCode(id) {
  const input = document.getElementById(`input-${id}`).value.trim();

  if (input === '') {
    document.getElementById(`output-${id}`).innerHTML = 'Input field is empty. Please enter some code and try again.';
    return;
  }

  document.querySelector("#output-1").style.display = "block";

  fetch('/execute', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ code: input })
  })
    .then(response => response.json())
    .then(data => {
      document.getElementById(`output-${id}`).innerHTML = data.output;
    })
    .catch(error => {
      console.error('Error:', error);
    });
}


// get the modal element and the submit button
var modal = document.getElementById("inputModal");
var submitBtn = document.getElementById("modal-submit");

// // add an event listener to the run button
document.getElementById("run-button").addEventListener("click", function () {
  const id = 1;
  // check if the code contains read() or read_int()
  var code = document.getElementById(`input-${id}`).value;
  if (code.includes("read()") || code.includes("read_int()")) {
    // show the modal
    modal.style.display = "block";

    // when the submit button is clicked, add the value to the code and run it
    submitBtn.onclick = function () {
      var value = document.getElementById("modal-input").value;
      code = code.replace("read()", value);
      code = code.replace("read_int()", parseInt(value));
      document.getElementById(`input-${id}`).value = code;
      modal.style.display = "none";
      runCode(id);
      // immediately change the code in the textarea to read or read_int again
      document.getElementById(`input-${id}`).value = code.replace(value, "read()");
      document.getElementById(`input-${id}`).value = code.replace(parseInt(value), "read_int()");
    }
  } else {
    // if read() or read_int() are not present, just run the code
    runCode(id);
  }
});

// ace editor
// var editor = ace.edit("editor");
// editor.setTheme("ace/theme/twilight");
// editor.session.setMode("ace/mode/javascript");
// add an event listener to the run button
// document.getElementById("run-btn").addEventListener("click", function() {
//   const id = 1;
//   // check if the code contains read() or read_int()
//   var code = document.getElementById(`editor`).value;
//   if (code.includes("read()") || code.includes("read_int()")) {
//     // show the modal
//     modal.style.display = "block";

//     // when the submit button is clicked, add the value to the code and run it
//     submitBtn.onclick = function() {
//       var value = document.getElementById("modal-input").value;
//       code = code.replace("read()", value);
//       code = code.replace("read_int()", parseInt(value));
//       document.getElementById(`editor`).value = code;
//       modal.style.display = "none";
//       runCode(id);
//       // immediately change the code in the textarea to read or read_int again
//       document.getElementById(`editor`).value = code.replace(value, "read()");
//       document.getElementById(`editor`).value = code.replace(parseInt(value), "read_int()");
//     }
//   } else {
//     // if read() or read_int() are not present, just run the code
//     runCode(id);
//   }
// });



// when the user clicks the close button or outside the modal, close the modal

var closeBtn = document.getElementsByClassName("close")[0];
window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
closeBtn.onclick = function () {
  modal.style.display = "none";
}





// examples
// get the modal element and the submit button
function Examples() {
  var modal = document.getElementById("examplesModal");
  var closeBtn = document.getElementsByClassName("close")[0];

  document.getElementById("examples-btn").addEventListener("click", function () {
    modal.style.display = "block";
  });

  window.onclick = function (event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  };

  closeBtn.addEventListener("click", function () {
    modal.style.display = "none";
  });
}
