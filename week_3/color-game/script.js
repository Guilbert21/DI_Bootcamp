// Initialize game board and color picker
const gameBoard = document.getElementById('game-board');
const colorPicker = document.getElementById('color-picker');

// Initialize board dimensions
const rows = 16;
const cols = 16;

// Initialize selected color
let selectedColor = colorPicker.value;

// Initialize drawing flag
let isDrawing = false;

// Generate game board
for (let i = 0; i < rows; i++) {
  for (let j = 0; j < cols; j++) {
    const square = document.createElement('div');
    square.classList.add('square');
    square.addEventListener('mousedown', () => {
      isDrawing = true;
      square.style.backgroundColor = selectedColor;
    });
    square.addEventListener('mouseup', () => {
      isDrawing = false;
    });
    square.addEventListener('mouseover', () => {
      if (isDrawing) {
        square.style.backgroundColor = selectedColor;
      }
    });
    gameBoard.appendChild(square);
  }
}

// Handle color picker change event
colorPicker.addEventListener('change', (event) => {
  selectedColor = event.target.value;
});

// Handle reset button click event
const resetButton = document.getElementById('reset-button');
resetButton.addEventListener('click', () => {
  gameBoard.querySelectorAll('.square').forEach((square) => {
    square.style.backgroundColor = 'white';
  });
});
