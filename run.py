# required imports

import os
from flask import (Flask, flash, render_template,
                   redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)

# app routes

# homepage route with example workouts from database


@app.route("/")
@app.route("/index")
def index():
    workouts = mongo.db.workouts.find().sort("date", -1).limit(3)
    return render_template("index.html", workouts=workouts)


# more information page route
@app.route("/more_information")
def more_information():
    return render_template("more_information.html")

# full workout list from database


@app.route("/workouts")
def workouts():
    workouts = list(mongo.db.workouts.find())
    return render_template("workouts.html", workouts=workouts)

# to show a list of exercise categories


@app.route("/categories")
def categories():
    categories = list(mongo.db.categories.find().sort("category_name"))
    return render_template("categories.html", categories=categories)

# user registration function


@app.route("/register",  methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in users collection in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

    # acts as the else statement if no existing user is found to create user
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

    # puts the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


# user sign-in function

@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Login Successful!")
                return redirect
                (url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("sign_in"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("sign_in"))

    return render_template("sign_in.html")

# function to display the current user's profile with saved information


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab session user's username from db
    workouts = list(mongo.db.workouts.find())
    planned_workouts = list(mongo.db.planned_workouts.find())
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        return render_template(
            "profile.html", username=username, workouts=workouts,
            planned_workouts=planned_workouts)

    return redirect(url_for("sign_in"))

# sign in function


@app.route("/sign_out")
def sign_out():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("sign_in"))

# create workout record function


@app.route("/record_workout", methods=["GET", "POST"])
def record_workout():
    if request.method == "POST":
        is_visible = "on" if request.form.get("is-visible") else "off"
        logged_workout = {
            "date": request.form.get
            ("workout-date"),
            "workout_description": request.form.get("workout-description"),
            "workout_container_description": request.form.get
            ("workout-description").replace(" ", ""),
            "created_by": session["user"],
            "exercise": request.form.get("exercise"),
            "exercise2": request.form.get("exercise-two"),
            "exercise3": request.form.get("exercise-three"),
            "exercise4": request.form.get("exercise-four"),
            "exercise5": request.form.get("exercise-five"),
            "category": request.form.get("category"),
            "category2": request.form.get("category-two"),
            "category3": request.form.get("category-three"),
            "category4": request.form.get("category-four"),
            "category5": request.form.get("category-five"),
            "modifier": request.form.get("modifier"),
            "modifier2": request.form.get("modifier-two"),
            "modifier3": request.form.get("modifier-three"),
            "modifier4": request.form.get("modifier-four"),
            "modifier5": request.form.get("modifier-five"),
            "total": request.form.get(str("total")),
            "total2": request.form.get(str("total-two")),
            "total3": request.form.get(str("total-three")),
            "total4": request.form.get(str("total-four")),
            "total5": request.form.get(str("total-five")),
            "is_visible": is_visible,
            "additional_information": request.form.get
            ("additional-information"),
            "saved_by": [],
            "unsaved_by": [],

        }

        # ensures key fields are not recorded as empty
        for key in logged_workout.keys():
            if logged_workout[key]:
                logged_workout[key] = logged_workout[key].lower()

        logged_exercise = {
            "exercise": request.form.get("exercise"),
            "created_by": session["user"],
        }

        logged_category = {
            "category": request.form.get("category"),
            "created_by": session["user"],
        }
        mongo.db.workouts.insert_one(logged_workout)
        mongo.db.exercises.insert_one(logged_exercise)
        mongo.db.categories.insert_one(logged_category)
        flash("Workout successfully logged!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("record_workout.html")

# for adding workout categories to the database


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category": request.form.get("category")
        }
        mongo.db.categories.insert_one(category)

    return render_template("add_workout.html")


@app.route("/add_exercise", methods=["GET", "POST"])
def add_exercise():
    if request.method == "POST":
        exercise = {
            "exercise": request.form.get("exercise")
        }
        mongo.db.categories.insert_one(exercise)

    return render_template("add_workout.html")

# for editing an existing workout in the database


@app.route("/edit_workout/<workout_id>", methods=["GET", "POST"])
def edit_workout(workout_id):
    workout = mongo.db.workouts.find_one({"_id": ObjectId(workout_id)})
    workouts = list(mongo.db.workouts.find())
    is_visible = "on" if request.form.get("is-visible") else "off"
    if request.method == "POST":
        submit = {
            "date": request.form.get("workout-date"),
            "workout_description": request.form.get("workout-description"),
            "workout_container_description": request.form.get
            ("workout-description").replace(" ", ""),
            "created_by": session["user"],
            "exercise": request.form.get("exercise"),
            "exercise2": request.form.get("exercise-two"),
            "exercise3": request.form.get("exercise-three"),
            "exercise4": request.form.get("exercise-four"),
            "exercise5": request.form.get("exercise-five"),
            "category": request.form.get("category"),
            "category2": request.form.get("category-two"),
            "category3": request.form.get("category-three"),
            "category4": request.form.get("category-four"),
            "category5": request.form.get("category-five"),
            "modifier": request.form.get("modifier"),
            "modifier2": request.form.get("modifier-two"),
            "modifier3": request.form.get("modifier-three"),
            "modifier4": request.form.get("modifier-four"),
            "modifier5": request.form.get("modifier-five"),
            "total": request.form.get(str("total")),
            "total2": request.form.get(str("total-two")),
            "total3": request.form.get(str("total-three")),
            "total4": request.form.get(str("total-four")),
            "total5": request.form.get
            (str("total-five")),
            "is_visible": is_visible,
            "additional_information": request.form.get
            ("additional-information"),
        }
        mongo.db.workouts.update_one
        ({"_id": ObjectId(workout_id)}, {"$set": submit})
        flash("workout successfully amended")
        return redirect(url_for("profile", username=session["user"]))

    return render_template(
        "edit_workout.html", workout=workout, workouts=workouts)

# function for a user to delete an owned workout record from the database


@app.route("/delete_workout/<workout_id>")
def delete_workout(workout_id):
    mongo.db.workouts.delete_one
    ({"_id": ObjectId(workout_id)})
    workouts = list(mongo.db.workouts.find())
    flash("workout successfully deleted")
    return render_template(
        "profile.html", username=session["user"], workouts=workouts)

# shows the full details of a single workout record in its own page


@app.route("/workout_details/<workout_id>")
def workout_details(workout_id):
    workout = mongo.db.workouts.find_one({"_id": ObjectId(workout_id)})

    return render_template(
        "workout_details.html", workout=workout, workouts=workouts)

# allows the user to search all workout records


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    workouts = list(mongo.db.workouts.find({"$text": {"$search": query}}))
    return render_template("workouts.html", workouts=workouts)

# function for the user to save another's public workout to their own profile


@app.route("/save_workout_page/<workout_id>", methods=["GET", "POST"])
def save_workout_page(workout_id):
    workout = mongo.db.workouts.find_one({"_id": ObjectId(workout_id)})
    workouts = list(mongo.db.workouts.find())
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    return render_template(
        "save_workout.html", workout=workout, workouts=workouts)


@app.route("/save_workout/<workout_id>", methods=["GET", "POST"])
def save_workout(workout_id):
    workout = mongo.db.workouts.find_one({"_id": ObjectId(workout_id)})
    workouts = list(mongo.db.workouts.find())
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if request.method == "POST":
        saved_workout = {
            "saved_by": username,
        }
        mongo.db.workouts.update_one
        ({"_id": ObjectId(workout_id)}, {"$push": saved_workout})

    return render_template(
        "profile.html",
        workout=workout, workouts=workouts,
        username=username, saved_workout=saved_workout)

# function for the user to remove a saved workout from their profile


@app.route("/un_save_workout/<workout_id>", methods=["GET", "POST"])
def un_save_workout(workout_id):
    workout = mongo.db.workouts.find_one({"_id": ObjectId(workout_id)})
    workouts = list(mongo.db.workouts.find())
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if request.method == "POST":
        un_saved_workout = {
            "un_saved_by": username,
        }
        mongo.db.workouts.update_one
        ({"_id": ObjectId(workout_id)}, {"$push": un_saved_workout})

    return render_template(
        "profile.html", workout=workout, workouts=workouts, username=username)

# function to display full details of a workout to be added as a plan


@app.route("/plan_workout_page/<workout_id>", methods=["GET", "POST"])
def plan_workout_page(workout_id):
    workout = mongo.db.workouts.find_one({"_id": ObjectId(workout_id)})
    planned_workouts = list(mongo.db.planned_workouts.find())
    workouts = list(mongo.db.workouts.find())
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    return render_template(
        "plan_workout.html", workout=workout,
        workouts=workouts, planned_workouts=planned_workouts)


@app.route("/plan_workout/<workout_id>", methods=["GET", "POST"])
def plan_workout(workout_id):
    workout = mongo.db.workouts.find_one({"_id": ObjectId(workout_id)})
    workouts = list(mongo.db.workouts.find())
    planned_workouts = list(mongo.db.planned_workouts.find())
    planned_workout = mongo.db.planned_workouts.find_one
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if request.method == "POST":
        planned_workouts = list(mongo.db.planned_workouts.find())
        planned_workout = {
            "workout_description": request.form.get
            ("plan-workout-description"),
            "workout_container_description": request.form.get
            ("plan-workout-description"),
            "exercise": request.form.get("plan-exercise"),
            "exercise2": request.form.get("plan-exercise-two"),
            "exercise3": request.form.get("plan-exercise-three"),
            "exercise4": request.form.get("plan-exercise-four"),
            "exercise5": request.form.get("plan-exercise-five"),
            "category": request.form.get("plan-category"),
            "category2": request.form.get("plan-category-two"),
            "category3": request.form.get("plan-category-three"),
            "category4": request.form.get("plan-category-four"),
            "category5": request.form.get("plan-category-five"),
            "modifier": request.form.get("plan-modifier"),
            "modifier2": request.form.get("plan-modifier-two"),
            "modifier3": request.form.get("plan-modifier-three"),
            "modifier4": request.form.get("plan-modifier-four"),
            "modifier5": request.form.get("plan-modifier-five"),
            "total": request.form.get(str("plan-total")),
            "total2": request.form.get(str("plan-total-two")),
            "total3": request.form.get(str("plan-total-three")),
            "total4": request.form.get(str("plan-total-four")),
            "total5": request.form.get(str("plan-total-five")),
            "additional_information": request.form.get
            ("plan-additional-information"),
            "planned_by": session["user"],
            "planned_date": request.form.get("plan-workout-date"),
        }
        mongo.db.planned_workouts.insert_one(planned_workout)
    flash("workout successfully planned")
    return render_template(
        "profile.html", username=session["user"],
        planned_workout=planned_workout,
        planned_workouts=planned_workouts, workout=workout, workouts=workouts)

# function to mark planned workout as complete


@app.route("/delete_planned_workout/<plan_workout_id>")
def delete_planned_workout(plan_workout_id):
    mongo.db.planned_workouts.delete_one({"_id": ObjectId(plan_workout_id)})
    workouts = list(mongo.db.workouts.find())
    planned_workouts = list(mongo.db.planned_workouts.find())
    flash("workout successfully completed!")
    return render_template(
        "profile.html", username=session["user"],
        workouts=workouts, planned_workouts=planned_workouts)

# how to run the app


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
