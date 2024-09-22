// global variables


let validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;


// profile page //

var today_date = new Date().toLocaleDateString()

let objToday = new Date(),
	weekday = new Array('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'),
	dayOfWeek = weekday[objToday.getDay()],
	domEnder = function() { var a = objToday; if (/1/.test(parseInt((a + "").charAt(0)))) return "th"; a = parseInt((a + "").charAt(1)); return 1 == a ? "st" : 2 == a ? "nd" : 3 == a ? "rd" : "th" }(),
	dayOfMonth = ( objToday.getDate() < 10) ? '0' + objToday.getDate() + domEnder : objToday.getDate() + domEnder,
	months = new Array('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'),
	curMonth = months[objToday.getMonth()],
	curYear = objToday.getFullYear(),
	curHour = objToday.getHours() > 12 ? objToday.getHours() - 12 : (objToday.getHours() < 10 ? "0" + objToday.getHours() : objToday.getHours()),
	curMinute = objToday.getMinutes() < 10 ? "0" + objToday.getMinutes() : objToday.getMinutes(),
	curSeconds = objToday.getSeconds() < 10 ? "0" + objToday.getSeconds() : objToday.getSeconds(),
	curMeridiem = objToday.getHours() > 12 ? "PM" : "AM";

let today = curHour + ":" + curMinute + "." + curSeconds + curMeridiem + " " + dayOfWeek + " " + dayOfMonth + " of " + curMonth + ", " + curYear;

// document.getElementById("today-date-month").innerHTML = curMonth;
if (document.getElementById("current-month-record")) {
    document.getElementById("current-month-record").append(curMonth);
    console.log(curMonth)
}



