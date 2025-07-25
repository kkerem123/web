from flask import Flask
import random

app = Flask(__name__)
facts = ["2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.",
         "Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.",
         "Elon Musk ayrıca sosyal ağların düzenlenmesini ve kullanıcıların kişisel verilerinin korunmasını savunmaktadır. Sosyal ağların hakkımızda büyük miktarda bilgi topladığını ve bu bilgilerin daha sonra düşüncelerimizi ve davranışlarımızı manipüle etmek için kullanılabileceğini iddia ediyor."]

@app.route("/")
def ana_sayfa():
    return  f' Merhaba sayfama hoş geldin \n <li><a href="/gercekler">Rastgele bir gerçeği görüntüle!</a></li>'

@app.route("/gercekler")
def gercekler():
    return f"<h3>{random.choice(facts)}</h3>"
app.run(debug=True)
