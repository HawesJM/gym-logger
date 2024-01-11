// global variables and event listeners


let validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;

// document.getElementById("registered-username-input").addEventListener("change", validateRegisteredUserName);//

//event listeners //

document.getElementById("exercise-add").addEventListener("click", duplicateExerciseOne);
document.getElementById("category-add").addEventListener("click", duplicateCategoryOne);
document.getElementById("modifier-add").addEventListener("click", duplicateModifierOne);
document.getElementById("total-add").addEventListener("click", duplicateTotalOne);
document.getElementById("exercise-add-two").addEventListener("click", duplicateExerciseTwo);
document.getElementById("category-add-two").addEventListener("click", duplicateCategoryTwo);


// check registered and new user input information //

function validateRegisteredUserName() {
        $("#registered-password").removeClass("hidden");
    }

// record workout section 1 functions //    

function duplicateExerciseOne() {
    $("#exercise-two-container").removeClass("hidden");
    $("#exercise-add").addClass("hidden");
}  

function duplicateCategoryOne() {
    $("#category-two-container").removeClass("hidden");
    $("#category-add").addClass("hidden");
}

function duplicateModifierOne() {
    $("#modifier-two-container").removeClass("hidden");
    $("#modifier-add").addClass("hidden");
}

function duplicateTotalOne() {
    $("#total-two-container").removeClass("hidden");
    $("#total-add").addClass("hidden");
}

// record workout section 2 functions //   

function duplicateExerciseTwo() {
    $("#exercise-three-container").removeClass("hidden");
    $("#exercise-add-two").addClass("hidden");
}  

function duplicateCategoryTwo() {
    $("#category-three-container").removeClass("hidden");
    $("#category-add-three").addClass("hidden");
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
    //$("#registered-password").removeClass("hidden"); ////document.getElementById("registered-password").removeClass("hidden");

