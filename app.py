# Initialize Flask application
import subprocess
import time
from celery import Celery
from flask import Flask, redirect, render_template, request, url_for

from models import register_employee, show_employees


app = Flask(__name__)
# Mảng lưu thông tin nhân viên
employee_list = []


    

# Define a route for the home page
@app.route("/")
def home():
    # Render the HTML template
    return render_template("index.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Lấy dữ liệu từ form
        name = request.form.get('name')
       
        password = request.form.get('password')
        email = request.form.get('email')
        userid = request.form.get('userid')

        # Gọi hàm đăng ký nhân viên
        register_employee(name, password, email, userid)

        # Kiểm tra dữ liệu và thêm vào danh sách
        # if name and age and position:
        #     employee_list.append({'name': name, 'age': age, 'position': position})
        return redirect(url_for('employees'))

    # Render trang đăng ký
    return render_template('register.html')


# Chạy worker bằng subprocess
def start_worker():
    subprocess.Popen(['rq', 'worker'])

@app.route('/start_worker')
def start_worker_route():
    start_worker()
    return "Worker started!", 200

@app.route('/employees')
def employees():
    # Render danh sách nhân viên
    employee_list = show_employees()

    return render_template('employees.html', employees=employee_list)


if __name__ == '__main__':
    app.run(debug=True)
    
# Run the app
if __name__ == "__main__":
    app.run(debug=True)