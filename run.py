# required imports

import os
import pandas as pd
from flask import (Flask, flash, render_template,
                   redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

from datetime import datetime
import calendar 
import inspect

# configuration

app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)

workouts = list(mongo.db.workouts.find())
full_total_workouts = len(workouts)
print(full_total_workouts)

# current date

today = datetime.today()
d2 = today.strftime("%B, %Y")
print("d2 =", d2)

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
                return redirect(
                    url_for("profile", username=session["user"]))
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
    # print("workouts = ",workouts)
    planned_workouts = list(mongo.db.planned_workouts.find())
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    # workout totals

    total_workouts = len(workouts)
    user_workouts = list(mongo.db.workouts.find({"created_by": session["user"]}))
    print("--------------------------------------------")
    user_total_workouts = len(user_workouts)

    
    # print("user_workouts = ",user_workouts)
    for workout in user_workouts:
        print(workout['date'])

        # workout totals - rowing filter

    rowing_filter1 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise": "Rowing Machine"}))
    rowing_filter2 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise2": "Rowing Machine"}))
    rowing_filter3 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise3": "Rowing Machine"}))
    rowing_filter4 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise4": "Rowing Machine"}))
    rowing_filter5 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise5": "Rowing Machine"}))
    rowing_filter6 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise6": "Rowing Machine"}))
    rowing_filter7 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise7": "Rowing Machine"}))
    rowing_filter8 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise8": "Rowing Machine"}))
    rowing_filtered = (len(rowing_filter1))+(len(rowing_filter2))+(len(rowing_filter3))+(len(rowing_filter4)+(len(rowing_filter5)))+(len(rowing_filter6))+(len(rowing_filter7))+(len(rowing_filter8))
    print(rowing_filtered)

        # workout totals - running filter

    running_filter1 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise": "Running Machine"}))
    running_filter2 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise2": "Running Machine"}))
    running_filter3 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise3": "Running Machine"}))
    running_filter4 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise4": "Running Machine"}))
    running_filter5 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise5": "Running Machine"}))
    running_filter6 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise6": "Running Machine"}))
    running_filter7 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise7": "Running Machine"}))
    running_filter8 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise8": "Running Machine"}))
    running_filtered = (len(running_filter1))+(len(running_filter2))+(len(running_filter3))+(len(running_filter4)+(len(running_filter5)))+(len(running_filter6))+(len(running_filter7))+(len(running_filter8))
    print(running_filtered)

    # workout totals - pec fly filter

    pectoral_fly_filter1 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise": "Pectoral Fly"}))
    pectoral_fly_filter2 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise2": "Pectoral Fly"}))
    pectoral_fly_filter3 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise3": "Pectoral Fly"}))
    pectoral_fly_filter4 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise4": "Pectoral Fly"}))
    pectoral_fly_filter5 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise5": "Pectoral Fly"}))
    pectoral_fly_filter6 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise6": "Pectoral Fly"}))
    pectoral_fly_filter7 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise7": "Pectoral Fly"}))
    pectoral_fly_filter8 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise8": "Pectoral Fly"}))
    pectoral_fly_filtered = (len(pectoral_fly_filter1))+(len(pectoral_fly_filter2))+(len(pectoral_fly_filter3))+(len(pectoral_fly_filter4)+(len(pectoral_fly_filter5)))+(len(pectoral_fly_filter6))+(len(pectoral_fly_filter7))+(len(pectoral_fly_filter8))
    print(pectoral_fly_filtered)

    # workout totals - ab crunch filter

    abdominal_crunch_filter1 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise": "Abdominal Crunch"}))
    abdominal_crunch_filter2 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise2": "Abdominal Crunch"}))
    abdominal_crunch_filter3 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise3": "Abdominal Crunch"}))
    abdominal_crunch_filter4 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise4": "Abdominal Crunch"}))
    abdominal_crunch_filter5 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise5": "Abdominal Crunch"}))
    abdominal_crunch_filter6 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise6": "Abdominal Crunch"}))
    abdominal_crunch_filter7 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise7": "Abdominal Crunch"}))
    abdominal_crunch_filter8 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise8": "Abdominal Crunch"}))
    abdominal_crunch_filtered = (len(abdominal_crunch_filter1))+(len(abdominal_crunch_filter2))+(len(abdominal_crunch_filter3))+(len(abdominal_crunch_filter4)+(len(abdominal_crunch_filter5)))+(len(abdominal_crunch_filter6))+(len(abdominal_crunch_filter7))+(len(abdominal_crunch_filter8))
    print(abdominal_crunch_filtered)

     # workout totals - seated tricep press filter

    seated_tricep_press_filter1 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise": "Seated Dips/Tricep Press"}))
    seated_tricep_press_filter2 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise2": "Seated Dips/Tricep Press"}))
    seated_tricep_press_filter3 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise3": "Seated Dips/Tricep Press"}))
    seated_tricep_press_filter4 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise4": "Seated Dips/Tricep Press"}))
    seated_tricep_press_filter5 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise5": "Seated Dips/Tricep Press"}))
    seated_tricep_press_filter6 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise6": "Seated Dips/Tricep Press"}))
    seated_tricep_press_filter7 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise7": "Seated Dips/Tricep Press"}))
    seated_tricep_press_filter8 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise8": "Seated Dips/Tricep Press"}))
    seated_tricep_press_filtered = (len(seated_tricep_press_filter1))+(len(seated_tricep_press_filter2))+(len(seated_tricep_press_filter3))+(len(seated_tricep_press_filter4)+(len(seated_tricep_press_filter5)))+(len(seated_tricep_press_filter6))+(len(seated_tricep_press_filter7))+(len(seated_tricep_press_filter8))
    print(seated_tricep_press_filtered)

     # workout totals - lat pulldown filter

    lat_pulldown_filter1 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise": "Lat Pulldown"}))
    lat_pulldown_filter2 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise2": "Lat Pulldown"}))
    lat_pulldown_filter3 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise3": "Lat Pulldown"}))
    lat_pulldown_filter4 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise4": "Lat Pulldown"}))
    lat_pulldown_filter5 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise5": "Lat Pulldown"}))
    lat_pulldown_filter6 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise6": "Lat Pulldown"}))
    lat_pulldown_filter7 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise7": "Lat Pulldown"}))
    lat_pulldown_filter8 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise8": "Lat Pulldown"}))
    lat_pulldown_filtered = (len(lat_pulldown_filter1))+(len(lat_pulldown_filter2))+(len(lat_pulldown_filter3))+(len(lat_pulldown_filter4)+(len(lat_pulldown_filter5)))+(len(lat_pulldown_filter6))+(len(lat_pulldown_filter7))+(len(lat_pulldown_filter8))
    print(lat_pulldown_filtered)

    # workout totals - chin assist filter

    chin_assist_filter1 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise": "Chin Assist"}))
    chin_assist_filter2 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise2": "Chin Assist"}))
    chin_assist_filter3 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise3": "Chin Assist"}))
    chin_assist_filter4 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise4": "Chin Assist"}))
    chin_assist_filter5 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise5": "Chin Assist"}))
    chin_assist_filter6 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise6": "Chin Assist"}))
    chin_assist_filter7 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise7": "Chin Assist"}))
    chin_assist_filter8 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise8": "Chin Assist"}))
    chin_assist_filtered = (len(chin_assist_filter1))+(len(chin_assist_filter2))+(len(chin_assist_filter3))+(len(chin_assist_filter4)+(len(chin_assist_filter5)))+(len(chin_assist_filter6))+(len(chin_assist_filter7))+(len(chin_assist_filter8))
    print(chin_assist_filtered)

    # workout totals - dual dumbbell curls filter

    dual_dumbbells_filter1 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise": "Dual Dumbbell Curls"}))
    dual_dumbbells_filter2 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise2": "Dual Dumbbell Curls"}))
    dual_dumbbells_filter3 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise3": "Dual Dumbbell Curls"}))
    dual_dumbbells_filter4 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise4": "Dual Dumbbell Curls"}))
    dual_dumbbells_filter5 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise5": "Dual Dumbbell Curls"}))
    dual_dumbbells_filter6 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise6": "Dual Dumbbell Curls"}))
    dual_dumbbells_filter7 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise7": "Dual Dumbbell Curls"}))
    dual_dumbbells_filter8 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise8": "Dual Dumbbell Curls"}))
    dual_dumbbells_filtered = (len(dual_dumbbells_filter1))+(len(dual_dumbbells_filter2))+(len(dual_dumbbells_filter3))+(len(dual_dumbbells_filter4)+(len(dual_dumbbells_filter5)))+(len(dual_dumbbells_filter6))+(len(dual_dumbbells_filter7))+(len(dual_dumbbells_filter8))
    print(dual_dumbbells_filtered)

    # workout totals - single dumbbell curls filter

    single_dumbbells_filter1 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise": "Single Dumbbell Curls"}))
    single_dumbbells_filter2 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise2": "Single Dumbbell Curls"}))
    single_dumbbells_filter3 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise3": "Single Dumbbell Curls"}))
    single_dumbbells_filter4 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise4": "Single Dumbbell Curls"}))
    single_dumbbells_filter5 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise5": "Single Dumbbell Curls"}))
    single_dumbbells_filter6 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise6": "Single Dumbbell Curls"}))
    single_dumbbells_filter7 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise7": "Single Dumbbell Curls"}))
    single_dumbbells_filter8 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise8": "Single Dumbbell Curls"}))
    single_dumbbells_filtered = (len(single_dumbbells_filter1))+(len(single_dumbbells_filter2))+(len(single_dumbbells_filter3))+(len(single_dumbbells_filter4)+(len(single_dumbbells_filter5)))+(len(single_dumbbells_filter6))+(len(single_dumbbells_filter7))+(len(single_dumbbells_filter8))
    print(single_dumbbells_filtered)

    # workout totals - converging chest press filter

    converging_chest_filter1 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise": "Converging Chest Press"}))
    converging_chest_filter2 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise2": "Converging Chest Press"}))
    converging_chest_filter3 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise3": "Converging Chest Press"}))
    converging_chest_filter4 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise4": "Converging Chest Press"}))
    converging_chest_filter5 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise5": "Converging Chest Press"}))
    converging_chest_filter6 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise6": "Converging Chest Press"}))
    converging_chest_filter7 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise7": "Converging Chest Press"}))
    converging_chest_filter8 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise8": "Converging Chest Press"}))
    converging_chest_filtered = (len(converging_chest_filter1))+(len(converging_chest_filter2))+(len(converging_chest_filter3))+(len(converging_chest_filter4)+(len(converging_chest_filter5)))+(len(converging_chest_filter6))+(len(converging_chest_filter7))+(len(converging_chest_filter8))
    print(converging_chest_filtered)

    # workout totals - seated dips filter

    seated_dips_filter1 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise": "Seated Dips/Tricep Press"}))
    seated_dips_filter2 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise2": "Seated Dips/Tricep Press"}))
    seated_dips_filter3 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise3": "Seated Dips/Tricep Press"}))
    seated_dips_filter4 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise4": "Seated Dips/Tricep Press"}))
    seated_dips_filter5 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise5": "Seated Dips/Tricep Press"}))
    seated_dips_filter6 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise6": "Seated Dips/Tricep Press"}))
    seated_dips_filter7 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise7": "Seated Dips/Tricep Press"}))
    seated_dips_filter8 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise8": "Seated Dips/Tricep Press"}))
    seated_dips_filtered = (len(seated_dips_filter1))+(len(seated_dips_filter2))+(len(seated_dips_filter3))+(len(seated_dips_filter4)+(len(seated_dips_filter5)))+(len(seated_dips_filter6))+(len(seated_dips_filter7))+(len(seated_dips_filter8))
    print(seated_dips_filtered)

    # workout totals - lateral dumbbell raise filter

    lateral_dumbbell_filter1 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise": "Lateral Dumbbell Raise"}))
    lateral_dumbbell_filter2 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise2": "Lateral Dumbbell Raise"}))
    lateral_dumbbell_filter3 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise3": "Lateral Dumbbell Raise"}))
    lateral_dumbbell_filter4 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise4": "Lateral Dumbbell Raise"}))
    lateral_dumbbell_filter5 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise5": "Lateral Dumbbell Raise"}))
    lateral_dumbbell_filter6 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise6": "Lateral Dumbbell Raise"}))
    lateral_dumbbell_filter7 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise7": "Lateral Dumbbell Raise"}))
    lateral_dumbbell_filter8 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise8": "Lateral Dumbbell Raise"}))
    lateral_dumbbell_filtered = (len(lateral_dumbbell_filter1))+(len(lateral_dumbbell_filter2))+(len(lateral_dumbbell_filter3))+(len(lateral_dumbbell_filter4)+(len(lateral_dumbbell_filter5)))+(len(lateral_dumbbell_filter6))+(len(lateral_dumbbell_filter7))+(len(lateral_dumbbell_filter8))
    print(lateral_dumbbell_filtered)

     # workout totals - diverging seated row filter

    diverging_row_filter1 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise": "Diverging Seated Row"}))
    diverging_row_filter2 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise2": "Diverging Seated Row"}))
    diverging_row_filter3 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise3": "Diverging Seated Row"}))
    diverging_row_filter4 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise4": "Diverging Seated Row"}))
    diverging_row_filter5 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise5": "Diverging Seated Row"}))
    diverging_row_filter6 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise6": "Diverging Seated Row"}))
    diverging_row_filter7 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise7": "Diverging Seated Row"}))
    diverging_row_filter8 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise8": "Diverging Seated Row"}))
    diverging_row_filtered = (len(diverging_row_filter1))+(len(diverging_row_filter2))+(len(diverging_row_filter3))+(len(diverging_row_filter4)+(len(diverging_row_filter5)))+(len(diverging_row_filter6))+(len(diverging_row_filter7))+(len(diverging_row_filter8))
    print(diverging_row_filtered)

    # workout totals - low row filter

    low_row_filter1 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise": "Low Row"}))
    low_row_filter2 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise2": "Low Row"}))
    low_row_filter3 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise3": "Low Row"}))
    low_row_filter4 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise4": "Low Row"}))
    low_row_filter5 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise5": "Low Row"}))
    low_row_filter6 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise6": "Low Row"}))
    low_row_filter7 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise7": "Low Row"}))
    low_row_filter8 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise8": "Low Row"}))
    low_row_filtered = (len(low_row_filter1))+(len(low_row_filter2))+(len(low_row_filter3))+(len(low_row_filter4)+(len(low_row_filter5)))+(len(low_row_filter6))+(len(low_row_filter7))+(len(low_row_filter8))
    print(low_row_filtered)

    # workout totals - dips filter

    dips_filter1 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise": "Dips"}))
    dips_filter2 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise2": "Dips"}))
    dips_filter3 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise3": "Dips"}))
    dips_filter4 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise4": "Dips"}))
    dips_filter5 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise5": "Dips"}))
    dips_filter6 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise6": "Dips"}))
    dips_filter7 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise7": "Dips"}))
    dips_filter8 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise8": "Dips"}))
    dips_filtered = (len(dips_filter1))+(len(dips_filter2))+(len(dips_filter3))+(len(dips_filter4)+(len(dips_filter5)))+(len(dips_filter6))+(len(dips_filter7))+(len(dips_filter8))
    print(dips_filtered)

     # workout totals - suspended leg raises filter

    leg_raises_filter1 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise": "Suspended Leg Raises"}))
    leg_raises_filter2 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise2": "Suspended Leg Raises"}))
    leg_raises_filter3 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise3": "Suspended Leg Raises"}))
    leg_raises_filter4 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise4": "Suspended Leg Raises"}))
    leg_raises_filter5 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise5": "Suspended Leg Raises"}))
    leg_raises_filter6 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise6": "Suspended Leg Raises"}))
    leg_raises_filter7 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise7": "Suspended Leg Raises"}))
    leg_raises_filter8 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise8": "Suspended Leg Raises"}))
    leg_raises_filtered = (len(leg_raises_filter1))+(len(leg_raises_filter2))+(len(leg_raises_filter3))+(len(leg_raises_filter4)+(len(leg_raises_filter5)))+(len(leg_raises_filter6))+(len(leg_raises_filter7))+(len(leg_raises_filter8))
    print(leg_raises_filtered)

    # workout totals - chin ups filter

    chin_ups_filter1 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise": "Chin Ups"}))
    chin_ups_filter2 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise2": "Chin Ups"}))
    chin_ups_filter3 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise3": "Chin Ups"}))
    chin_ups_filter4 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise4": "Chin Ups"}))
    chin_ups_filter5 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise5": "Chin Ups"}))
    chin_ups_filter6 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise6": "Chin Ups"}))
    chin_ups_filter7 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise7": "Chin Ups"}))
    chin_ups_filter8 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise8": "Chin Ups"}))
    chin_ups_filtered = (len(chin_ups_filter1))+(len(chin_ups_filter2))+(len(chin_ups_filter3))+(len(chin_ups_filter4)+(len(chin_ups_filter5)))+(len(chin_ups_filter6))+(len(chin_ups_filter7))+(len(chin_ups_filter8))
    print(chin_ups_filtered)

    # workout totals - prone leg raises filter

    prone_raises_filter1 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise": "Prone Leg Raises"}))
    prone_raises_filter2 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise2": "Prone Leg Raises"}))
    prone_raises_filter3 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise3": "Prone Leg Raises"}))
    prone_raises_filter4 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise4": "Prone Leg Raises"}))
    prone_raises_filter5 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise5": "Prone Leg Raises"}))
    prone_raises_filter6 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise6": "Prone Leg Raises"}))
    prone_raises_filter7 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise7": "Prone Leg Raises"}))
    prone_raises_filter8 = list(mongo.db.workouts.find({"created_by": session["user"]} | {"exercise8": "Prone Leg Raises"}))
    prone_raises_filtered = (len(prone_raises_filter1))+(len(prone_raises_filter2))+(len(prone_raises_filter3))+(len(prone_raises_filter4)+(len(prone_raises_filter5)))+(len(prone_raises_filter6))+(len(prone_raises_filter7))+(len(prone_raises_filter8))
    print(prone_raises_filtered)

    # Get month:
    current_date = datetime.now()
    current_month = current_date.month
    current_year = current_date.year
    print(current_month)

    # calculate overview stats

    stats_mapping = {
        "rowing machine": rowing_filtered,
        "running machine": running_filtered,
        "pectoral fly": pectoral_fly_filtered,
        "abdominal crunch": abdominal_crunch_filtered,
        "seated dip/tricep press": seated_tricep_press_filtered,
        "lat pulldown": lat_pulldown_filtered,
        "chin assist": chin_assist_filtered,
        "dual dumbbell curls": dual_dumbbells_filtered,
        "single dumbbell curls": single_dumbbells_filtered,
        "converging chest press": converging_chest_filtered,
        "seated dips": seated_dips_filtered,
        "lateral dumbbell raise": lateral_dumbbell_filtered,
        "diverging row": diverging_row_filtered,
        "low row": low_row_filtered,
        "dips": dips_filtered,
        "suspended leg raises": leg_raises_filtered,
        "chin ups": chin_ups_filtered,
        "prone leg raises": prone_raises_filtered,
        
    }

    total_workouts_stats = [rowing_filtered, running_filtered, pectoral_fly_filtered, abdominal_crunch_filtered, seated_tricep_press_filtered, lat_pulldown_filtered,
        chin_assist_filtered, dual_dumbbells_filtered, single_dumbbells_filtered, converging_chest_filtered,
        seated_dips_filtered, lateral_dumbbell_filtered, diverging_row_filtered, low_row_filtered, dips_filtered, leg_raises_filtered, chin_ups_filtered, prone_raises_filtered]
    total_workouts_stats.sort()
    highest_stat = total_workouts_stats[-1]
    print(highest_stat)

    for name, value in stats_mapping.items():
        if value == highest_stat:
            print(f"favourite exercise: {name}, done {value} times")
            profile_favourite_exercise = (f"favourite exercise: {name}, completed {value} times")



    # check session user
    if session["user"]:
        return render_template(
            "profile.html", username=username,
            workouts=workouts, planned_workouts=planned_workouts, total_workouts=total_workouts, user_total_workouts=user_total_workouts, month=current_month, year=current_year, highest_stat=highest_stat, stats_mapping=stats_mapping, profile_favourite_exercise=profile_favourite_exercise)

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
    
    categories = list(mongo.db.categories.find())
    exercises = list(mongo.db.exercises.find())
    modifiers = list(mongo.db.modifiers.find())

    if request.method == "POST":
        is_visible = "on" if request.form.get("is-visible") else "off"
        logged_workout = {
            "date": request.form.get("workout-date"),
            "workout_description": request.form.get("workout-description"),
            "workout_container_description": request.form.get(
                "workout-description").replace(" ", ""),
            "created_by": session["user"],
            "exercise": request.form.get("exercise"),
            "exercise2": request.form.get("exercise-two"),
            "exercise3": request.form.get("exercise-three"),
            "exercise4": request.form.get("exercise-four"),
            "exercise5": request.form.get("exercise-five"),
            "exercise6": request.form.get("exercise-six"),
            "exercise7": request.form.get("exercise-seven"),
            "exercise8": request.form.get("exercise-eight"),
            "category": request.form.get("category"),
            "category2": request.form.get("category-two"),
            "category3": request.form.get("category-three"),
            "category4": request.form.get("category-four"),
            "category5": request.form.get("category-five"),
            "category6": request.form.get("category-six"),
            "category7": request.form.get("category-seven"),
            "category8": request.form.get("category-eight"),
            "modifier": request.form.get("modifier"),
            "modifier_two": request.form.get("modifier_two"),
            "modifier_three": request.form.get("modifier_three"),
            "exercise_two_modifier": request.form.get("exercise_two_modifier_one"),
            "exercise_two_modifier_two": request.form.get("exercise_two_modifier_two"),
            "exercise_two_modifier_three": request.form.get("exercise_two_modifier_three"),
            "exercise_three_modifier": request.form.get("exercise_three_modifier_one"),
            "exercise_three_modifier_two": request.form.get("exercise_three_modifier_two"),
            "exercise_three_modifier_three": request.form.get("exercise_three_modifier_three"),
            "exercise_four_modifier": request.form.get("exercise_four_modifier_one"),
            "exercise_four_modifier_two": request.form.get("exercise_four_modifier_two"),
            "exercise_four_modifier_three": request.form.get("exercise_four_modifier_three"),
            "exercise_five_modifier": request.form.get("exercise_five_modifier_one"),
            "exercise_five_modifier_two": request.form.get("exercise_five_modifier_two"),
            "exercise_five_modifier_three": request.form.get("exercise_five_modifier_three"),
            "exercise_six_modifier": request.form.get("exercise_six_modifier_one"),
            "exercise_six_modifier_two": request.form.get("exercise_six_modifier_two"),
            "exercise_six_modifier_three": request.form.get("exercise_six_modifier_three"),
            "exercise_seven_modifier": request.form.get("exercise_seven_modifier_one"),
            "exercise_seven_modifier_two": request.form.get("exercise_seven_modifier_two"),
            "exercise_seven_modifier_three": request.form.get("exercise_seven_modifier_three"),
            "exercise_eight_modifier": request.form.get("exercise_eight_modifier_one"),
            "exercise_eight_modifier_two": request.form.get("exercise_eight_modifier_two"),
            "exercise_eight_modifier_three": request.form.get("exercise_eight_modifier_three"),
            "total_one": request.form.get(str("total_one")),
            "total_two": request.form.get(str("total_two")),
            "total_three": request.form.get(str("total_three")),
            "exercise_two_total_one": request.form.get(str("exercise_two_total_one")),
            "exercise_two_total_two": request.form.get(str("exercise_two_total_two")),
            "exercise_two_total_three": request.form.get(str("exercise_two_total_three")),
            "exercise_three_total_one": request.form.get(str("exercise_three_total_one")),
            "exercise_three_total_two": request.form.get(str("exercise_three_total_two")),
            "exercise_three_total_three": request.form.get(str("exercise_three_total_three")),
            "exercise_four_total_one": request.form.get(str("exercise_four_total_one")),
            "exercise_four_total_two": request.form.get(str("exercise_four_total_two")),
            "exercise_four_total_three": request.form.get(str("exercise_four_total_three")),
            "exercise_five_total_one": request.form.get(str("exercise_five_total_one")),
            "exercise_five_total_two": request.form.get(str("exercise_five_total_two")),
            "exercise_five_total_three": request.form.get(str("exercise_five_total_three")),
            "exercise_six_total_one": request.form.get(str("exercise_six_total_one")),
            "exercise_six_total_two": request.form.get(str("exercise_six_total_two")),
            "exercise_six_total_three": request.form.get(str("exercise_six_total_three")),
            "exercise_seven_total_one": request.form.get(str("exercise_seven_total_one")),
            "exercise_seven_total_two": request.form.get(str("exercise_seven_total_two")),
            "exercise_seven_total_three": request.form.get(str("exercise_seven_total_three")),
            "exercise_eight_total_one": request.form.get(str("exercise_eight_total_one")),
            "exercise_eight_total_two": request.form.get(str("exercise_eight_total_two")),
            "exercise_eight_total_three": request.form.get(str("exercise_eight_total_three")),
            "is_visible": is_visible,
            "additional_information": request.form.get(
                "additional-information"),
            "saved_by": [],
            "unsaved_by": [],

        }

        # ensures key fields are not recorded as empty

        logged_exercise = {
            "exercise": request.form.get("exercise"),
            "created_by": session["user"],
        }

        logged_category = {
            "category": request.form.get("category"),
            "created_by": session["user"],
        }

        logged_modifier = {
            "modifier": request.form.get("modifier"),
            "created_by": session["user"],
        }

        logged_modifier_two = {
            "modifier_two": request.form.get("modifier_two"),
            "created_by": session["user"],
        }

        
        logged_modifier_three = {
            "modifier_three": request.form.get("modifier_three"),
            "created_by": session["user"],
        }

        mongo.db.workouts.insert_one(logged_workout)
        flash("Workout successfully logged!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("record_workout.html", categories=categories, exercises=exercises, modifiers=modifiers)


# for adding workout categories to the database
@app.route("/add_category", methods=["GET", "POST"])
def add_category():

    existing_category = mongo.db.categories.find_one(
            {"category": request.form.get("category").lower()})
        
    if request.method == "POST":
        if not existing_category:
            category = {
                "category": request.form.get("category")
            }
            mongo.db.categories.insert_one(category)

    return render_template("add_workout.html")


# for adding specific exercises to the database
@app.route("/add_exercise", methods=["GET", "POST"])
def add_exercise():
    if request.method == "POST":
        exercise = {
            "exercise": request.form.get("exercise")
        }
        mongo.db.categories.insert_one(exercise)

    return render_template("add_workout.html")

# for adding modifiers to the database
@app.route("/add_modifier", methods=["GET", "POST"])
def add_modifier():
    if request.method == "POST":
        exercise = {
            "modifier": request.form.get("modifier")
        }
        mongo.db.categories.insert_one(modifier)

    return render_template("add_workout.html")

# for editing an existing workout in the database
@app.route("/edit_workout/<workout_id>", methods=["GET", "POST"])
def edit_workout(workout_id):
    categories = list(mongo.db.categories.find())
    exercises = list(mongo.db.exercises.find())
    modifiers = list(mongo.db.modifiers.find())
    totals = list(mongo.db.modifiers.find())

    workout = mongo.db.workouts.find_one({"_id": ObjectId(workout_id)})
    workouts = list(mongo.db.workouts.find())
    is_visible = "on" if request.form.get("is-visible") else "off"
    if request.method == "POST":
        submit = {
            "date": request.form.get("workout-date"),
            "workout_description": request.form.get("workout-description"),
            "workout_container_description": request.form.get(
                "workout-description").replace(" ", ""),
            "created_by": session["user"],
            "exercise": request.form.get("exercise"),
            "exercise2": request.form.get("exercise-two"),
            "exercise3": request.form.get("exercise-three"),
            "exercise4": request.form.get("exercise-four"),
            "exercise5": request.form.get("exercise-five"),
            "exercise6": request.form.get("exercise-six"),
            "exercise7": request.form.get("exercise-seven"),
            "exercise8": request.form.get("exercise-eight"),
            "category": request.form.get("category"),
            "category2": request.form.get("category-two"),
            "category3": request.form.get("category-three"),
            "category4": request.form.get("category-four"),
            "category5": request.form.get("category-five"),
            "category6": request.form.get("category-six"),
            "category7": request.form.get("category-seven"),
            "category8": request.form.get("category-eight"),
            "total_one": request.form.get(str("total_one")),
            "total_two": request.form.get(str("total_two")),
            "total_three": request.form.get(str("total_three")),
            "exercise_two_total_one": request.form.get(str("exercise_two_total_one")),
            "exercise_two_total_two": request.form.get(str("exercise_two_total_two")),
            "exercise_two_total_three": request.form.get(str("exercise_two_total_three")),
            "exercise_three_total_one": request.form.get(str("exercise_three_total_one")),
            "exercise_three_total_two": request.form.get(str("exercise_three_total_two")),
            "exercise_three_total_three": request.form.get(str("exercise_three_total_three")),
            "exercise_four_total_one": request.form.get(str("exercise_four_total_one")),
            "exercise_four_total_two": request.form.get(str("exercise_four_total_two")),
            "exercise_four_total_three": request.form.get(str("exercise_four_total_three")),
            "exercise_five_total_one": request.form.get(str("exercise_five_total_one")),
            "exercise_five_total_two": request.form.get(str("exercise_five_total_two")),
            "exercise_five_total_three": request.form.get(str("exercise_five_total_three")),
            "exercise_six_total_one": request.form.get(str("exercise_six_total_one")),
            "exercise_six_total_two": request.form.get(str("exercise_six_total_two")),
            "exercise_six_total_three": request.form.get(str("exercise_six_total_three")),
            "exercise_seven_total_one": request.form.get(str("exercise_seven_total_one")),
            "exercise_seven_total_two": request.form.get(str("exercise_seven_total_two")),
            "exercise_seven_total_three": request.form.get(str("exercise_seven_total_three")),
            "exercise_eight_total_one": request.form.get(str("exercise_eight_total_one")),
            "exercise_eight_total_two": request.form.get(str("exercise_eight_total_two")),
            "exercise_eight_total_three": request.form.get(str("exercise_eight_total_three")),
            "is_visible": is_visible,
            "additional_information": request.form.get(
                "additional-information"),
        }
        mongo.db.workouts.update_one(
            {"_id": ObjectId(workout_id)}, {"$set": submit})
        flash("workout successfully amended")
        return redirect(url_for("profile", username=session["user"]))

    return render_template(
        "edit_workout.html", workout=workout, workouts=workouts, categories=categories, exercises=exercises, modifiers=modifiers, totals=totals)


# function for a user to delete an owned workout record from the database
@app.route("/delete_workout/<workout_id>")
def delete_workout(workout_id):
    mongo.db.workouts.delete_one({"_id": ObjectId(workout_id)})
    workouts = list(mongo.db.workouts.find())
    flash("workout successfully deleted")
        # Get month:
    current_date = datetime.now()
    current_month = current_date.month
    current_year = current_date.year
    print(current_month)
    return render_template(
        "profile.html", username=session["user"], workouts=workouts, month=current_month, year=current_year, highest_stat=highest_stat, stats_mapping=stats_mapping, profile_favourite_exercise=profile_favourite_exercise)


# shows the full details of a single workout record in its own page
@app.route("/workout_details/<workout_id>")
def workout_details(workout_id):
    categories = list(mongo.db.categories.find())
    exercises = list(mongo.db.exercises.find())
    modifiers = list(mongo.db.modifiers.find())
    totals = list(mongo.db.modifiers.find())
    workout = mongo.db.workouts.find_one({"_id": ObjectId(workout_id)})

    return render_template(
        "workout_details.html", workout=workout, workouts=workouts, categories=categories, exercises=exercises, modifiers=modifiers, totals=totals)


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
        mongo.db.workouts.update_one(
            {"_id": ObjectId(workout_id)}, {"$push": saved_workout})

    return render_template(
        "profile.html", workout=workout,
        workouts=workouts, username=username, saved_workout=saved_workout)


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
        mongo.db.workouts.update_one(
            {"_id": ObjectId(workout_id)}, {"$push": un_saved_workout})

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
            "date": request.form.get("plan-workout-date"),
            "workout_description": request.form.get("plan-workout-description"),
            "created_by": session["user"],
            "exercise": request.form.get("plan-exercise"),
            "exercise2": request.form.get("plan-exercise-two"),
            "exercise3": request.form.get("plan-exercise-three"),
            "exercise4": request.form.get("plan-exercise-four"),
            "exercise5": request.form.get("plan-exercise-five"),
            "exercise6": request.form.get("plan-exercise-six"),
            "exercise7": request.form.get("plan-exercise-seven"),
            "exercise8": request.form.get("plan-exercise-eight"),
            "category": request.form.get("plan-category"),
            "category2": request.form.get("plan-category-two"),
            "category3": request.form.get("plan-category-three"),
            "category4": request.form.get("plan-category-four"),
            "category5": request.form.get("plan-category-five"),
            "category6": request.form.get("plan-category-six"),
            "category7": request.form.get("plan-category-seven"),
            "category8": request.form.get("plan-category-eight"),
            "modifier": request.form.get("plan-exercise-one-modifier-one"),
            "modifier_two": request.form.get("plan-exercise-one-modifier-two"),
            "modifier_three": request.form.get("plan-exercise-one-modifier-three"),
            "exercise_two_modifier": request.form.get("plan-exercise-two-modifier-one"),
            "exercise_two_modifier_two": request.form.get("plan-exercise-two-modifier-two"),
            "exercise_two_modifier_three": request.form.get("plan-exercise-two-modifier-three"),
            "exercise_three_modifier": request.form.get("plan-exercise-three-modifier-one"),
            "exercise_three_modifier_two": request.form.get("plan-exercise-three-modifier-two"),
            "exercise_three_modifier_three": request.form.get("plan-exercise-three-modifier-three"),
            "exercise_four_modifier": request.form.get("plan-exercise-four-modifier-one"),
            "exercise_four_modifier_two": request.form.get("plan-exercise-four-modifier-two"),
            "exercise_four_modifier_three": request.form.get("plan-exercise-four-modifier-three"),
            "exercise_five_modifier": request.form.get("plan-exercise-five-modifier-one"),
            "exercise_five_modifier_two": request.form.get("plan-exercise-five-modifier-two"),
            "exercise_five_modifier_three": request.form.get("plan-exercise-five-modifier-three"),
            "exercise_six_modifier": request.form.get("plan-exercise-six-modifier-one"),
            "exercise_six_modifier_two": request.form.get("plan-exercise-six-modifier-two"),
            "exercise_six_modifier_three": request.form.get("plan-exercise-six-modifier-three"),
            "exercise_seven_modifier": request.form.get("plan-exercise-seven-modifier-one"),
            "exercise_seven_modifier_two": request.form.get("plan-exercise-seven-modifier-two"),
            "exercise_seven_modifier_three": request.form.get("plan-exercise-seven-modifier-three"),
            "exercise_eight_modifier": request.form.get("plan-exercise-eight-modifier-one"),
            "exercise_eight_modifier_two": request.form.get("plan-exercise-eight-modifier-two"),
            "exercise_eight_modifier_three": request.form.get("plan-exercise-eight-modifier-three"),
            "total_one": request.form.get(str("plan-total-one")),
            "total_two": request.form.get(str("plan-total-two")),
            "total_three": request.form.get(str("plan-total-three")),
            "exercise_two_total_one": request.form.get("exercise_two_total_one"),
            "exercise_two_total_two": request.form.get(str("exercise_two_total_two")),
            "exercise_two_total_three": request.form.get(str("exercise_two_total_three")),
            "exercise_three_total_one": request.form.get(str("exercise_three_total_one")),
            "exercise_three_total_two": request.form.get(str("exercise_three_total_two")),
            "exercise_three_total_three": request.form.get(str("exercise_three_total_three")),
            "exercise_four_total_one": request.form.get(str("exercise_four_total_one")),
            "exercise_four_total_two": request.form.get(str("exercise_four_total_two")),
            "exercise_four_total_three": request.form.get(str("exercise_four_total_three")),
            "exercise_five_total_one": request.form.get(str("exercise_five_total_one")),
            "exercise_five_total_two": request.form.get(str("exercise_five_total_two")),
            "exercise_five_total_three": request.form.get(str("exercise_five_total_three")),
            "exercise_six_total_one": request.form.get(str("exercise_six_total_one")),
            "exercise_six_total_two": request.form.get(str("exercise_six_total_two")),
            "exercise_six_total_three": request.form.get(str("exercise_six_total_three")),
            "exercise_seven_total_one": request.form.get(str("exercise_seven_total_one")),
            "exercise_seven_total_two": request.form.get(str("exercise_seven_total_two")),
            "exercise_seven_total_three": request.form.get(str("exercise_seven_total_three")),
            "exercise_eight_total_one": request.form.get(str("exercise_eight_total_one")),
            "exercise_eight_total_two": request.form.get(str("exercise_eight_total_two")),
            "exercise_eight_total_three": request.form.get(str("exercise_eight_total_three")),
            "additional_information": request.form.get(
                "plan-additional-information"),
            "planned_by": session["user"],
            "planned_date": request.form.get("plan-workout-date"),
        }
        mongo.db.planned_workouts.insert_one(planned_workout)
    flash("workout successfully planned")
    return render_template(
        "profile.html", username=session["user"],
        planned_workout=planned_workout, planned_workouts=planned_workouts,
        workout=workout, workouts=workouts)

