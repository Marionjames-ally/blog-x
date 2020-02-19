from ..models import Quotes
from flask import render_template, request, redirect, url_for, flash
from ..models import User, Blogs, Comment, Subscriber
from flask_login import login_required, current_user
from . import main
from ..request import get_quotes
from .forms import BlogForm, CommentForm
from .. import db


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

@main.route('/comments/<blog_id>', methods = ['GET', 'POST'])
def comment(blog_id):
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = comment_form.comment.data 
        blog_id = blog_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id)
        new_comment.save_comment()
        return redirect(url_for('.index'))
    return render_template('comments.html', comment_form =comment_form)

@main.route('/view/comments/<blog_id>')
def view_comments(blog_id):
    '''
    Function that returs  the comments belonging to a particular pitch
    '''
    comments = Comment.get_comments(blog_id)
    blog_id = blog_id

    return render_template('view_comments.html',comments = comments, blog_id=blog_id)

@main.route('/delete/<blog_id>')
@login_required
def delete(blog_id):
    deleteitem = Blogs.query.filter_by(id=blog_id).first()

    db.session.delete(deleteitem)
    db.session.commit()

    return redirect(url_for('main.index'))