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
document.getElementById("modifier-add-two").addEventListener("click", duplicateModifierTwo);
document.getElementById("total-add-two").addEventListener("click", duplicateTotalTwo);
document.getElementById("exercise-add-three").addEventListener("click", duplicateExerciseThree);
document.getElementById("category-add-three").addEventListener("click", duplicateCategoryThree);
document.getElementById("modifier-add-three").addEventListener("click", duplicateModifierThree);
document.getElementById("total-add-three").addEventListener("click", duplicateTotalThree)
document.getElementById("exercise-add-four").addEventListener("click", duplicateExerciseFour);
document.getElementById("category-add-four").addEventListener("click", duplicateCategoryFour);
document.getElementById("modifier-add-four").addEventListener("click", duplicateModifierFour);
document.getElementById("total-add-four").addEventListener("click", duplicateTotalFour);

// check registered and new user input information //

function validateRegisteredUserName() {
        $("#registered-password").removeClass("hidden");
    }

// record workout section 2 functions //    

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

// record workout section 3 functions //   

function duplicateExerciseTwo() {
    $("#exercise-three-container").removeClass("hidden");
    $("#exercise-add-two").addClass("hidden");
}  

function duplicateCategoryTwo() {
    $("#category-three-container").removeClass("hidden");
    $("#category-add-two").addClass("hidden");
}

function duplicateModifierTwo() {
    $("#modifier-three-container").removeClass("hidden");
    $("#modifier-add-two").addClass("hidden");
}


function duplicateTotalTwo() {
    $("#total-three-container").removeClass("hidden");
    $("#total-add-two").addClass("hidden");
}

// record workout section 4 functions //   

function duplicateExerciseThree() {
    $("#exercise-four-container").removeClass("hidden");
    $("#exercise-add-three").addClass("hidden");
}  

function duplicateCategoryThree() {
    $("#category-four-container").removeClass("hidden");
    $("#category-add-three").addClass("hidden");
}

function duplicateModifierThree() {
    $("#modifier-four-container").removeClass("hidden");
    $("#modifier-add-three").addClass("hidden");
}

function duplicateTotalThree() {
    $("#total-four-container").removeClass("hidden");
    $("#total-add-three").addClass("hidden");
}

// record workout section 5 functions //   

function duplicateExerciseFour() {
    $("#exercise-five-container").removeClass("hidden");
    $("#exercise-add-four").addClass("hidden");
}  

function duplicateCategoryFour() {
    $("#category-five-container").removeClass("hidden");
    $("#category-add-four").addClass("hidden");
}

function duplicateModifierFour() {
    $("#modifier-five-container").removeClass("hidden");
    $("#modifier-add-four").addClass("hidden");
}

function duplicateTotalFour() {
    $("#total-five-container").removeClass("hidden");
    $("#total-add-four").addClass("hidden");
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

