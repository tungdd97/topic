from src.common.utils import get_current_time, generate_md5_by_str
from src.models.user_model import UserModel
from src.models.student_model import StudentModel
from src.models.teacher_model import TeacherModel

default_pass = "123456"
import random


def create_data(n=10):
    all_data = list()
    for i in range(1, n):
        email = f"sinhvien{i}.utehy@gmail.com"
        password = generate_md5_by_str(default_pass)
        student_data = {
            "Ten": "Nguyen Van A " + str(i),
            "MaSV": "Ma101152" + str(i),
            "SDT": "03133312323" + str(i),
            "Email": email,
            "IDLop": 1,
            "MaGVHD": "",
            "IDDeTai": "",
            "Cap": random.randrange(1,3,1),
            "TrangThai": "TaoMoi",
            "ThoiGianTao": get_current_time(),
            "ThoiGianCapNhat": get_current_time()
        }
        student_id = StudentModel.insert_one_student(student_data)
        user_data = {
            "TaiKhoan": email,
            "MatKhau": str(password),
            "Quyen": "sinhvien",
            "LienKet": student_id,
            "ThoiGianTao": get_current_time(),
            "ThoiGianCapNhat": get_current_time()
        }
        user_id = UserModel.insert_user(data_insert=user_data)
    for i in range(1, n):
        email = f"giaovien{i}.utehy@gmail.com"
        password = generate_md5_by_str(default_pass)
        teacher_data = {
            "Ten": "Le Van A" + str(i),
            "SoLuong": 0,
            "MaGV": f"Gv12983192{i}",
            "SDT": f"19831321312{i}",
            "Email": email,
            "ChucVu": "GiaoVien",
            "TrangThai": "",
            "ThoiGianTao": get_current_time(),
            "ThoiGianCapNhat": get_current_time()
        }
        teacher_id = TeacherModel.insert_one_teacher(teacher_data)
        user_data = {
            "TaiKhoan": email,
            "MatKhau": str(password),
            "Quyen": "giaovien",
            "LienKet": teacher_id,
            "ThoiGianTao": get_current_time(),
            "ThoiGianCapNhat": get_current_time()
        }
        user_id = UserModel.insert_user(data_insert=user_data)

    email = f"truongkhoa.utehy@gmail.com"
    password = generate_md5_by_str(default_pass)
    teacher_data = {
        "Ten": "Truong khoa",
        "SoLuong": 0,
        "MaGV": "Tk1231231",
        "SDT": "192831892313",
        "Email": email,
        "ChucVu": "TruongKhoa",
        "TrangThai": "",
        "ThoiGianTao": get_current_time(),
        "ThoiGianCapNhat": get_current_time()
    }
    teacher_id = TeacherModel.insert_one_teacher(teacher_data)
    user_data = {
        "TaiKhoan": email,
        "MatKhau": str(password),
        "Quyen": "truongkhoa",
        "LienKet": teacher_id,
        "ThoiGianTao": get_current_time(),
        "ThoiGianCapNhat": get_current_time()
    }
    user_id = UserModel.insert_user(data_insert=user_data)


if __name__ == "__main__":
    create_data()
