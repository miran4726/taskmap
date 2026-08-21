from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return """
    <div style="font-family:'Plus Jakarta Sans',sans-serif; text-align:center; padding-top:120px; background:#0b0f19; color:#fff; height:100vh;">
        <h2 style="font-size:28px; margin-bottom:10px;">Giriş Yap</h2>
        <p style="color:#94a3b8;">TaskMap kullanıcı paneline yönlendiriliyorsunuz...</p>
        <br>
        <a href="/" style="display:inline-block; padding:10px 20px; background:#38bdf8; color:#0b0f19; font-weight:700; border-radius:8px; text-decoration:none;">Anasayfaya Dön</a>
    </div>
    """

@app.route('/register')
def register():
    return """
    <div style="font-family:'Plus Jakarta Sans',sans-serif; text-align:center; padding-top:120px; background:#0b0f19; color:#fff; height:100vh;">
        <h2 style="font-size:28px; margin-bottom:10px;">Hesap Oluştur</h2>
        <p style="color:#94a3b8;">Ücretsiz kayıt sihirbazı hazırlanıyor...</p>
        <br>
        <a href="/" style="display:inline-block; padding:10px 20px; background:#38bdf8; color:#0b0f19; font-weight:700; border-radius:8px; text-decoration:none;">Anasayfaya Dön</a>
    </div>
    """

if __name__ == '__main__':
    app.run(debug=True)
