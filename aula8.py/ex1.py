def exibir_info(**kwargs):
    for chave,valor in kwargs.items():
        print(f"{chave}:{valor}")

print(exibir_info(nome = "Thiago", cidade = "Rio Claro"))