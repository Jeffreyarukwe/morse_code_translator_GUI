from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from datetime import datetime

from encode import encode
from decode import decode
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("FLASK_KEY", "dev")
bootstrap = Bootstrap5(app)


class MorseToTextForm(FlaskForm):
    user_choices = ['text-to-morse', 'morse-to-text']

    user_input = StringField('Input: ', validators=[DataRequired()])
    conversion_type = SelectField(u'Convert: ', choices=user_choices, validators=[DataRequired()])
    submit = SubmitField('Convert')


@app.route('/', methods=['GET', 'POST'])
def morse_to_text_converter():
    form = MorseToTextForm()

    if form.validate_on_submit():
        user_input = form.user_input.data
        conversion_type = form.conversion_type.data

        if conversion_type == 'text-to-morse':
            result = encode(user_input)
        elif conversion_type == 'morse-to-text':
            result = decode(user_input)
        return render_template('index.html', form=form, result=result, current_year=datetime.now().year)

    return render_template('index.html', form=form, result=None, current_year=datetime.now().year)


if __name__ == '__main__':
    app.run(debug=False)
