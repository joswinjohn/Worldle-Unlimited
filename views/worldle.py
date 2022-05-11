from flask import session

@bp.route('/worldle', methods=('GET', 'POST'))
def worldle:
  return render_template(index.html)
