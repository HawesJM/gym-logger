// global variables and event listeners

let validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;

document.getElementById("registered-username-input").addEventListener("change", validateRegisteredUserName);

// check registered and new user input information

function validateRegisteredUserName() {
    if (document.getElementById("registered-username-input").value.match(validRegex)) {
        $("#registered-password").removeClass("hidden");
    }
    else {
        alert("please type a valid username and hit 'enter' to login");
    }
}

    //if (document.getElementByIegistered-email-input").value != "") {
    //let reg;isteredUserEmailInput = docu.getElementById("registered-email-input").value;
   // }
    //if (registeredUserEmailInput.value.match(validRegex)) {
        //let registeredUserEmailInput = validatedRegisteredUserEmail
        //$("#registered-passwod").removeClass("hidden");
    //} else {
       // alert("please enter a valid email address to login")
    //}


//let registeredEmailInput = document.getElementById("registered-email-input");
//registeredEmailInput.addEventListener("input", validateRegisteredUserInput);

//function validateRegisteredUserEmail() {
   // let registeredUserEmailInput = document.getElementById("registered-email-input").value;
    //if (registeredUserEmailInput != "") && (registeredUserEmailInput.match(validRegex) {
       // alert("please enter a valid email address to login");
       // return false;
   // }
    //else if ("registered-email-input".value.match(validRegex)) {
      //  alert("please enter a valid email address to proceed");
  //  }
    /////else { $("#registered-password").removeClass("hidden"); }
//}
    //}
    //else { registeredUserEmailInput = registeredUserEmail; }
//}


//{ registeredUserEmailInput = registeredUserEmail; }

//if if (registeredUserEmailInput.value.match(validRegex))
//console.log("thanks")

//if (registeredUserEmailInput != "")
    //else {
    //$("#registered-password").removeClass("hidden");
        ////document.getElementById("registered-password").removeClass("hidden");