from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , SubmitField , ValidationError
from wtforms.validators import DataRequired , Email , EqualTo , Length , Regexp
from flask_wtf.file import FileAllowed,FileField
from flask_login import current_user
from blog.models import User

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('User Name',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(), 
                                                    EqualTo('pass_confirm'), 
                                                    Length(min=8, message='Password must be at least 8 characters long'), 
                                                    Regexp(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*()_+{}[\]:;<>,.?~\\-])',message='Password must contain at least 1 uppercase letter, 1 lowercase letter, and 1 special symbol')
                                                    ]
                            )
    pass_confirm = PasswordField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField('Register')

    def check_email(self,field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError('Email Already Registered')
        
    def check_username(self,field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError('User Name Already Registered')
        
class UpdateUserForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('User Name',validators=[DataRequired()])
    picture = FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    def check_email(self,field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError('Email Already Registered')
        
    def check_username(self,field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError('User Name Already Registered')
