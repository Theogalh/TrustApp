from app import app, db
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required
from app.forms.list import ListCreateForm
from app.forms.character import CharacterCreateForm
from app.models.list import List
from app.models.character import Character


@app.route('/list', methods=["GET", "POST", "DELETE"], defaults={"listname": None})
@app.route('/list/<listname>', methods=["GET", "POST", "DELETE"])
@login_required
def list(listname=None):
    formChar = CharacterCreateForm()
    formList = ListCreateForm()
    if request.method == "POST":
        if listname:
            list = List.query.filter_by(name=listname).first()
            if list:
                char = Character.query.filter_by(name=formChar.name.data.lower(),
                                                 server=formChar.server.data.lower(),
                                                 region=formChar.region.data).first()
                if char in list.characters:
                    char.refresh()
                    flash("Character already in this list.")
                else:
                    if not char:
                        char = Character(name=formChar.name.data.lower(), server=formChar.server.data.lower(),
                                         region=formChar.region.data)
                        db.session.add(char)

                    if char.refresh() == 200:
                        list.characters.append(char)
                        db.session.commit()
                        flash("Character added")
                    else:
                        flash("Character didn't exist")
            else:
                flash("Error, list didn't exist.")
        else:
            list = List.query.filter_by(name=formList.name.data).first()
            if not list:
                list = List(name=formList.name.data, user_id=current_user.id)
                db.session.add(list)
                current_user.lists.append(list)
                db.session.commit()
                flash("List create")
            else:
                flash("List already exist")
    return render_template('list.html', formList=formList, formChar=formChar)
