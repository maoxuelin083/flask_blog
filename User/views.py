from flask import Blueprint, render_template
from .models import UserModels

bp = Blueprint("bp", __name__)


@bp.route("/")
def home():
    return render_template('home.html')




