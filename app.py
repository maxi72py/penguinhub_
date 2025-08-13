# imports
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comentarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelos
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mensaje = db.Column(db.Text, nullable=False)

class Tema(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    contenido = db.Column(db.Text, nullable=False)
    analogia = db.Column(db.Text, nullable=True)
    challenge = db.Column(db.Text, nullable=True)
    solucion = db.Column(db.Text, nullable=True)

with app.app_context():
    db.create_all()

# Función para manejar temas
@app.route('/tema', methods=['POST'])
def manejar_tema():
    accion = request.form.get('accion')
    tema_id = request.form.get('id')

    if accion == "agregar":
        nueva = Tema(
            titulo=request.form.get("titulo"),
            descripcion=request.form.get("descripcion"),
            contenido=request.form.get("contenido"),
            analogia=request.form.get("analogia"),
            challenge=request.form.get("challenge"),
            solucion=request.form.get("solucion")
        )
        db.session.add(nueva)
        db.session.commit()

    elif accion == "editar" and tema_id:
        return redirect(url_for("editar_tema", tema_id=tema_id))

    elif accion == "eliminar" and tema_id:
        tema = Tema.query.get(tema_id)
        if tema:
            db.session.delete(tema)
            db.session.commit()

    return redirect("/")

# Ruta para editar tema
@app.route('/tema/editar/<int:tema_id>', methods=['GET'])
def editar_tema(tema_id):
    tema = Tema.query.get_or_404(tema_id)
    temas = Tema.query.all()
    return render_template('index.html', temas=temas, tema_editando=tema)

# Función para manejar feedback
@app.route('/feedback', methods=['POST'])
def manejar_feedback():
    accion = request.form.get('accion')
    feedback_id = request.form.get('id')

    if accion == 'agregar':
        nuevo_feedback = Feedback(mensaje=request.form.get('mensaje'))
        db.session.add(nuevo_feedback)
        db.session.commit()

    elif accion == 'editar' and feedback_id:
        # Redirige a home con query param para mostrar el form de edición
        return redirect(url_for('home', editar=feedback_id) + '#dia1')

    elif accion == 'actualizar' and feedback_id:
        feedback = Feedback.query.get(feedback_id)
        if feedback:
            feedback.mensaje = request.form.get('mensaje')
            db.session.commit()

    elif accion == 'eliminar' and feedback_id:
        feedback = Feedback.query.get(feedback_id)
        if feedback:
            db.session.delete(feedback)
            db.session.commit()

    return redirect(url_for('home') + '#dia1')

# Ruta principal combinando temas y feedback
@app.route('/', methods=['GET'])
def home():
    temas = Tema.query.all()
    comentarios = Feedback.query.all()
    feedback_editando_id = request.args.get('editar')
    feedback_editando = Feedback.query.get(feedback_editando_id) if feedback_editando_id else None
    return render_template('index.html', temas=temas, feedback=comentarios, feedback_editando=feedback_editando)

if __name__ == "__main__":
    app.run(debug=True)
