from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, DateField, SelectField, FieldList
from wtforms.validators import DataRequired, InputRequired

traitlist = [(0, 'Active'),
 (1, 'Friendly'),
 (2, 'Creative'),
 (3, 'Clever'),
 (4, 'Self-Assured'),
 (5, 'Attractive'),
 (6, 'Perfectionist'),
 (7, 'Ambitious'),
 (8, 'Self-Aware'),
 (9, 'Open-minded'),
 (10, 'Empathic'),
 (11, 'Adaptable')]



class Choose_Character_Form(FlaskForm):
    boy = BooleanField(render_kw={ "class":"form-check-input"})
    girl = BooleanField(render_kw={"type":"checkbox"})
    trait0 = SelectField('Characteristic 1', choices=traitlist, render_kw={"placeholder": "Choose", "class":"form-control"})
    trait1 = SelectField('Characteristic 2', choices=traitlist, render_kw={"placeholder": "Choose", "class":"form-control"})
    trait2 = SelectField('Characteristic 3', choices=traitlist, render_kw={"placeholder": "Choose", "class":"form-control"})
    trait3 = SelectField('Characteristic 4', choices=traitlist, render_kw={"placeholder": "Choose", "class":"form-control"})
    trait4 = SelectField('Characteristic 5', choices=traitlist, render_kw={"placeholder": "Choose", "class":"form-control"})
    submit = SubmitField("Find name", render_kw={"class":"gradient-button gradient-button-1"})

