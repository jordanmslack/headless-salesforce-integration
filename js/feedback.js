function submitForm(event) {
    event.preventDefault()

	let url_string = window.location.href
	let url = new URL(url_string);
	let case_id = url.searchParams.get("case_id");

    let formElement = document.querySelector("form"),
      formDataInstance = new FormData(formElement),
      dataArray = {};

    dataArray['case_id'] = case_id

    for (let [field, value] of formDataInstance.entries()) {
        dataArray[field] = value;
    }

    fetch(formElement.action, {
        method: "post",
        body: JSON.stringify(dataArray),
        'Content-Type':'application/json'
    });

    formElement.reset();

    document.getElementById('alert-message').innerText = 'Thanks for your feedback!';

    return false;
}