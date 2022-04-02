"""Flask app for adopt app."""

from flask import Flask, render_template, redirect, flash

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


@app.get('/')
def display_listing():
    """ Displays listing page for pets """

    pets = Pet.query.all()

    return render_template('listing_page.html', pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Pet add form; handle adding."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name = name, species = species, photo_url = photo_url, age = age, notes = notes)
        db.session.add(new_pet)
        db.session.commit()

        flash(f"Added {name} to the pet list!")

        return redirect("/")

    else:
        return render_template(
            "add_pet_page.html", form=form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet_page(pet_id):
    """ Edit Pet Profile Page; handle editing """

    curr_pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=curr_pet)

    if form.validate_on_submit():
        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data

        curr_pet.photo_url = photo_url
        curr_pet.notes = notes
        curr_pet.available = available

        db.session.commit()

        flash(f"Edited {curr_pet.name}'s profile")

        return redirect(f"/{pet_id}")

    else:
        return render_template(
            "pet_detail_page.html", form=form, curr_pet=curr_pet)