from flask import Flask, render_template,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:''@localhost/meet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    konu = db.Column(db.String(100))
    tarih = db.Column(db.String(100))
    bsaat = db.Column(db.String(100))
    esaat = db.Column(db.String(100))
    kisiler = db.Column(db.String(100))

    def __init__(self, konu, tarih, bsaat, esaat,kisiler ):
        self.konu = konu
        self.tarih = tarih
        self.bsaat = bsaat
        self.esaat = esaat
        self.kisiler = kisiler

@app.route('/')
def index():
    all_data = Data.query.all()
    return render_template("index.html", meets = all_data)


@app.route('/insert', methods = ['POST'])
def insert():
 
    if request.method == 'POST':
 
        konu = request.form['konu']
        tarih = request.form['tarih']
        bsaat = request.form['bsaat']
        esaat = request.form['esaat']
        kisiler = request.form['kisiler']
 
        my_data = Data(konu, tarih, bsaat, esaat,kisiler )
        db.session.add(my_data)
        db.session.commit()
 
        flash("Toplantı Başarıyla Eklendi !")
 
        return redirect(url_for('index'))

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))
 
        my_data.konu = request.form['konu']
        my_data.tarih = request.form['tarih']
        my_data.bsaat = request.form['bsaat']
        my_data.esaat = request.form['esaat']
        my_data.kisiler = request.form['kisiler']
 
        db.session.commit()
        flash("Toplantı Başarıyla Güncellendi !")
 
        return redirect(url_for('index'))

@app.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Toplantı Başarıyla Silindi !")
 
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

