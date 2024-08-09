// global variables


let validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;



//workout form event listeners //
if (document.getElementById("workout-record-container")) {
    document.getElementById("exercise-row-two-add").addEventListener("click", duplicateExerciseOne);
    document.getElementById("exercise-row-three-add").addEventListener("click", duplicateExerciseTwo);
    document.getElementById("exercise-row-four-add").addEventListener("click", duplicateExerciseThree);
    document.getElementById("exercise-row-five-add").addEventListener("click", duplicateExerciseFour);
    document.getElementById("exercise-row-six-add").addEventListener("click", duplicateExerciseFive);
    document.getElementById("exercise-row-seven-add").addEventListener("click", duplicateExerciseSix);
    document.getElementById("exercise-row-eight-add").addEventListener("click", duplicateExerciseSeven);
    

//mobile form event listeners //
    document.getElementById("workout-date-mobile-input").addEventListener("change", hideDatePicker);
    document.getElementById("workout-description-mobile").addEventListener("change", hideMobileDescription);
    document.getElementById("mobile-exercise-add-1").addEventListener("click", hideWorkoutRow1);
    document.getElementById("mobile-exercise-add-2").addEventListener("click", hideWorkoutRow2);
    document.getElementById("mobile-exercise-add-3").addEventListener("click", hideWorkoutRow3);
    document.getElementById("mobile-exercise-add-4").addEventListener("click", hideWorkoutRow4);
    document.getElementById("mobile-exercise-add-5").addEventListener("click", hideWorkoutRow5);
    document.getElementById("mobile-exercise-add-6").addEventListener("click", hideWorkoutRow6);
    document.getElementById("mobile-exercise-add-7").addEventListener("click", hideWorkoutRow7);



// record workout section 2 functions //    

function duplicateExerciseOne() {
    $("#exercise-two-container").removeClass("hidden");
    $("#exercise-row-three-add").removeClass("hidden");
    $("#exercise-row-two-add").addClass("hidden");
    $("#workout-description-block").addClass("hidden");
    $("#date-picker").addClass("hidden");
    $("#exercise-one-header").addClass("hidden");
    $("#record-workout-header").addClass("hidden");
    $("#record-workout-explainer").addClass("hidden");
    $("#workout").addClass("hidden");
    $(".exercise-one").addClass("hidden");
}  


// record workout section 3 functions //

function duplicateExerciseTwo() {
    $("#exercise-three-container").removeClass("hidden");
    $("#exercise-row-three-add").removeClass("hidden");
    $("#exercise-two-header").addClass("hidden");
    $("#exercise-two-container").addClass("hidden");
    $("#exercise-row-three-add").addClass("hidden");
    $("#exercise-row-four-add").removeClass("hidden");
}  


// record workout section 4 functions //   
function duplicateExerciseThree() {
    $("#exercise-four-container").removeClass("hidden");
    $("#exercise-row-four-add").addClass("hidden");
    $("#exercise-row-five-add").removeClass("hidden");
    $("#exercise-three-container").addClass("hidden");
}


// record workout section 5 functions //   
function duplicateExerciseFour() {
    $("#exercise-five-container").removeClass("hidden");
    $("#exercise-row-five-add").addClass("hidden");
    $("#exercise-row-six-add").removeClass("hidden");
    $("#exercise-four-container").addClass("hidden");
}

// record workout section 6 functions //   
function duplicateExerciseFive() {
    $("#exercise-six-container").removeClass("hidden");
    $("#exercise-row-six-add").addClass("hidden");
    $("#exercise-row-seven-add").removeClass("hidden");
    $("#exercise-five-container").addClass("hidden");
}

// record workout section 7 functions //   
function duplicateExerciseSix() {
    $("#exercise-seven-container").removeClass("hidden");
    $("#exercise-row-seven-add").addClass("hidden");
    $("#exercise-row-eight-add").removeClass("hidden");
    $("#exercise-six-container").addClass("hidden");
}

// record workout section 8 functions //   
function duplicateExerciseSeven() {
    $("#exercise-eight-container").removeClass("hidden");
    $("#exercise-row-eight-add").addClass("hidden");
    $("#exercise-seven-container").addClass("hidden");
}

// mobile record workout section //

function hideDatePicker() {
    $("#date-picker-mobile-container").addClass("hidden");
    let mobile_date = document.getElementById("workout-date-mobile-input").value;
    alert(`selected workout date is ${mobile_date}`);

}

function hideMobileDescription() {
    $("#mobile-description").addClass("hidden");
    let mobile_description = document.getElementById("workout-description-mobile").value; 
    alert(`workout description is ${mobile_description}`);

}

function hideWorkoutRow1() {
    $("#mobile-exercise-row-1").addClass("hidden");
    $("#mobile-exercise-row-2").removeClass("hidden");
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

function hideWorkoutRow5() {
    $("#mobile-exercise-row-5").addClass("hidden");
    $("#mobile-exercise-add-5").addClass("hidden");
    $("#mobile-exercise-row-6").removeClass("hidden");
}

function hideWorkoutRow6() {
    $("#mobile-exercise-row-6").addClass("hidden");
    $("#mobile-exercise-add-6").addClass("hidden");
    $("#mobile-exercise-row-7").removeClass("hidden");
}

function hideWorkoutRow7() {
    $("#mobile-exercise-row-7").addClass("hidden");
    $("#mobile-exercise-add-7").addClass("hidden");
    $("#mobile-exercise-row-8").removeClass("hidden");
}

}


// save workout function //

function saveWorkoutSubmit() { 
    document.getElementById("save-workout").submit(); 
} 


// flash messages //

    if (document.getElementsByClassName("flashes-timed")) {
        setTimeout(function() {
            $("#profile-flashes-container").addClass("hidden");
        }, 10000);
    }
