#lista de bairros que tendem a alagar em época de chuva intesa (verão)
# https://imoveis.estadao.com.br/noticias/saiba-quais-sao-os-bairros-mais-suscetiveis-a-enchentes-e-alagamentos-em-sao-paulo/

bairros_alagados = ['Mooca', 'Vila Prudente', 'Tatuapé', 'Belenzinho', 'Bela Vista', 'Casa Verde',
                    'Vila Leopoldina', 'Cidade Jardim', 'Chácara Santo Antônio', 'Bosque da Saúde']

#principais meses de chuva intensa
meses_temporal = ['Dezembro', 'Janeiro', 'Fevereiro', 'Março']
#demais meses para consulta
demais_meses = ['Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro']

print('Bem-vido ao nosso projeto "GaloGuard", sistema preventivo para alagamentos nas vias urbanas')
print('')

while True:
    print (f'Bairros cadastrados: {bairros_alagados}')
    print('')
    bairro_user = input('Digite o bairro que queira consultar: ').lower() #input e normalização do dado para evitar erros de sintaxe
    if bairro_user in [bairro.lower() for bairro in bairros_alagados]: #verificação do input e normalização da lista
        while True:
            mes_user = input('Digite o mês corrente: ').lower()
            if mes_user in [mes.lower() for mes in meses_temporal]:
                print (f'O bairro {bairro_user.capitalize()} tende a alagar no mês de {mes_user.capitalize()}. Tome cuidado!')
                break
            elif mes_user in [mes.lower() for mes in demais_meses]:
                print (f'O bairro {bairro_user.capitalize()} não tende a alagar no mês de {mes_user.capitalize()}. Fique tranquilo!')
            else:
                print('')
                print('Mês não encontrado, verifique se contém abreviação ou erro ortográfico') #mensagem de erro ao usuário
        break
    else:
        print('')
        print('Bairro não encontrado, verifique se contém abreviação ou erro ortográfico')
