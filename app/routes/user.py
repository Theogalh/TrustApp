from app import app, db
from app.forms.user import EditProfileForm
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required
from app.models.user import User


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    characters = [
        {'Owner': user, 'body': 'Test post #1'},
        {'Owner': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, characters=characters)


@app.route("/user/edit", methods=["GET", "POST"])
@login_required
def edit():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash("Your changes have been saved.")
        return redirect("/user/edit")
    elif request.method == "GET":
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title="Edit Profile", form=form)
