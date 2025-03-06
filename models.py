from sqlalchemy import Column, create_engine, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URL
Base = declarative_base()
class Employee(Base):
    __tablename__ = 'tb_employee'
    
    empid = Column(Integer, primary_key=True, autoincrement=True)
    userid = Column(String, nullable=False)
    empname = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)

# Kết nối cơ sở dữ liệu
#DATABASE_URL = "postgresql://pedevelop:123456@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)

# Tạo bảng nếu chưa có
Base.metadata.create_all(engine)



# Tạo session để tương tác với cơ sở dữ liệu
Session = sessionmaker(bind=engine)

# Hàm đăng ký nhân viên
def register_employee(name, password, email, userid):
    session = Session()
    new_employee = Employee(empname=name, password=password, email=email, userid=userid)
    session.add(new_employee)
    session.commit()
    session.close()

# Hàm hiển thị danh sách nhân viên
def show_employees():
    session = Session()
    employees = session.query(Employee).all()
    session.close()
    return employees