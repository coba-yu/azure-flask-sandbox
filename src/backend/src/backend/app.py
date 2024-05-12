"""Backend App."""

import os

from flask import Flask, render_template
from identity.flask import Auth

from . import app_config

app = Flask(__name__)
app.config.from_object(app_config)

auth = Auth(
    app=app,
    authority=f'https://login.microsoftonline.com/{os.getenv("AZURE_APP__TENANT_ID")}',
    client_id=os.getenv("AZURE_APP__CLIENT_ID"),
    client_credential=os.getenv("AZURE_APP__CLIENT_SECRET"),
    redirect_uri=os.getenv("AZURE_APP__REDIRECT_URI"),
)


@app.route("/")
@auth.login_required
def index(*, context) -> str:
    """Index page."""
    print("Request for index page received")
    return render_template(
        "index.html",
        user=context["user"],
        edit_profile_url=auth.get_edit_profile_url(),
        api_endpoint=os.getenv("AZURE_APP__API_ENDPOINT"),
    )


if __name__ == "__main__":
    app.run()
