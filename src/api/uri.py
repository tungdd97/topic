class URI:
    PING = "/ping"

    LOGIN = "/login"
    STUDENT = "/student"
    STUDENT_REPORT = "/student_report/<student_id>"

    PROJECT = "/project"

    TEACHER = "/teacher"

    TEACHER_DETAIL = "/teacher/<teacher_id>"

    CONTACT = "/contact_dean"

    REPORT_WEEKLY = "/report_weekly/<week>"

    DOWNLOAD_IMAGE = "/download/image/<week_id>/<image_id>"
    DOWNLOAD_FILE = "/download/file/<week_id>/<file_id>"

    REPORT_POINT = "/report/<week>/point"
