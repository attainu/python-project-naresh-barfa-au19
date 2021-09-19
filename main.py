from enum import unique
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///parkCars.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

maxCars = 5


class AllCars(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    slot = db.Column(db.Integer)
    car_no = db.Column(db.String(50), unique=True, nullable=False)
    color = db.Column(db.String(50), nullable=False)
    time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.slot} - {self.car_no} - {self.color}"


def validation(car_no):
    car_no_database = AllCars.query.filter_by(car_no=car_no).first()
    if(car_no_database or len(car_no) == 0):
        return "Enter valid car number "
    else:
        return ""


def genrateSlot():
    # maxCars = 5
    slotArr = []
    for cars in AllCars.query.all():
        slotArr.append(cars.slot)
    for i in range(1, maxCars+1):
        if(i not in slotArr):
            return i


@app.route("/", methods=["POST", "GET"])
def create_parking():
    msg = ""
    # maxCars = 5
    # allCars = AllCars(car_no="KA-12-O789", color="while", slot=2)
    # db.session.add(allCars,x)
    # db.session.commit()
    allCars = AllCars.query.all()
    if(len(allCars) <= maxCars and genrateSlot()):
        db.create_all()
        if(request.method == "POST"):
            car_no = request.form['car_no']
            color = request.form['color']
            if(validation(car_no.strip())):
                msg = validation(car_no.strip())
            else:
                genSlot = genrateSlot()
                allCars = AllCars(car_no=car_no.strip(),
                                  color=color.strip().upper(), slot=genSlot)
                db.session.add(allCars)
                db.session.commit()
                msg = "Car parked, successfully !!  "
    else:
        msg = "No Parking slot available :( "

    allCars = AllCars.query.all()

    return render_template("index.html", AllCars=allCars, msg=msg)


@app.route('/delete/<int:slot>')
def delete(slot):
    allCars = AllCars.query.filter_by(slot=slot).first()
    db.session.delete(allCars)
    db.session.commit()
    return redirect("/")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/setting", methods=["POST", "GET"])
def setting():
    msg = ""
    global maxCars
    if(request.method == "POST"):
        max_cars = request.form['max_cars']
        maxCars = int(max_cars)
        print(max_cars)
        msg = "maximum car parking slot update to " + str(max_cars)
    return render_template("setting.html", msg=msg)


@app.route("/search", methods=["POST", "GET"])
def search_color():
    msg = ""
    search_color = ""
    global maxCars
    if(request.method == "POST"):
        search_color = request.form['search_color']
        search_color = search_color.strip().upper()
    colorCars = AllCars.query.filter_by(color=search_color).all()
    if(colorCars):
        msg = "All " + str(search_color) + " color car available here !! "
    else:
        msg = "NO car found !! "
    return render_template("search.html", colorCars=colorCars, msg=msg)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
