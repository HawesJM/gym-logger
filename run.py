import os
from gymlogger import app
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)

## testing

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)

def get_user(user_id):
    user = mongo.db.users.find_one(
            {"username": request.form.get("username")})
    return user
    print(user)
    """
    gets user from users DB using user_id passed in
    """
    user = mongo.db.users.find_one({"user_id": user_id})
    return user

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        """
        Checks if username and email are already in users collection
        and that passwords match, displays relevant flashed messages
        and reloads page until user info is all valid
        """
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email")})

        if existing_user and existing_email:
            flash("Username and email already exist")
            return redirect(url_for("register"))
        elif existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        elif existing_email:
            flash("Email already exists")
            return redirect(url_for("register"))
        elif request.form.get("password") != request.form.get(
                "password_check"):
            flash("Passwords do not match")
            return redirect(url_for("register"))
        else:
            """
            Adds unique id to new user and stores this id to
            used_id database for future reference in while loop
            """
            user_id = 1
            existing_id = True
            while existing_id:
                if user_id not in mongo.db.used_ids.find_one({
                        "name": "used_ids"})["ids"]:
                    existing_id = False
                    break
                else:
                    user_id += 1

            mongo.db.used_ids.update_one({"name": "used_ids"}, {
                "$push": {"ids": user_id}})

            """
            builds new user dict with default superuser and admin permissions
            """
            new_user = {
                "user_id": user_id,
                "f_name": request.form.get("f_name").capitalize(),
                "l_name": request.form.get("l_name").capitalize(),
                "email": request.form.get("email"),
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(
                    request.form.get("password")),
                "user_since": datetime.now(),
                "photo_url": request.form.get("photo_url"),
                "is_super": False,
                "is_admin": False}
            mongo.db.users.insert_one(new_user)

            """puts new user id into session cookie"""
            session["user"] = user_id
            flash("Successfully Registered!")
            return redirect(url_for("profile"))

    """
    If user already signed in, redirects with
    flashed message to their profile page
    """
    if "user" in session:
        flash("You are already registered")
        return redirect(url_for("profile"))

    return render_template("register.html")

