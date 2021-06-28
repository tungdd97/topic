class URI:
    PING = "/ping"

    LOGIN = "/login"
    REGISTER = "/register"
    CHANGE_PASSWORD = "/change_password"

    STUDENT = "/student"
    STUDENTS = "/students"
    STUDENT_NOT_TEACHER = "/student_not_teacher"
    STUDENT_TEACHER = "/student/<student_id>/teacher"
    STUDENT_PROJECT = "/student/<student_id>/project"

    STUDENT_REPORT = "/student_report/<student_id>"

    PROJECT = "/project"
    PROJECT_TEACHER = "/project_teacher/<teacher_id>"

    TEACHER_PROJECT_DETAIL = "teacher_project_detail/<teacher_id>"
    TEACHER = "/teacher"

    TEACHERS = "/teachers"

    TEACHER_DETAIL = "/teacher/<teacher_id>"

    CONTACT = "/contact"

    MESSAGE = "/message"

    REPORT_WEEKLY = "<teacher_id>/report_weekly/<week>"
    REPORT_WEEKLY_DETAIL = "/report_weekly/<week>"

    ALL_COMMENT = "/comments/<student_id>"

    DOWNLOAD_IMAGE = "/download/image/<week_id>/<image_id>"
    DOWNLOAD_FILE = "/download/file/<week_id>/<file_id>"

    REPORT_POINT = "/report/<week>/point"
    REPORT = "/reports"
    REPORT_BROWSE = "<teacher_id>/browse/<masv>"
