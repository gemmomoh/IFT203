from flask import *

from app.faculty import faculty_bp

@faculty_bp.route("/faculty_list")

def get_faculty_list():
    return render_template("list_faculty.html")