function consult_user() {
    let nom_Mascota = document.getElementById("nombreMascota").value
    let nom_propietario = document.getElementById("propietario").value
    let obj_mascota = {
        "mascota": nom_Mascota,
        "propietario": nom_propietario
    }
    fetch("/consult_user", {
       "method":"post",
       "headers":{"Content-Type":"application/json"},
       "body":JSON.stringify(obj_mascota)
    })
    .then(resp => resp.json())
    .then(data => {
        alert(data)
    })
    .catch(err => {
        alert("Error")
    })
}  