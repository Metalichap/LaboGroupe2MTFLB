from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed

class AttachmentForm(FlaskForm):
    file = FileField("File", validators=[FileRequired(),
						FileAllowed(
							["pdf", "png", "jpg", "jpeg"],
							"File type not allowed."
						)])