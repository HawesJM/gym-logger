// global variables


let validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;



//workout form event listeners //
if (document.getElementById("workout-record-container")) {
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


//mobile form event listeners //
    document.getElementById("workout-date-mobile-input").addEventListener("change", hideDatePicker)
    document.getElementById("workout-description-mobile").addEventListener("change", hideMobileDescription)
    document.getElementById("mobile-exercise-add-1").addEventListener("click", hideWorkoutRow1)
    document.getElementById("mobile-exercise-add-2").addEventListener("click", hideWorkoutRow2)
    document.getElementById("mobile-exercise-add-3").addEventListener("click", hideWorkoutRow3)
    document.getElementById("mobile-exercise-add-4").addEventListener("click", hideWorkoutRow4)


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

function saveWorkoutSubmit() { 
    document.getElementById("save-workout").submit(); 
} 

// mobile record workout section //

function hideDatePicker() {
    $("#date-picker-mobile-container").addClass("hidden");
    let mobile_date = document.getElementById("workout-date-mobile-input").value 
    alert(`selected workout date is ${mobile_date}`)

}

function hideMobileDescription() {
    $("#mobile-description").addClass("hidden");
    let mobile_description = document.getElementById("workout-description-mobile").value 
    alert(`workout description is ${mobile_description}`)

}

function hideWorkoutRow1() {
    $("#mobile-exercise-row-1").addClass("hidden");
    $("#mobile-exercise-row-2").removeClass("hidden");;
}

function hideWorkoutRow2() {
    $("#mobile-exercise-row-2").addClass("hidden");
    $("#mobile-exercise-add-2").addClass("hidden");
    $("#mobile-exercise-row-3").removeClass("hidden");
}

function hideWorkoutRow3() {
    $("#mobile-exercise-row-3").addClass("hidden");
    $("#mobile-exercise-add-3").addClass("hidden");
    $("#mobile-exercise-row-4").removeClass("hidden");
}

function hideWorkoutRow4() {
    $("#mobile-exercise-row-4").addClass("hidden");
    $("#mobile-exercise-add-4").addClass("hidden");
    $("#mobile-exercise-row-5").removeClass("hidden");
}

};

// flash messages //

    if (document.getElementsByClassName("flashes-timed")) {
        setTimeout(function() {
            $("#profile-flashes-container").addClass("hidden");
        }, 10000);
    }
