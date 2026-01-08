const form = document.getElementById("loginForm");
const message = document.getElementById("message");

form.addEventListener('submit', function (event){
    event.prevenDefault();

    const email = document.getElementById("email").value
    const senha = document.getElementById("senha").value

    if(email === "" || senha === ""){
        message.style.color = "red";
        message.textContent = "Preencha todos os campos";
        return;
    }

    if (email === "admin@email.com" && senha === "123"){
        message.style.color = "green";
        message.textContent = "Login Realizado";
        setTimeout(() => {
            window.location.href = "dashboard.html";
        }, 1000);
    } else{
        message.style.color = "red";
        message.textContent = "Email ou senha inválidos";
    }


})