from flask import Flask , render_template, url_for , redirect ,request
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

#Employee Information data model structure
class EmployeeInformation(db.Model):
    eid = db.Column(db.Integer, primary_key=True)
    ename = db.Column(db.String(200), nullable=False)
    desgination = db.Column(db.String(200), nullable=False)
    email= db.Column(db.String(100),nullable=False)
    number = db.Column(db.String(100),nullable=False)
    
    def __init__(self, eid=None, ename=None, desgination=None, email=None, number=None):
        self.eid = eid
        self.ename = ename
        self.desgination = desgination
        self.email = email
        self.number = number
   
@app.route('/view')
def routed_page():
    data = EmployeeInformation.query.all()
    return render_template('view.html',data=data)

@app.route('/',methods=['POST',"GET"])
def save_data():
    if request.method =="POST":
        #This piece of script will extract the value from requested form
        
        eid_request = request.form['eid']
        ename_request = request.form['ename']
        desgination_request = request.form['des']
        email_request = request.form['eemail']
        number_request = request.form['enumber']
        
        #This piece of script will store the data into repective model field 
        eid_store = EmployeeInformation(eid=eid_request, ename=ename_request, desgination=desgination_request, email=email_request, number=number_request)

        try:
            db.session.add(eid_store)
            db.session.commit()
            return redirect('/view')
        except:
            return "<h1>Somthing is going the wrong</h1>"
    else:
        
        return render_template('create.html')

@app.route("/delete/<int:id>")
def DeleteRecord(id):
    delete_record = EmployeeInformation.query.get_or_404(id)
    try:
        db.session.delete(delete_record)
        db.session.commit()
        return redirect('/view')
    except:
        return "<h1>Thre is Something problem in deleting the record</h1>"

@app.route("/update/<int:id>", methods=['GET','POST'])
def UpdateRecord(id):
    update_record = EmployeeInformation.query.get_or_404(id)
    if request.method=='POST':
        update_record.ename = request.form['ename']
        update_record.desgination = request.form['des']
        update_record.email = request.form['eemail']
        update_record.number = request.form['enumber']
        try:
            db.session.commit()
            return redirect('/view')
        except:
            return "<h1>Somthing is going the wrong updating the Record</h1>"
    else:
        return render_template('edit.html', update_record=update_record)
    

if __name__=="__main__":
    app.run(debug=True)
    manager.run()