from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators
from wtforms.validators import DataRequired, URL, Email, Length
from flask_ckeditor import CKEditorField


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    nickname = StringField("Enter a username (will not be displayed in website)", validators=[DataRequired(), Length(min=4)], render_kw={"autocomplete": "off"})
    password = PasswordField("Enter a Password", validators=[DataRequired(), Length(min=8)], render_kw={"autocomplete": "off"})
    name = StringField("Enter a Name (will be displayed as author of posts)", validators=[DataRequired()], render_kw={"autocomplete": "off"})
    submit = SubmitField("Register!")

class LoginForm(FlaskForm):
    nickname = StringField("Username", validators=[DataRequired()], render_kw={"autocomplete": "off"})
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)], render_kw={"autocomplete": "off"})
    submit = SubmitField("Log in!")

class CommentForm(FlaskForm):
    body = CKEditorField("Comment", validators=[DataRequired()], render_kw={"autocomplete": "off"})
    submit = SubmitField("Submit Comment")