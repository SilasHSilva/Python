custo_fabrica = float(input("Digite o custo de fabrica do veiculo: "))
percent_distr = custo_fabrica * 0.28
percent_imposto = custo_fabrica * 0.45

custo_final = custo_fabrica + percent_distr + percent_imposto

print(f"Custo final do veiculo eh R${custo_final:.2f}")