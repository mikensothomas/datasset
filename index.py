import matplotlib.pyplot as plt

dados = open("populacao_brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.plot(x, y, color='blue')
plt.bar(x, y, color='red')
plt.xlabel("Anos")
plt.ylabel("Crescimento da população")
plt.show()
