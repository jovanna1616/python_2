let errorMessages = document.getElementsByClassName('error-message-content')
if (errorMessages.length) {
    setTimeout(() => {
        errorMessages[0].classList.add('hidden')
    }, 3000);
}
