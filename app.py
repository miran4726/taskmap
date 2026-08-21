from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return """
    <div style="font-family:'Segoe UI',sans-serif; text-align:center; padding-top:100px; background:#f8f9fa; color:#333; height:100vh;">
        <h2 style="color:#0056b3; font-size:26px; margin-bottom:10px;">TaskMap Kurumsal Giriş</h2>
        <p style="color:#666;">Kullanıcı kimlik doğrulama modülü yükleniyor...</p>
        <br>
        <a href="/" style="display:inline-block; padding:8px 20px; background:#0056b3; color:#fff; font-weight:600; border-radius:4px; text-decoration:none;">← Anasayfaya Dön</a>
    </div>
    """

@app.route('/register')
def register():
    return """
    <div style="font-family:'Segoe UI',sans-serif; text-align:center; padding-top:100px; background:#f8f9fa; color:#333; height:100vh;">
        <h2 style="color:#0056b3; font-size:26px; margin-bottom:10px;">TaskMap Kurumsal Kayıt</h2>
        <p style="color:#666;">Yeni işletme hesabı oluşturma sihirbazı açılıyor...</p>
        <br>
        <a href="/" style="display:inline-block; padding:8px 20px; background:#0056b3; color:#fff; font-weight:600; border-radius:4px; text-decoration:none;">← Anasayfaya Dön</a>
    </div>
    """

if __name__ == '__main__':
    app.run(debug=True)
