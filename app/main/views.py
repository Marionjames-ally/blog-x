from ..models import Quotes
from flask import render_template, request, redirect, url_for, flash
from ..models import User, Blogs, Comment, Subscriber
from flask_login import login_required, current_user
from . import main
from ..request import get_quotes
from .forms import BlogForm


@main.route('/')
def index():
    """
    returns the index page and its data
    :return:
    """
    title = 'HOME'
    quotes = get_quotes()
    blogs = Blogs.query.all()
    return render_template('index.html', title=title, quotes=quotes, blogs=blogs)


#  function to add blog
@main.route('/blog', methods = ['GET', 'POST'])
@login_required
def blog():
	form = BlogForm()
	if form.validate_on_submit():
		title = form.title.data
		content = form.content.data

		new_blog = Blogs(blog_title = title, blog_content = content, user = current_user)
		new_blog.save_blog()
		return redirect (url_for('.index'))

	return render_template('blog.html', blog_form = form)
