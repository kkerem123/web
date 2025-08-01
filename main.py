from flask import Flask
import random

app = Flask(__name__)

facts = [
    "2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.",
    "Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.",
    "Elon Musk ayrıca sosyal ağların düzenlenmesini ve kullanıcıların kişisel verilerinin korunmasını savunmaktadır. Sosyal ağların hakkımızda büyük miktarda bilgi topladığını ve bu bilgilerin daha sonra düşüncelerimizi ve davranışlarımızı manipüle etmek için kullanılabileceğini iddia ediyor."
]

animals = ["panda", "fok", "kutup ayısı", "penguen"]


@app.route("/")
def ana_sayfa():
    return 'Merhaba sayfama hoş geldin \n <li><a href="/gercekler">Rastgele bir gerçeği görüntüle!</a></li>'

@app.route("/gercekler")
def gercekler():
    return f'<h3>{random.choice(facts)}</h3> <br> <li> <a href="/hayvan">rastgele bir hayvan ismi gör</a></li>'

@app.route("/hayvan")
def hayvan():
    return f"<h1>{random.choice(animals)}</h1>"
  

app.run(debug=True)
