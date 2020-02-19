from ..models import Quotes
from flask import render_template, request, redirect, url_for, flash
from ..models import User, Blogs, Comment, Subscriber
from flask_login import login_required, current_user
from . import main
from ..request import get_quotes


@main.route('/')
def index():
    """
    returns the index page and its data
    :return:
    """
    title = 'HOME'
    quotes = get_quotes()
    return render_template('index.html', title=title, quotes=quotes)


@main.route('/quotes/<int:id>')
def quotes():
    """
    view quotes and its data
    :return:
    """
    quote = get_quotes(id)
    title = 'HOME OF QUOTES'
    return render_template('quotes.html', quote=quote, title=title)
