const btn = document.querySelector('#shrink-btn');
const succsessBox = document.querySelector('#success-box');
const errorBox = document.querySelector('#error-box');
const main = document.querySelector('main');
btn.addEventListener('click', function() {
  fetch('/shrink', { method: 'POST' })
    .then(handleResponse)
    .then(handleText)
    .catch(handleError);
});

function handleResponse(res) {
  return res.text();
}

function handleText(text) {
  if (document.getElementById('success-box')) {
    document.getElementById('success-box').remove();
  }
  let box = document.createElement('div');
  box.textContent = text;
  box.setAttribute('id', 'success-box');
  main.appendChild(box);
}

function handleError(err) {
  console.log(err);
}
