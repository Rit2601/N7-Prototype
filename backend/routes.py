from flask import Blueprint, render_template

bp = Blueprint("main", __name__)

@bp.get("/")
def home():
    return render_template("index.html")

@bp.get("/case-studies")
def case_studies():
    return render_template("case-studies.html")

@bp.get("/footer-demo")
def footer_demo():
    return render_template("footer-demo.html")
