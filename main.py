from pyscript import document

def verify_account(event):
    document.getElementById('result').innerHTML = ""

    user_val = document.getElementById("username").value
    pass_val = document.getElementById("password").value
    result = document.getElementById("result")

    if user_val == "" or pass_val == "":
        result.innerHTML = "Please enter both username and password."
        return

    if len(user_val) < 7:
        remaining = 7 - len(user_val)
        result.innerHTML = "Username must be at least 7 characters long. Please enter " + str(remaining) + " more character(s)."
        return

    if len(pass_val) < 10:
        remaining = 10 - len(pass_val)
        result.innerHTML = "Password must be at least 10 characters long. Please enter " + str(remaining) + " more character(s)."
        return

    has_letter = False
    has_number = False

    for char in pass_val:
        if char.isalpha():
            has_letter = True
        if char.isdigit():
            has_number = True

    if not has_letter:
        result.innerHTML = "Password must contain at least one letter."
        return

    if not has_number:
        result.innerHTML = "Password must contain at least one number."
        return

    result.innerHTML = "Account created successfully!"
