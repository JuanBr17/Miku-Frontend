from flask import Flask, jsonify, request, render_template, render_template_string
import pymysql

app=Flask(__name__)

def conectar(vhost, vuser, vpass, vdb):
    conn= pymysql.connect(host=vhost, user=vuser, passwd=vpass, db= vdb)
    return conn


@app.route("/", methods=['GET'])
def inicio():
    return render_template("index.html")


@app.route("/registrar", methods=['GET','POST'])
def add():
    try:
        if request.method == 'POST':
            usuario = request.form.get('email')
            contrasena = request.form.get('passw')
            print(usuario)
            print(contrasena)
        
        
            conn=conectar('localhost', 'root', '1711', 'usuarios')    
            cur = conn.cursor()
            cur.execute("INSERT into usuarios (usuario, contrasena) VALUES (%s, %s)", (usuario, contrasena))
            conn.commit()
            cur.close()
            conn.close()
        else:
            print("hola")
            
        return  render_template("prueba.html")
    except Exception as error:
        print(error)
        
        return render_template("prueba.html")

        

if __name__=='__main__':
    app.run(debug=True)