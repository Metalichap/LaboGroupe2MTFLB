from flask import flash, redirect, render_template, request, url_for


from app import app
from app.framework.decorators.auth_required import auth_required
from app.framework.decorators.inject import inject
from app.services.auth_service import AuthService
from app.models.role import RoleStatus
from app.services.team_service import TeamService
from app.forms.team.team_form import TeamInsertForm

@app.route("/team/add", methods=["GET", "POST"])
@auth_required(level=RoleStatus.ADMIN)
@inject
def team_add(team_service: TeamService):
    form = TeamInsertForm()

    if form.validate_on_submit():
        team = team_service.insert(form)

        if team is None:
            flash("Ce nom d'équipe est déjà utilisé.", "danger")
        else:
            flash("Equipe créée.", "success")
            return redirect(url_for("team_list"))

    return render_template("teams/add.html")