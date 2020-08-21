function submitForm(event) {
    event.preventDefault()

    let formElement = document.querySelector("form"),
      formDataInstance = new FormData(formElement),
      dataArray = {};

    for (let [field, value] of formDataInstance.entries()) {
        dataArray[field] = value;
    }

    fetch(formElement.action, {
        method: "post",
        body: JSON.stringify(dataArray),
        'Content-Type':'application/json'
    });

    formElement.reset();

    document.getElementById('alert-message').innerText = 'Thanks for connecting, we will be in touch shortly!';

    return false;
}
