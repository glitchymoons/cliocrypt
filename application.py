from flask import Flask, render_template, request
import caesar
import vigenere
import scytale

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Disable caching
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Routes
@app.route("/")
def index():
    return render_template("index.html")


# CAESAR
@app.route("/caesar", methods=["GET"])
def caesar_get():
   return render_template("caesar.html")

@app.route("/caesar_enc", methods=["POST"])
def caesar_enc():

    # Check input
    if not request.form.get("plaintext") or not request.form.get("key"):
        return render_template("error.html", message="Enter valid text and a valid key!")

    plaintext = request.form.get("plaintext")
    keyE = int(request.form.get("key"))

    result = caesar.caesarEnc(plaintext, keyE)

    inptE = plaintext
    outptE = result

    # Output ciphertext
    return render_template("caesar.html", inptE=inptE, keyE=keyE, outptE=outptE)

@app.route("/caesar_dec", methods=["POST"])
def caesar_dec():

    # Check input
    if not request.form.get("ciphertext") or not request.form.get("key"):
        return render_template("error.html", message="Enter valid text and a key!")

    ciphertext = request.form.get("ciphertext")
    keyD = int(request.form.get("key"))

    result = caesar.caesarDec(ciphertext, keyD)

    inptD = ciphertext
    outptD = result

    # Output ciphertext
    return render_template("caesar.html", inptD=inptD, keyD=keyD, outptD=outptD)


# VIGENERE
@app.route("/vigenere", methods=["GET"])
def vigenere_get():
   return render_template("vigenere.html")

@app.route("/vigenere_enc", methods=["POST"])
def vigenere_enc():

    # Check input
    if not request.form.get("plaintext") or not request.form.get("key"):
        return render_template("error.html", message="Enter valid text and a valid keyword!")

    plaintext = request.form.get("plaintext")
    key = str(request.form.get("key"))

    keyE = ""

    # Check that keyword is a word
    for c in key:
        if not c.isalpha():
            return render_template("error.html", message="Enter valid text and a keyword!")
        else:
            keyE += c

    result = vigenere.vigenereEnc(plaintext, keyE)

    inptE = plaintext
    outptE = result

    # Output ciphertext
    return render_template("vigenere.html", inptE=inptE, keyE=keyE, outptE=outptE)

@app.route("/vigenere_dec", methods=["POST"])
def vigenere_dec():

    # Check input
    if not request.form.get("ciphertext") or not request.form.get("key"): #CRASHES IF KEY IS ONLY NON-ALPHA!!!!!!! code 400
        return render_template("error.html", message="Enter valid text and a keyword!")

    ciphertext = request.form.get("ciphertext")
    key = str(request.form.get("key"))

    keyD = ""

    # Check that keyword is a word
    for c in key:
        if not c.isalpha():
            return render_template("error.html", message="Enter valid text and a keyword!")
        else:
            keyD += c

    result = vigenere.vigenereDec(ciphertext, keyD)

    inptD = ciphertext
    outptD = result

    # Output ciphertext
    return render_template("vigenere.html", inptD=inptD, keyD=keyD, outptD=outptD)


# SCYTALE
@app.route("/scytale", methods=["GET"])
def scytale_get():
   return render_template("scytale.html")

@app.route("/scytale_enc", methods=["POST"])
def scytale_enc():

    # Check input
    if not request.form.get("plaintext") or not request.form.get("key"):
        return render_template("error.html", message="Enter valid text and a valid keyword!")

    plaintext = request.form.get("plaintext")
    keyE = str(request.form.get("key"))

    result = scytale.scytaleEnc(plaintext, int(keyE))

    inptE = plaintext
    outptE = result

    # Output ciphertext
    return render_template("scytale.html", inptE=inptE, keyE=keyE, outptE=outptE)

@app.route("/scytale_dec", methods=["POST"])
def scytale_dec():

    # Check input
    if not request.form.get("ciphertext") or not request.form.get("key"):
        return render_template("error.html", message="Enter valid text and a keyword!")

    ciphertext = request.form.get("ciphertext")
    keyD = str(request.form.get("key"))

    result = scytale.scytaleDec(ciphertext, int(keyD))

    inptD = ciphertext
    outptD = result

    # Output ciphertext
    return render_template("scytale.html", inptD=inptD, keyD=keyD, outptD=outptD)
