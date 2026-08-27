from flask import render_template, flash, redirect, url_for

from app import app
from app.framework.decorators.inject import inject
from app.framework.decorators.auth_required import auth_required
from app.services.site_service import SiteService
from app.forms.site.site_form import SiteForm

@app.route('/sites', methods=['GET'])
@auth_required()
@inject
def sites_list(site_service: SiteService):
    return render_template('sites/list.html',
    sites=site_service.find_all())

@app.route('/sites/add', methods=['GET', 'POST'])
@auth_required()
@inject
def site_add(site_service: SiteService):
    form = SiteForm()

    if form.validate_on_submit():
        site = site_service.insert(form)

        if site is None:
            flash("Ce site existe déjà.", "danger")
        else:
            flash("Site créé.", "success")
            return redirect(url_for('sites_list'))

    return render_template('sites/add_or_update.html',
    form=form, site=None)

@app.route('/sites/<int:site_id>/edit', methods=['GET', 'POST'])
@auth_required()
@inject
def site_update(site_id: int, site_service: SiteService):
    site = site_service.find_one(site_id)

    if site is None:
        flash("Site introuvable.", "warning")
        return redirect(url_for('sites_list'))

    form = SiteForm(obj=site)

    if form.validate_on_submit():
        updated = site_service.update(site_id, form)

        if updated is None:
            flash("Ce site existe déjà.", "danger")
        else:
            flash("Site créé.", "success")
            return redirect(url_for('sites_list'))

    return render_template('sites/add_or_update.html',
    form=form, site=site)

@app.post('/sites/<int:site_id>/delete')
@auth_required()
@inject
def site_delete(site_id: int, site_service: SiteService):
    if site_service.delete(site_id) is None:
        flash("Suppression impossible.", "danger")
    else:
        flash("Site désactivée.", "success")

    return redirect(url_for('sites_list'))