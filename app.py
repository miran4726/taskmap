from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return """
    <div style="font-family:sans-serif; text-align:center; padding-top:100px; background:#0f172a; color:#fff; height:100vh;">
        <h2>TaskMap Güvenli Giriş Ekranı</h2>
        <p style="color:#94a3b8; margin-top:10px;">Giriş modülü aktif ediliyor...</p>
        <a href="/" style="display:inline-block; margin-top:20px; color:#38bdf8; text-decoration:none;">← Anasayfaya Dön</a>
    </div>
    """

@app.route('/register')
def register():
    return """
    <div style="font-family:sans-serif; text-align:center; padding-top:100px; background:#0f172a; color:#fff; height:100vh;">
        <h2>TaskMap Hesap Oluşturma Sihirbazı</h2>
        <p style="color:#94a3b8; margin-top:10px;">Kayıt formu hazırlanıyor...</p>
        <a href="/" style="display:inline-block; margin-top:20px; color:#38bdf8; text-decoration:none;">← Anasayfaya Dön</a>
    </div>
    """

if __name__ == '__main__':
    app.run(debug=True)
