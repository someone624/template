from flask import render_template

def render_error_page(error_code, error_message):
    # Render a generic error page
    return render_template('error_template.html', error_code=error_code, error_message=error_message), error_code