//workout form event listeners //
if (document.getElementById("workout-record-container")) {
    document.getElementById("exercise-row-two-add").addEventListener("click", duplicateExerciseOne);
    document.getElementById("exercise-row-three-add").addEventListener("click", duplicateExerciseTwo);
    document.getElementById("exercise-row-four-add").addEventListener("click", duplicateExerciseThree);
    document.getElementById("exercise-row-five-add").addEventListener("click", duplicateExerciseFour);
    document.getElementById("exercise-row-six-add").addEventListener("click", duplicateExerciseFive);
    document.getElementById("exercise-row-seven-add").addEventListener("click", duplicateExerciseSix);
    document.getElementById("exercise-row-eight-add").addEventListener("click", duplicateExerciseSeven);
    document.getElementById("category").addEventListener("change", selectCategoryOne);
    document.getElementById("category-two").addEventListener("change", selectCategoryTwo);
    document.getElementById("category-three").addEventListener("change", selectCategoryThree);
    document.getElementById("category-four").addEventListener("change", selectCategoryFour);
    document.getElementById("category-five").addEventListener("change", selectCategoryFive);
    document.getElementById("category-six").addEventListener("change", selectCategorySix);
    document.getElementById("category-seven").addEventListener("change", selectCategorySeven);
    document.getElementById("category-eight").addEventListener("change", selectCategoryEight);
    

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
    document.getElementById("mobile-category").addEventListener("change", selectMobileCategoryOne);
    document.getElementById("mobile-category-two").addEventListener("change", selectMobileCategoryTwo);
    document.getElementById("mobile-category-three").addEventListener("change", selectMobileCategoryThree);
    document.getElementById("mobile-category-four").addEventListener("change", selectMobileCategoryFour);
    document.getElementById("mobile-category-five").addEventListener("change", selectMobileCategoryFive);
    document.getElementById("mobile-category-six").addEventListener("change", selectMobileCategorySix);
    document.getElementById("mobile-category-seven").addEventListener("change", selectMobileCategorySeven);
    document.getElementById("mobile-category-eight").addEventListener("change", selectMobileCategoryEight);




// dropdown functions  //   

function selectCategoryOne() {    
    let categoryOne = document.getElementById("category").value;
    if (categoryOne == "Weightlifting") {
        $(".weightlifting-option").removeClass("hidden")
        $(".cardio-option").addClass("hidden")
        $(".calisthenics-option").addClass("hidden")
    }
    if (categoryOne == "Cardio") {
        $(".cardio-option").removeClass("hidden")
        $(".weightlifting-option").addClass("hidden")
        $(".calisthenics-option").addClass("hidden")
    }
    if (categoryOne == "Calisthenics") {
        $(".calisthenics-option").removeClass("hidden")
        $(".weightlifting-option").addClass("hidden")
        $(".cardio-option").addClass("hidden")
    }
}

function selectCategoryTwo() {
    let categoryTwo = document.getElementById("category-two").value;
    if (categoryTwo == "Weightlifting") {
        $(".weightlifting-option").removeClass("hidden")
        $(".cardio-option").addClass("hidden")
        $(".calisthenics-option").addClass("hidden")
    }
    if (categoryTwo == "Cardio") {
        $(".cardio-option").removeClass("hidden")
        $(".weightlifting-option").addClass("hidden")
        $(".calisthenics-option").addClass("hidden")
    }
    if (categoryTwo == "Calisthenics") {
        $(".calisthenics-option").removeClass("hidden")
        $(".weightlifting-option").addClass("hidden")
        $(".cardio-option").addClass("hidden")
    }
}

function selectCategoryThree() {
    let categoryThree = document.getElementById("category-three").value;
    if (categoryThree == "Weightlifting") {
        $(".weightlifting-option").removeClass("hidden")
        $(".cardio-option").addClass("hidden")
        $(".calisthenics-option").addClass("hidden")
    }
    if (categoryThree == "Cardio") {
        $(".cardio-option").removeClass("hidden")
        $(".weightlifting-option").addClass("hidden")
        $(".calisthenics-option").addClass("hidden")
    }
    if (categoryThree == "Calisthenics") {
        $(".calisthenics-option").removeClass("hidden")
        $(".weightlifting-option").addClass("hidden")
        $(".cardio-option").addClass("hidden")
    }
}

function selectCategoryFour() {
    let categoryFour = document.getElementById("category-four").value;
    if (categoryFour == "Weightlifting") {
        $(".weightlifting-option").removeClass("hidden")
        $(".cardio-option").addClass("hidden")
        $(".calisthenics-option").addClass("hidden")
    }
    if (categoryFour == "Cardio") {
        $(".cardio-option").removeClass("hidden")
        $(".weightlifting-option").addClass("hidden")
        $(".calisthenics-option").addClass("hidden")
    }
    if (categoryFour == "Calisthenics") {
        $(".calisthenics-option").removeClass("hidden")
        $(".weightlifting-option").addClass("hidden")
        $(".cardio-option").addClass("hidden")
    }
}

function selectCategoryFive() {
    let categoryFive = document.getElementById("category-five").value;
    if (categoryFive == "Weightlifting") {
        $(".weightlifting-option").removeClass("hidden")
        $(".cardio-option").addClass("hidden")
        $(".calisthenics-option").addClass("hidden")
    }
    if (categoryFive == "Cardio") {
        $(".cardio-option").removeClass("hidden")
        $(".weightlifting-option").addClass("hidden")
        $(".calisthenics-option").addClass("hidden")
    }
    if (categoryFive == "Calisthenics") {
        $(".calisthenics-option").removeClass("hidden")
        $(".weightlifting-option").addClass("hidden")
        $(".cardio-option").addClass("hidden")
    }
}

function selectCategorySix() {
    let categorySix = document.getElementById("category-six").value;
    if (categorySix == "Weightlifting") {
        $(".weightlifting-option").removeClass("hidden")
        $(".cardio-option").addClass("hidden")
        $(".calisthenics-option").addClass("hidden")
    }
    if (categorySix == "Cardio") {
        $(".cardio-option").removeClass("hidden")
        $(".weightlifting-option").addClass("hidden")
        $(".calisthenics-option").addClass("hidden")
    }
    if (categorySix == "Calisthenics") {
        $(".calisthenics-option").removeClass("hidden")
        $(".weightlifting-option").addClass("hidden")
        $(".cardio-option").addClass("hidden")
    }
}

function selectCategorySeven() {
    let categorySeven = document.getElementById("category-seven").value;
    if (categorySeven == "Weightlifting") {
        $(".weightlifting-option").removeClass("hidden")
        $(".cardio-option").addClass("hidden")
        $(".calisthenics-option").addClass("hidden")
    }
    if (categorySeven == "Cardio") {
        $(".cardio-option").removeClass("hidden")
        $(".weightlifting-option").addClass("hidden")
        $(".calisthenics-option").addClass("hidden")
    }
    if (categorySeven == "Calisthenics") {
        $(".calisthenics-option").removeClass("hidden")
        $(".weightlifting-option").addClass("hidden")
        $(".cardio-option").addClass("hidden")
    }
}

function selectCategoryEight() {
    let categoryEight = document.getElementById("category-eight").value;
    if (categoryEight == "Weightlifting") {
        $(".weightlifting-option").removeClass("hidden")
        $(".cardio-option").addClass("hidden")
        $(".calisthenics-option").addClass("hidden")
    }
    if (categoryEight == "Cardio") {
        $(".cardio-option").removeClass("hidden")
        $(".weightlifting-option").addClass("hidden")
        $(".calisthenics-option").addClass("hidden")
    }
    if (categoryEight == "Calisthenics") {
        $(".calisthenics-option").removeClass("hidden")
        $(".weightlifting-option").addClass("hidden")
        $(".cardio-option").addClass("hidden")
    }
}

// mobile dropdown functions  // 

function selectMobileCategoryOne() {    
    let mobileCategoryOne = document.getElementById("mobile-category").value;
    if (mobileCategoryOne == "Weightlifting") {
        $(".weightlifting-option").removeClass("hidden")
        $(".cardio-option").addClass("hidden")
        $(".calisthenics-option").addClass("hidden")
        console.log(mobileCategoryOne)
    }
    if (mobileCategoryOne == "Cardio") {
        $(".cardio-option").removeClass("hidden")
        $(".weightlifting-option").addClass("hidden")
        $(".calisthenics-option").addClass("hidden")
        console.log(mobileCategoryOne)
    }
    if (mobileCategoryOne == "Calisthenics") {
        $(".calisthenics-option").removeClass("hidden")
        $(".weightlifting-option").addClass("hidden")
        $(".cardio-option").addClass("hidden")
        console.log(mobileCategoryOne)
    }
}


function selectMobileCategoryTwo() {    
    let mobileCategoryTwo = document.getElementById("mobile-category-two").value;
    if (mobileCategoryTwo == "Weightlifting") {
        $(".weightlifting-option").removeClass("hidden")
        $(".cardio-option").addClass("hidden")
        $(".calisthenics-option").addClass("hidden")
        console.log(mobileCategoryTwo)
    }
    if (mobileCategoryTwo == "Cardio") {
        $(".cardio-option").removeClass("hidden")
        $(".weightlifting-option").addClass("hidden")
        $(".calisthenics-option").addClass("hidden")
        console.log(mobileCategoryTwo)
    }
    if (mobileCategoryTwo == "Calisthenics") {
        $(".calisthenics-option").removeClass("hidden")
        $(".weightlifting-option").addClass("hidden")
        $(".cardio-option").addClass("hidden")
        console.log(mobileCategoryTwo)
    }
}

function selectMobileCategoryThree() {    
    let mobileCategoryThree = document.getElementById("mobile-category-three").value;
    if (mobileCategoryThree == "Weightlifting") {
        $(".weightlifting-option").removeClass("hidden")
        $(".cardio-option").addClass("hidden")
        $(".calisthenics-option").addClass("hidden")
        console.log(mobileCategoryThree)
    }
    if (mobileCategoryThree == "Cardio") {
        $(".cardio-option").removeClass("hidden")
        $(".weightlifting-option").addClass("hidden")
        $(".calisthenics-option").addClass("hidden")
        console.log(mobileCategoryThree)
    }
    if (mobileCategoryThree == "Calisthenics") {
        $(".calisthenics-option").removeClass("hidden")
        $(".weightlifting-option").addClass("hidden")
        $(".cardio-option").addClass("hidden")
        console.log(mobileCategoryThree)
    }
}

function selectMobileCategoryFour() {    
    let mobileCategoryFour = document.getElementById("mobile-category-four").value;
    if (mobileCategoryFour == "Weightlifting") {
        $(".weightlifting-option").removeClass("hidden")
        $(".cardio-option").addClass("hidden")
        $(".calisthenics-option").addClass("hidden")
        console.log(mobileCategoryFour)
    }
    if (mobileCategoryFour == "Cardio") {
        $(".cardio-option").removeClass("hidden")
        $(".weightlifting-option").addClass("hidden")
        $(".calisthenics-option").addClass("hidden")
        console.log(mobileCategoryFour)
    }
    if (mobileCategoryFour == "Calisthenics") {
        $(".calisthenics-option").removeClass("hidden")
        $(".weightlifting-option").addClass("hidden")
        $(".cardio-option").addClass("hidden")
        console.log(mobileCategoryFour)
    }
}

function selectMobileCategoryFive() {    
    let mobileCategoryFive = document.getElementById("mobile-category-five").value;
    if (mobileCategoryFive == "Weightlifting") {
        $(".weightlifting-option").removeClass("hidden")
        $(".cardio-option").addClass("hidden")
        $(".calisthenics-option").addClass("hidden")
        console.log(mobileCategoryFive)
    }
    if (mobileCategoryFive == "Cardio") {
        $(".cardio-option").removeClass("hidden")
        $(".weightlifting-option").addClass("hidden")
        $(".calisthenics-option").addClass("hidden")
        console.log(mobileCategoryFive)
    }
    if (mobileCategoryFive == "Calisthenics") {
        $(".calisthenics-option").removeClass("hidden")
        $(".weightlifting-option").addClass("hidden")
        $(".cardio-option").addClass("hidden")
        console.log(mobileCategoryFive)
    }
}

function selectMobileCategorySix() {    
    let mobileCategorySix = document.getElementById("mobile-category-six").value;
    if (mobileCategorySix == "Weightlifting") {
        $(".weightlifting-option").removeClass("hidden")
        $(".cardio-option").addClass("hidden")
        $(".calisthenics-option").addClass("hidden")
        console.log(mobileCategorySix)
    }
    if (mobileCategorySix == "Cardio") {
        $(".cardio-option").removeClass("hidden")
        $(".weightlifting-option").addClass("hidden")
        $(".calisthenics-option").addClass("hidden")
        console.log(mobileCategorySix)
    }
    if (mobileCategorySix == "Calisthenics") {
        $(".calisthenics-option").removeClass("hidden")
        $(".weightlifting-option").addClass("hidden")
        $(".cardio-option").addClass("hidden")
        console.log(mobileCategorySix)
    }
}

function selectMobileCategorySeven() {    
    let mobileCategorySeven = document.getElementById("mobile-category-seven").value;
    if (mobileCategorySeven == "Weightlifting") {
        $(".weightlifting-option").removeClass("hidden")
        $(".cardio-option").addClass("hidden")
        $(".calisthenics-option").addClass("hidden")
        console.log(mobileCategorySeven)
    }
    if (mobileCategorySeven == "Cardio") {
        $(".cardio-option").removeClass("hidden")
        $(".weightlifting-option").addClass("hidden")
        $(".calisthenics-option").addClass("hidden")
        console.log(mobileCategorySeven)
    }
    if (mobileCategorySeven == "Calisthenics") {
        $(".calisthenics-option").removeClass("hidden")
        $(".weightlifting-option").addClass("hidden")
        $(".cardio-option").addClass("hidden")
        console.log(mobileCategorySeven)
    }
}

function selectMobileCategoryEight() {    
    let mobileCategoryEight = document.getElementById("mobile-category-eight").value;
    if (mobileCategoryEight == "Weightlifting") {
        $(".weightlifting-option").removeClass("hidden")
        $(".cardio-option").addClass("hidden")
        $(".calisthenics-option").addClass("hidden")
        console.log(mobileCategoryEight)
    }
    if (mobileCategoryEight == "Cardio") {
        $(".cardio-option").removeClass("hidden")
        $(".weightlifting-option").addClass("hidden")
        $(".calisthenics-option").addClass("hidden")
        console.log(mobileCategoryEight)
    }
    if (mobileCategoryEight == "Calisthenics") {
        $(".calisthenics-option").removeClass("hidden")
        $(".weightlifting-option").addClass("hidden")
        $(".cardio-option").addClass("hidden")
        console.log(mobileCategoryEight)
    }
}

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
