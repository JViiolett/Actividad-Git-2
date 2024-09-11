document.addEventListener("DOMContentLoaded",() => {
    const iconLock = document.querySelector(".i-lock")
    const inputContrasena = document.querySelector(".contrasena")
    const inputCorreo = document.querySelector(".correo")
    const btnIngresar = document.querySelector(".btn-login")

    btnIngresar.addEventListener("click",ingreso)
    iconLock.addEventListener("click",viewPassword)

    function viewPassword(){
        const NewName = "bx bxs-lock-open"
        let changeName = iconLock.className === NewName ? "bx bxs-lock" : NewName
        iconLock.className = changeName
        
        let type = inputContrasena.getAttribute("type")
        let changePassword = type === "password" ? "text" : "password"
        inputContrasena.setAttribute("type",changePassword)
    }

    function ingreso() {
        const infoUserValidad = [
            {
                correo: "cristianarrietar4@gmail.com",
                contrasena: "cristian1234"
            }
        ]
        infoUserValidad.forEach((i) => {
            if (inputCorreo.value === i.correo && inputContrasena.value === i.contrasena) {
                window.location.href = "../main/index.html"
            }
        })
    }
})