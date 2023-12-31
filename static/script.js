
function passwordVerification(password) {
    if (password.length < 8) {
        return 1;
    }

    const match = password.match(/(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[?!.,@£$%&*#;:])/);

    if (match) {
        return 0;
    } else {
        return 2;
    }
}


let gi = passwordVerification('djdd')