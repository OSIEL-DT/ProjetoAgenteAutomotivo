from app.protocol.mcp import send_message

def get_valid_input(prompt, input_type='str', valid_options=None, max_length=None):
    while True:
        user_input = input(prompt).strip()
        
        if not user_input:  # Se for vazio, retorna None
            return None
            
        if input_type == 'int':
            if user_input.isdigit():
                return int(user_input)
            print("Apenas números são válidos. Tente novamente.")
        elif input_type == 'float':
            if user_input.replace('.', '', 1).isdigit():
                return float(user_input)
            print("Apenas números são válidos. Tente novamente.")
        elif input_type == 'option':
            if valid_options and user_input.lower() in [opt.lower() for opt in valid_options]:
                # Retorna a versão correta (com capitalização igual à das opções)
                for opt in valid_options:
                    if user_input.lower() == opt.lower():
                        return opt
            print(f"Opção inválida. Tente novamente.")

        elif input_type == 'word':
            if user_input.replace(' ', '').isalpha():
                if max_length and len(user_input) > max_length:
                    print(f"Por favor, digite no máximo {max_length} caracteres. Tente novamente.")
                else:
                    return user_input
            else:
                print("Por favor, digite apenas letras e espaços. Tente novamente.")
        else:  # string normal
            return user_input

def main():
    print("============================================================================================================================")
    print("Olá! Seja bem-vindo ao nosso sistema de busca de veículos. Por favor, informe os filtros desejados.")
    filtros = {}

    print("------------------------------------------------------------------------------------------------------------------------||||")
    MARCAS_VALIDAS = ['Fiat', 'Ford', 'Volkswagen', 'Chevrolet', 'Toyota', 'Honda', 'Hyundai', 'Renault', 'Nissan', 'Kia', 'Jeep', 'Peugeot', 'Citroën', 'Mitsubishi', 'Suzuki', 'Mazda', 'Subaru', 'Volvo', 'Audi', 'BMW', 'Mercedes-Benz', 'Lamborghini', 'Ferrari', 'Mclaren', 'Bugatti', 'Lamborghini', 'Ferrari', 'Mclaren', 'Bugatti']
    COMBUSTIVEIS_VALIDOS = ['Gasolina', 'Etanol', 'Flex', 'Diesel', 'Elétrico', 'Híbrido']
    CORES_VALIDAS = ['Preto', 'Branco', 'Vermelho', 'Prata', 'Cinza', 'Azul', 'Verde', 'Amarelo', 'Laranja', 'Roxo', 'Marrom', 'Bege', 'Dourado', 'Ciano', 'Magenta']
    TRANSMISSOES_VALIDAS = ['Manual', 'Automático', 'Automatizado', 'CVT', 'Semi-Automático', 'Dual-Clutch', 'Híbrido', 'Elétrico']


    print("------------------------------------------------------------------------------------------------------------------------||||")

    modelo = get_valid_input("Qual marca você procura? (ex: Fiat, Ford...) ", 
                           input_type='option', 
                           valid_options=MARCAS_VALIDAS)
    if modelo:
        filtros['brand'] = modelo

    print("------------------------------------------------------------------------------------------------------------------------||||")

    ano = get_valid_input("Digite o ano específico? (ex: 2015) ", input_type='int')
    if ano is not None:
        filtros['year'] = ano
    
    print("------------------------------------------------------------------------------------------------------------------------||||")

    combustivel = get_valid_input("Digite o tipo de combustível? (ex: Gasolina, Etanol, Flex...) ", 
                                input_type='option',
                                valid_options=COMBUSTIVEIS_VALIDOS)
    if combustivel:
        filtros['fuel'] = combustivel

    print("------------------------------------------------------------------------------------------------------------------------||||")

    cor = get_valid_input("Digite a cor? (ex: Preto, Branco, Vermelho...) ", 
                         input_type='option',
                         valid_options=CORES_VALIDAS)
    if cor:
        filtros['color'] = cor

    print("------------------------------------------------------------------------------------------------------------------------||||")

    quilometragem = get_valid_input("Digite a quilometragem máxima? (ex: 100000, 150000, 200000, 250000, 300000. 900000) ", input_type='int')
    if quilometragem is not None:
        filtros['mileage_max'] = quilometragem

    print("------------------------------------------------------------------------------------------------------------------------||||")
    
    transmissao = get_valid_input("Digite o tipo de transmissão? (ex: Manual, Automático) ", 
                                input_type='option',
                                valid_options=TRANSMISSOES_VALIDAS)
    if transmissao:
        filtros['transmission'] = transmissao

    print("------------------------------------------------------------------------------------------------------------------------||||")
    
    portas = get_valid_input("Digite o número de portas? (2 ou 4) ", 
                           input_type='option', 
                           valid_options=['2', '4'])
    if portas:
        filtros['doors'] = int(portas)

    print("------------------------------------------------------------------------------------------------------------------------||||")

    preco = get_valid_input("Digite o valor máximo? (ex: 10000, 20000, 30000, 40000, 90000) ", input_type='float')
    if preco is not None:
        filtros['price_max'] = preco
        
    print("------------------------------------------------------------------------------------------------------------------------||||")
    if not filtros:
        print("Nenhum filtro fornecido. Buscando todos os veículos disponíveis...")
        filtros = None
    elif len(filtros) == 1:
        print(f"Buscando veículos com o filtro: {list(filtros.keys())[0]} = {list(filtros.values())[0]}")
    elif len(filtros) > 1:
        print(f"Buscando veículos com os filtros: {', '.join([f'{k} = {v}' for k, v in filtros.items()])}")
    else:
        print("Nenhum filtro fornecido. Buscando todos os veículos disponíveis...")
        filtros = None  
    print("------------------------------------------------------------------------------------------------------------------------||||")         

    print("\nBuscando veículos com os filtros fornecidos...")
    print("Aguarde, isso pode levar alguns segundos...")
    print("Iniciando a busca no banco de dados...")
    print("------------------------------------------------------------------------------------------------------------------------||||")
    resultados = send_message(filtros)
    print("Busca concluída!")
    print("------------------------------------------------------------------------------------------------------------------------||||")
    if resultados:
        print(f"\nVeículos encontrados ({len(resultados)}):\n")
        print("-" * 70)
        print("------------------------------------------------------------------------------------------------------------------------||||")
        print("Marca | Modelo | Ano | Preço | Combustível | Cor | Quilometragem")
        print("-" * 70) 
        for v in resultados:
            v['price'] = float(v['price'])
            v['mileage'] = int(v['mileage'])
            v['year'] = int(v['year'])            
            print(f"{v['brand']} {v['model']} - {v['year']} | R$ {v['price']:.2f} | {v['fuel']} | {v['color']} | {v['mileage']} km")
    else:        
        print("Nenhum veículo encontrado.")
        print("Tente ajustar os filtros ou busque novamente sem filtros.")
        print("------------------------------------------------------------------------------------------------------------------------||||")
        print("\nObrigado por usar nosso assistente de busca automotiva!")

        print("============================================================================================================================")

if __name__ == "__main__":    
    main()