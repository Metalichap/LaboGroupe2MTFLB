"""Controller des catégories: listing, ajout, édition, suppression.

Même motif POST/Redirect/GET que dans user_controller.py.
Accès simplement authentifié pour l'instant (@auth_required() sans niveau).
La gestion des permissions (technicien, admin, ... ) sera fignolée avec Théo
"""
from flask import flash, redirect, render_template, url_for

from app import app
from app.forms.category.category_form import CategoryForm
from app.framework.decorators.auth_required import auth_required
from app.framework.decorators.inject import inject
from app.services.category_service import CategoryService


@app.get('/categories')
@auth_required()
@inject
def category_list(category_service: CategoryService):
    return render_template('categories/list.html', categories=category_service.find_all())


@app.route('/categories/add', methods=['GET', 'POST'])
@auth_required()
@inject
def category_add(category_service: CategoryService):
    form = CategoryForm()

    if form.validate_on_submit():
        category = category_service.insert(form)

        if category is None:
            flash("Ce nom de catégorie est déjà utilisé.", "danger")
        else:
            flash("Catégorie créée.", "success")
            return redirect(url_for('category_list'))

    # category=None -> le template add_or_update.html affiche "Nouvelle catégorie"
    return render_template('categories/add_or_update.html', form=form, category=None)


@app.route('/categories/<int:category_id>/edit', methods=['GET', 'POST'])
@auth_required()
@inject
def category_update(category_id: int, category_service: CategoryService):
    category = category_service.find_one(category_id)

    if category is None:
        flash("Catégorie introuvable.", "warning")
        return redirect(url_for('category_list'))

    # obj=category pré-remplit les champs de même nom en GET.
    form = CategoryForm(obj=category)

    if form.validate_on_submit():
        updated = category_service.update(category_id, form)

        if updated is None:
            flash("Ce nom de catégorie est déjà utilisé.", "danger")
        else:
            flash("Catégorie mise à jour.", "success")
            return redirect(url_for('category_list'))

    return render_template('categories/add_or_update.html', form=form, category=category)


@app.post('/categories/<int:category_id>/delete')
@auth_required()
@inject
def category_delete(category_id: int, category_service: CategoryService):
    """Désactive une catégorie (soft delete).

    En POST et pas en GET: une action qui modifie l'état ne doit jamais être
    accessible par un simple lien.
    """
    if category_service.delete(category_id) is None:
        flash("Suppression impossible.", "danger")
    else:
        flash("Catégorie désactivée.", "success")

    return redirect(url_for('category_list'))