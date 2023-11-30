# mengimpor modul flask
from flask import Flask, request, render_template

# membuat objek aplikasi
app = Flask(__name__)

# membuat fungsi untuk memeriksa data login
def check_login(username, password):
    # asumsikan data login yang benar adalah admin dan 1234
    if username == "admin" and password == "1234":
        return True
    else:
        return False

# membuat URL /hello dengan metode GET
@app.route("/hello")
def hello():
    # mengembalikan teks Hello, World! sebagai respons
    return "Hello, World!"

# membuat URL /login dengan metode GET dan POST
@app.route("/login", methods=["GET", "POST"])
def login():
    # memeriksa metode permintaan
    if request.method == "GET":
        # merender template login.html sebagai respons
        return render_template("login.html")
    elif request.method == "POST":
        # mengambil data username dan password dari form
        username = request.form["username"]
        password = request.form["password"]
        # memeriksa data login dengan fungsi check_login
        if check_login(username, password):
            # mengembalikan teks Login berhasil! sebagai respons
            return "Login berhasil!"
        else:
            # mengembalikan teks Login gagal! sebagai respons
            return "Login gagal!"

# menjalankan aplikasi
if __name__ == "__main__":
    app.run()
