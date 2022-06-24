from flask import Flask, render_template, url_for

# ----------------------------APP INITIALIZATION-----------------------
app = Flask(__name__)


# -------------------------------ROUTES-------------------------------
@app.route("/")
@app.route("/home")
def home():
    header = 'header'
    return render_template("home.html", state=header, title='Zambia Conference of Catholic Bishops - Home')

@app.route("/about")
def about():
    header = 'about-header'
    return render_template("about.html", state=header, title='Zambia Conference of Catholic Bishops - About')


# BISHOP MULENGA AND KABWE DIOCESE
@app.route("/BishopMulenga")
def BishopM():
    header = 'about-header'
    return render_template("BishopMulenga.html", state=header, bishop='Bishop Mulenga', title='Zambia Conference of Catholic Bishops - Bishop Mulenga')

@app.route("/KabweDiocese")
def KabweDiocese():
    header = 'about-header'
    return render_template("KabweDiocese.html", state=header, bishop='KABWE DIOCESE', title='Zambia Conference of Catholic Bishops - Kabwe Diocese')


# BISHOP ZUMAILE AND CHIPATA DIOCESE
@app.route("/BishopZumaile")
def BishopZumaile():
    header = 'about-header'
    return render_template("BishopZumaile.html", state=header, bishop='Bishop Zumaile', title='Zambia Conference of Catholic Bishops - Bishop Zumaile')

@app.route("/ChipataDiocese")
def ChipataDiocese():
    header = 'about-header'
    return render_template("ChipataDiocese.html", state=header, bishop='CHIPATA DIOCESE', title='Zambia Conference of Catholic Bishops - Chipata Diocese')


#ARCHBISHOP CHAMA AND KASAMA DIOCESE
@app.route("/ArchbishopChama")
def ArchbishopChama():
    header = 'about-header'
    return render_template("ArchbishopChama.html", state=header, bishop='Archbishop Chama', title='Zambia Conference of Catholic Bishops - Archbishop Chama')

@app.route("/KasamaDiocese")
def KasamaDiocese():
    header = 'about-header'
    return render_template("KasamaDiocese.html", state=header, bishop='KASAMA DIOCESE', title='Zambia Conference of Catholic Bishops - Kasama Diocese')


# BISHOP KALUMBA AND LIVINGSTONE DIOCESE
@app.route("/BishopKalumba")
def BishopKalumba():
    header = 'about-header'
    return render_template("BishopKalumba.html", state=header, bishop='Bishop Kalumba', title='Zambia Conference of Catholic Bishops - Bishop Kalumba')

@app.route("/LivingstoneDiocese")
def LivingstoneDiocese():
    header = 'about-header'
    return render_template("LivingstoneDiocese.html", state=header, bishop='LINGSTONE DIOCESE', title='Zambia Conference of Catholic Bishops - Livingstone Diocese')


# ARCHBISHOP BANDA AND LUSAKA DIOCESE
@app.route("/ArchbishopBanda")
def ArchbishopBanda():
    header = 'about-header'
    return render_template("ArchbishopBanda.html", state=header, bishop='Archbishop Banda', title='Zambia Conference of Catholic Bishops - Archbishop Banda')

@app.route("/LusakaDiocese")
def LusakaDiocese():
    header = 'about-header'
    return render_template("LusakaDiocese.html", state=header, bishop='LUSAKA DIOCESE', title='Zambia Conference of Catholic Bishops - Lusaka Diocese')


# BISHOP CHILEKWA AND MANSA DIOCESE
@app.route("/BishopChilekwa")
def BishopChilekwa():
    header = 'about-header'
    return render_template("BishopChilekwa.html", state=header, bishop='Bishop Chilekwa', title='Zambia Conference of Catholic Bishops - Bishop Chilekwa')

@app.route("/MansaDiocese")
def MansaDiocese():
    header = 'about-header'
    return render_template("MansaDiocese.html", state=header, bishop='MANSA DIOCESE', title='Zambia Conference of Catholic Bishops - Mansa Diocese')


# BISHOP MULANDU AND MPIKA DIOCESE
@app.route("/BishopMulandu")
def BishopMulandu():
    header = 'about-header'
    return render_template("BishopMulandu.html", state=header, bishop='Bishop Mulandu', title='Zambia Conference of Catholic Bishops - Bishop Mulandu')

@app.route("/MpikaDiocese")
def MpikaDiocese():
    header = 'about-header'
    return render_template("MpikaDiocese.html", state=header, bishop='MPIKA DIOCESE', title='Zambia Conference of Catholic Bishops - Mpika Diocese')


# BISHOP MWEEMPWA AND MOZE DIOCESE
@app.route("/BishopMweempwa")
def BishopMweempwa():
    header = 'about-header'
    return render_template("BishopMweempwa.html", state=header, bishop='Bishop Mweempwa', title='Zambia Conference of Catholic Bishops - Bishop Mweempwa')

@app.route("/MonzeDiocese")
def MonzeDiocese():
    header = 'about-header'
    return render_template("MonzeDiocese.html", state=header, bishop='MONZE DIOCESE', title='Zambia Conference of Catholic Bishops - Monze Diocese')


# BISHOP KASONDE ADN SOLWEZI DIOCESE
@app.route("/BishopKasonde")
def BishopKasonde():
    header = 'about-header'
    return render_template("BishopKasonde.html", state=header, bishop='Bishop Kasonde', title='Zambia Conference of Catholic Bishops - Bishop Kasonde')

@app.route("/SolweziDiocese")
def SolweziDiocese():
    header = 'about-header'
    return render_template("SolweziDiocese.html", state=header, bishop='SOLWEZI DIOCESE', title='Zambia Conference of Catholic Bishops - Solwezi Diocese')


@app.route("/NdolaDiocese")
def NdolaDiocese():
    header = 'about-header'
    return render_template("NdolaDiocese.html", state=header, bishop='NDOLA DIOCESE', title='Zambia Conference of Catholic Bishops - Ndola Diocese')


@app.route("/MonguDiocese")
def MonguDiocese():
    header = 'about-header'
    return render_template("MonguDiocese.html", state=header, bishop='MONGU DIOCESE', title='Zambia Conference of Catholic Bishops - Mongu Diocese')

@app.route("/ArchbishopGallone")
def ArchbishopGallone():
    header = 'about-header'
    return render_template("ArchbishopGallone.html", state=header, bishop='Archbishop Gallone', title='Zambia Conference of Catholic Bishops - Archbishop Gallone')

# -------------------------------RUNNING IN DEBUG MODE-------------------------------
if __name__ == '__main__':
   app.run(debug = True)