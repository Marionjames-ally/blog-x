from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField,RadioField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError

class BlogForm(FlaskForm):
	title = StringField('Title', validators=[Required()])
	content = TextAreaField("Post Blog",validators=[Required()])
	submit = SubmitField('POST')