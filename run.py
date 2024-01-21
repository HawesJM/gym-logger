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


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/workouts")
def workouts():
    workouts = list(mongo.db.workouts.find())
    return render_template("workouts.html", workouts=workouts)


@app.route("/categories")
def categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/register",  methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

    # acts as the else statement if no existing user is found
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

    # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


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
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for
                    ("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("sign_in"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("sign_in"))

    return render_template("sign_in.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab session user's username from db
    workouts = list(mongo.db.workouts.find())
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        return render_template("profile.html", username=username, workouts=workouts)

    return redirect(url_for("sign_in"))


@app.route("/sign_out")
def sign_out():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("sign_in"))

@app.route("/record_workout", methods=["GET", "POST"])
def record_workout():
    if request.method == "POST":
        is_visible = "on" if request.form.get("is-visible") else "off"
        logged_workout = {
            "date": request.form.get("workout-date"),
            "workout_description": request.form.get("workout-description"),
            "workout_container_description": request.form.get("workout-description").replace(" ", ""),
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
            "additional_information": request.form.get("additional-information"),
        }

        #
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


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category": request.form.get("category")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")

    return render_template("add_workout.html")

@app.route("/add_exercise", methods=["GET", "POST"])
def add_exercise():
    if request.method == "POST":
        exercise = {
            "exercise": request.form.get("exercise")
        }
        mongo.db.categories.insert_one(exercise)
        flash("New Exercise Added")

    return render_template("add_workout.html")


@app.route("/edit_workout/<workout_id>", methods=["GET", "POST"])
def edit_workout(workout_id):
    workout = mongo.db.workouts.find_one({"_id": ObjectId(workout_id)})
    workouts = list(mongo.db.workouts.find())
    if request.method == "POST":
        submit = {
            "workout_description": request.form.get("workout-description")
        }
        mongo.db.workouts.update_one({"_id": ObjectId(workout_id)}, {"$set": submit})

    return render_template("edit_workout.html", workout=workout, workouts=workouts)
    


@app.route("/delete_workout/<workout_id>")
def delete_workout(workout_id):
    mongo.db.workouts.delete_one({"_id": 
    ObjectId(workout_id)})
    flash("workout successfully deleted")
    workouts = list(mongo.db.workouts.find())
    return render_template("profile.html", username=session["user"], workout=workouts)



@app.route("/workout_details/<workout_id>")
def workout_details(workout_id):
    workout = mongo.db.workouts.find_one({"_id": ObjectId(workout_id)})

    return render_template("workout_details.html", workout=workout)

@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    workouts = list(mongo.db.workouts.find({"$text": {"$search": query}}))
    return render_template("workouts.html", workouts=workouts)

    

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)