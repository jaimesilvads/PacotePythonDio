def juros_compostos(capital, taxa, tempo):
    montante  = capital *(1 + taxa /100) ** tempo
    lucro = montante - capital
    msg  = 'Sua aplicação renderá: {} no período de {} meses terá lucro de R$ {}'

    return print(msg.format(round(montante,2), tempo, round(lucro,2)))

def simular_emprestimo(valor, taxa_Ano, prazo):
    total = ((valor * taxa_Ano))* prazo + valor
    return  print('Total a pagar em 2 anos é : R$ {}'.format(total))