# function to display full details of a workout added as a plan
@app.route("/plan_workout_details/<plan_workout_id>")
def plan_workout_details(plan_workout_id):
    workout = mongo.db.workouts.find_one()
    workouts = list(mongo.db.workouts.find())
    planned_workouts = list(mongo.db.planned_workouts.find())
    planned_workout = mongo.db.planned_workouts.find_one({"_id": ObjectId(plan_workout_id)})
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    return render_template(
        "plan_workout_details.html", planned_workouts=planned_workouts, planned_workout=planned_workout, workouts=workouts, workout=workout)

# function to mark planned workout as complete
@app.route("/delete_planned_workout/<plan_workout_id>")
def delete_planned_workout(plan_workout_id):
    completed_workout = mongo.db.planned_workouts.find_one({"_id": ObjectId(plan_workout_id)})
    mongo.db.completed_planned_workouts.insert_one(completed_workout)
    mongo.db.planned_workouts.delete_one(
        {"_id": ObjectId(plan_workout_id)})
    workouts = list(mongo.db.workouts.find())
    planned_workouts = list(mongo.db.planned_workouts.find())
    flash("workout successfully completed!")
    return render_template(
        "profile.html", username=session["user"],
        workouts=workouts, planned_workouts=planned_workouts)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

# how to run the app
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
