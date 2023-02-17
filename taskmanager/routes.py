from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    categories = list(Category.query.order_by(Category.category_name).all())
     # This has been converted to a list from a cursor
     # (we are navigating the db so its a cursor, list method converts it to a python list)
    return render_template("categories.html", categories=categories) 
    # 1st instance is passing the variable to the template.
    # The 2nd one is setting that variable to the ordered list created above


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")
