from wtforms import form, StringField, PasswordField, validators
from werkzeug.security import generate_password_hash, check_password_hash
from ....models import db
from ....models.user import User

class LoginForm(form.Form):
    login = StringField(validators=[validators.required()])
    password = PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError('Invalid user')

        if not check_password_hash(user.password, self.password.data):
        # if user.password != self.password.data:
            raise validators.ValidationError('Invalid password')

    def get_user(self):
        return db.session.query(User).filter_by(login=self.login.data).first()