from flask import Blueprint, json
from flask import render_template, redirect, url_for, request, session, jsonify

from app.employee import bp
from app.employee.model import  Employee , EmployeeSchema 
import json
from datetime import datetime , timedelta
import dateutil.parser as dt

from app import db, ma

from randomuser import RandomUser
import random

@bp.route('/gen/<num>', methods=['GET'])
def gen_emps(num):
        user_list = RandomUser.generate_users(200,{'nat': 'IN'})
        for row in user_list:
            try:
                emp = Employee()
                rand_ids = random.randint(100000000, 10000000000)
                emp.name = row.get_full_name()
                emp.date_of_joining = dt.parse(row.get_dob())
                emp.pf_no = 'PF-'+str(rand_ids)
                emp.pan = 'PAN'+str(rand_ids)
                emp.emp_id = 'SIL-'+str(random.randint(1, 4000))
                emp.ctc = random.randint(245000, 5000000)
                emp.uan = 'UAN-'+str(rand_ids)
                emp.gender = row.get_gender()
                emp.bank_name = 'HDFC Bank'
                emp.acc_no = 'ACC-'+str(rand_ids)
                emp.ifsc_no = 'HDFC000013'
                emp.department =random.choice(['IT','HR','Accounts','Marketing','Sales'])
                emp.designation = random.choice(['SDE1','SDE2','SDE3','Manager','Lead','Senior Manager','Junioir Manager','Analyst'])
                emp.aadhar = 'AADHAR-'+str(rand_ids)
                db.session.add(emp)
                db.session.commit()
            except Exception as e:
                pass
          
        return jsonify({'success':True, 'message': 'Employes Added'})


@bp.route('/get', methods=['GET'])
def get_emps():
    if request.method == 'GET':
        data_schema = EmployeeSchema(many=True)
        data = Employee.query.all()
        json_data = data_schema.dump(data)
        return jsonify({'success':True, 'message': 'Employes Fetched','data':json_data})
