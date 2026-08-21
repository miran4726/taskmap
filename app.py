from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return """
    <div style="font-family:'Inter',sans-serif; text-align:center; padding-top:120px; background:#f8fafc; color:#1e293b; height:100vh;">
        <h2 style="font-size:28px; margin-bottom:10px; color:#0284c7;">TaskMap Giriş Paneli</h2>
        <p style="color:#64748b;">Kullanıcı girişi modülü açılıyor...</p>
        <br>
        <a href="/" style="display:inline-block; padding:10px 20px; background:#0284c7; color:#fff; font-weight:600; border-radius:8px; text-decoration:none;">← Anasayfaya Dön</a>
    </div>
    """

@app.route('/register')
def register():
    return """
    <div style="font-family:'Inter',sans-serif; text-align:center; padding-top:120px; background:#f8fafc; color:#1e293b; height:100vh;">
        <h2 style="font-size:28px; margin-bottom:10px; color:#0284c7;">TaskMap Ücretsiz Kayıt</h2>
        <p style="color:#64748b;">Hesap oluşturma sihirbazı yükleniyor...</p>
        <br>
        <a href="/" style="display:inline-block; padding:10px 20px; background:#0284c7; color:#fff; font-weight:600; border-radius:8px; text-decoration:none;">← Anasayfaya Dön</a>
    </div>
    """

if __name__ == '__main__':
    app.run(debug=True)
