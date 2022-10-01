from flask import Flask, request, render_template

app = Flask("mainapp")


def encrypt_algorithm(string, key):
    s = key + string + key
    return s


def decrypt_algorithm(string, key):
    return string[len(key):len(string)-len(key)]


@app.route('/encrypt')
@app.route("/")
def start_page():
    return render_template("startpage.html")


@app.route("/do_encrypt")
def encrypting():
    string = request.args.get("crypt_string")
    key = request.args.get("crypt_key")
    encrypted_string = encrypt_algorithm(string, key)
    return render_template("result_page.html", result=encrypted_string)


@app.route("/decrypt")
def decrypt_page():
    return render_template("decrypt_page.html")


@app.route("/do_decrypt")
def decrypting():
    string = request.args.get("crypt_string")
    key = request.args.get("crypt_key")
    decrypted_string = decrypt_algorithm(string, key)
    return render_template("result_page.html", result=decrypted_string)


app.run()
