# %%

meus_dados = {}

meus_dados["nome"] = "Rodrigo"

meus_dados["sobrenome"] = "Luparelli"

meus_dados["esposa"] = {"nome":"Daiane", "idade":35}

meus_dados["exs"] = ['Stéfani', "Maria", "Clara"]

meus_dados['descendentes'] = [{"nome":"Pedro"}, {"nome":"benjamin"}]

meus_dados

# %%

meus_dados["esposa"]["idade"]

meus_dados["esposa"]["profissao"] = "Vendedora"

meus_dados

# %%

meus_dados["descendentes"].append({"nome": "Tiky"})
meus_dados

# %%

# Descobrindo as chaves de um dicionário
meus_dados.keys()

# %%

# Descobrindo valores
meus_dados.values()

# %%

# Tuplas de chave/valor
meus_dados.items()

# %%

del meus_dados["exs"]
meus_dados
# %%

lupa = {"nome":"Lupa", "idade":35}

mais_infos = {"profissao": "Dev",
              "tempo no cargo": 2}

novas_infos = {"esposa":"Daiane"}

lupa.update(mais_infos)
lupa.update(novas_infos)
lupa