from flask import Flask, jsonify, request, render_template, render_template_string

app=Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/inicio, methods=['POST']")
def formulario():
    if formulario == 'POST':
        user = request.form.get['email']
        
        return render_template_string('''
                <script>alert("Bienvenido, {{ user }}!");</script>
                <a href="/">Volver</a>
            ''', user=user)
        

if __name__=='__main__':
    app.run(debug=True)