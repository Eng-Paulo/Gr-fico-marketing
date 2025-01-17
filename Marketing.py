import matplotlib.pyplot as plt


class Campanha:
    def __init__(self, canal, investimentos, cliques, conversoes):
        self.canal = canal
        self.investimentos = investimentos
        self.cliques = cliques
        self.conversoes = conversoes

    def cpc(self):
        return self.investimentos / self.cliques


campanhas = [
    Campanha("Facebook Ads", 2000, 15000, 15000),
    Campanha("Google Ads", 1200, 1000, 200),
    Campanha("Email Ads", 1000, 5000, 50),
    Campanha("Instagram Ads", 8000, 19000, 190),
]

canais = [c.canal for c in campanhas]
cpcs = [c.cpc() for c in campanhas]


plt.bar(canais, cpcs)
plt.title("Custos por cliques")
plt.xlabel("Canais")
plt.ylabel("Custo em real")
plt.show()


###########
