from app import db , ma
from marshmallow_sqlalchemy import field_for 
# from app.masters.model import Employee

from datetime import datetime

class Employee(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    
    # EMP BASE DETAILS
    emp_id = db.Column(db.String(20),unique=True)
    name = db.Column(db.String(250))
    designation = db.Column(db.String(250),default="")
    emp_type = db.Column(db.String(250),default="fte")
    date_of_joining = db.Column(db.DateTime,default="")
    pf_no = db.Column(db.String(250),default="")
    pan = db.Column(db.String(250),default="")
    uan = db.Column(db.String(250),default="")
    gender = db.Column(db.String(250),default="")
    bank_name = db.Column(db.String(250),default="")
    acc_no = db.Column(db.String(250),default="")
    ifsc_no = db.Column(db.String(250),default="")
    department = db.Column(db.String(250),default="")
    aadhar = db.Column(db.String(250),default="")
    
    # PAY STRUCTURE
    ctc = db.Column(db.Float, default = 0 ) #to fill
    basic = db.Column(db.Float, default = 0 )
    hra = db.Column(db.Float, default = 0 )
    uniform = db.Column(db.Float, default = 0 )
    other_all = db.Column(db.Float, default = 0 )
    addl_all = db.Column(db.Float, default = 0 )
   


class EmployeeSchema(ma.ModelSchema ):
    class Meta:
        model = Employee
