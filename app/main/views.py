from ..models import Quotes
from flask import render_template,request,redirect,url_for, flash
from ..models import User, Blogs, Comment, Subscriber   
from flask_login import login_required,current_user
from . import main
from ..request import get_quotes