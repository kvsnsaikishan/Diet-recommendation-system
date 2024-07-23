from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SelectField
from wtforms.validators import InputRequired

class UserInfoForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    weight = FloatField('Weight (kg)', validators=[InputRequired()])
    height = FloatField('Height (cm)', validators=[InputRequired()])
    age = IntegerField('Age', validators=[InputRequired()])
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')], validators=[InputRequired()])
    physical_activity = SelectField('Physical Activity Level', choices=[
        ('value1', 'Sedentary (little or no exercise)'),
        ('value2', 'Light Active (1-3 days/week)'),
        ('value3', 'Moderately Active (3-5 days/week)'),
        ('value4', 'Very Active (6-7 days/week)'),
        ('value5', 'Super Active (twice/day)')], validators=[InputRequired()])
    diet_type = SelectField('Diet Type', choices=[
        ('veg', 'Vegetarian'), ('nonveg', 'Non-Vegetarian'), ('vegan', 'Vegan')
    ], validators=[InputRequired()])
