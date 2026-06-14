import pickle


with open("usuario_vitoria.pkl", "rb") as arquivo:
    nome = pickle.load(arquivo)


print(nome)