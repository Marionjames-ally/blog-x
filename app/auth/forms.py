from flask_wtf import FlaskForm
from wtf_forms import StringField, PasswordField, SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError

class RegistrationForm(FlaskForm):

    email = StringField('Enter your email address',validators=[Required(),Email()])
    username = StringField( 'enter username',validators = [Required()])
    password = PasswordField('Password',validators = [Required(),
    EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up')
    
    """ password and email validation """
        
    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('email is taken.')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('username is not available')
          
          
          
class LoginForm(FlaskForm):
  email = StringField('Enter your email Address',validators = [Required(),Email()])
  password = PasswordField('enter your password',validators = [Required()])
  remember = BooleanField('Remember me')
  submit = SubmitField('Sign In')
