const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input');

let telefono = document.getElementById('id_telefono');

telefono.addEventListener('keypress',(event ) => {
    event.preventDefault();
    let codigokey = event.keyCode
    console.log(codigokey)
    let valorKey = String.fromCharCode(codigokey)
    console.log(valorKey)
    
    let valor = parseInt(valorKey)
    console.log(valor)

    if(valor){
        telefono.value += valor
    }
    else if (valor || valorKey === "0"){
        (
            telefono.value += valor
            );
    }
    
})

let rut = document.getElementById('id_rut');

rut.addEventListener('keypress',(event ) => {
    event.preventDefault();
    let codigokey = event.keyCode
    console.log(codigokey)
    let valorKey = String.fromCharCode(codigokey)
    console.log(valorKey)
    
    let valor = parseInt(valorKey)
    console.log(valor)

    if(valor){
        rut.value += valor
    }
    else if (valor || valorKey === "0"){
        (
            rut.value += valor
            );
    }
    
})

function SoloLetras(e){
    key = e.keyCode || e.which;
    teclas = String.fromCharCode(key).toString();
    letras ="ABCDEFGHIJKLMNÑOPQVWXYXabcdefghijklmnñopqrstuvwxyzáéíóú"

    especiales=[8,13];
    tecla_especiales= false;
    for (var i in especiales) {
        if(key == especiales[i]){
            tecla_especiales= true;
            break;
        }
    }
    if(letras.indexOf(teclas)== -1 && !tecla_especiales){
        console.log("Ingresar solo letras")
        return false;
    }

}





const expresiones = {
	id_username: /^[a-zA-Z0-9\_\-]{4,16}$/, // Letras, numeros, guion y guion_bajo
    id_email: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
    id_rut: /^\d{8,9}$/, // 10 numeros.
	id_nombres: /^[a-zA-ZÀ-ÿ\s]{1,50}$/, // Letras y espacios, pueden llevar acentos.
    id_apellidos: /^[a-zA-ZÀ-ÿ\s]{1,50}$/, // Letras y espacios, pueden llevar acentos.
    id_telefono: /^\d{9}$/, // 9 numeros.
	id_password1: /^.{4,12}$/, // 4 a 12 digitos.
	
	
}

const campos = {
    id_username :false,
    id_email: false,
    id_rut: false,
    id_nombres: false,
    id_apellidos: false,
    id_telefono: false,
    id_password1: false,
}

const validarFormulario=(e) => {
   switch(e.target.name){
    case "username":
        validarCampo(expresiones.id_username, e.target, 'username');
    break;
    case "email":
        validarCampo(expresiones.id_email, e.target, 'email');
    break;
    case "rut":
        validarCampo(expresiones.id_rut, e.target, 'rut');
    break;
    case "nombres":
        validarCampo(expresiones.id_nombres, e.target, 'nombres');
    break;
    case "apellidos":
        validarCampo(expresiones.id_apellidos, e.target, 'apellidos');
    break;
    case "telefono":
        validarCampo(expresiones.id_telefono, e.target, 'telefono');
    break;
    case "password1":
        validarCampo(expresiones.id_password1, e.target, 'password1');
        validarPassword2();
    break;
    case "password2":
        validarPassword2();
    break;
   } 
}

const validarCampo = (expresion, input, campo) => {
	if(expresion.test(input.value)){
		document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-incorrecto');
		document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-correcto');
		document.querySelector(`#grupo__${campo} i`).classList.add('fa-check-circle');
		document.querySelector(`#grupo__${campo} i`).classList.remove('fa-times-circle');
		document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.remove('formulario__input-error-activo');
		campos[campo] = true;
	} else {
		document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-incorrecto');
		document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-correcto');
		document.querySelector(`#grupo__${campo} i`).classList.add('fa-times-circle');
		document.querySelector(`#grupo__${campo} i`).classList.remove('fa-check-circle');
		document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.add('formulario__input-error-activo');
		campos[campo] = false;
	}
}

const validarPassword2 = () =>{
    const inputPassword1 = document.getElementById('id_password1');
    const inputPassword2 = document.getElementById('id_password2');

    if (inputPassword1.value !== inputPassword2.value) {
        document.getElementById(`grupo__password2`).classList.add('formulario__grupo-incorrecto');
		document.getElementById(`grupo__password2`).classList.remove('formulario__grupo-correcto');
		document.querySelector(`#grupo__password2 i`).classList.add('fa-times-circle');
		document.querySelector(`#grupo__password2 i`).classList.remove('fa-check-circle');
		document.querySelector(`#grupo__password2 .formulario__input-error`).classList.add('formulario__input-error-activo');
        campos['id_password1'] = false;
    } else{
        document.getElementById(`grupo__password2`).classList.remove('formulario__grupo-incorrecto');
		document.getElementById(`grupo__password2`).classList.add('formulario__grupo-correcto');
		document.querySelector(`#grupo__password2 i`).classList.remove('fa-times-circle');
		document.querySelector(`#grupo__password2 i`).classList.add('fa-check-circle');
		document.querySelector(`#grupo__password2 .formulario__input-error`).classList.remove('formulario__input-error-activo');
        campos['id_password1'] = true;
    }
}

inputs.forEach((input)=>{
    input.addEventListener('keyup', validarFormulario); 
    input.addEventListener('blur', validarFormulario);
});

formulario.addEventListener('submit',(e)=>{
   

    if(campos.id_username && campos.id_email && campos.id_rut && campos.id_nombres && campos.id_apellidos && campos.id_telefono && campos.id_password1){
        formulario.reset();
    }

   
});

