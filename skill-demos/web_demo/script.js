const button = document.querySelector('#run');
const result = document.querySelector('#result');

button.addEventListener('click', () => {
  const score = (0.75 + Math.random() * 0.2).toFixed(3);
  result.textContent = `Sample accuracy: ${score}`;
});
