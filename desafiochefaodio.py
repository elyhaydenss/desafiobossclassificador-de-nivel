def verificar_medalha(xp):
    medalha = ""
    match xp:
        case x if x < 1000:
            medalha = "Ferro"
        case x if 1001 <= x <= 2000:
            medalha = "Bronze"
        case x if 2001 <= x <= 5000:
            medalha = "Prata"
        case x if 5001 <= x <= 7000:
            medalha = "Ouro"
        case x if 7001 <= x <= 8000:
            medalha = "Platina"
        case x if 8001 <= x <= 9000:
            medalha = "Ascendente"
        case x if 9001 <= x <= 10000:
            medalha = "Imortal"
        case _:
            medalha = "Radiante" if xp >= 10001 else "Erro: XP inválido"
    return medalha


nomeheroi =input("Digite o Nome do Heroi: ")
xpstr = input("Digite o Xp: ")
xp =int(xpstr)
print(f"O Herói de nome **{nomeheroi}** está no nível de **{verificar_medalha(xp)}**")  
