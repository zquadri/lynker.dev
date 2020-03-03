const shrinkBtn = document.querySelector('#shrink-btn');
const successBox = document.querySelector('#success-box');
const errorBox = document.querySelector('#error-box');
const main = document.querySelector('main');
const urlInput = document.querySelector('#url-input');

//hide buttons and show loader
shrinkBtn.addEventListener('click', function() {
  shrinkBtn.classList.add('hide');

  const reqBody = {
    url: urlInput.value
  };

  const fetchConfig = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(reqBody)
  };

  fetch('/shrink', fetchConfig)
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
  box.innerHTML = text;
  box.setAttribute('id', 'success-box');
  main.appendChild(box);
}

function handleError(err) {
  console.log(err);
}
