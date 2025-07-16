from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from app.models.vehicle import Vehicle, Base
from faker import Faker
import random

DB_URL = "sqlite:///vehicles.db"

def populate_database(n=100):    
    fake = Faker()    
    Faker._DEFAULT_LOCALE = 'pt_BR'
    Faker.seed(0)
    random.seed(0)    
    engine = create_engine(DB_URL)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()


    print("Incerindo dados no banco de dados....")

    print(f"Fazendo conexão ao banco de dados {DB_URL}...")
    if not engine:
        print("Erro ao conectar ao banco de dados. Verifique se voce possui a URL do banco de dados.")
        return
    
    print("conectado com sucesso ao banco de dados!")   

    print(f"Preparando para adicionar {n} veículos...") 

    print("Verificando, se a tabela existe no banco de dados...")

    if not engine.dialect.has_table(engine, 'Veiculos'):        
        print("Tabela Veiculos não encontrada. Criando tabela...")        
        Base.metadata.create_all(engine)
        print("Tabela Veiculos criada com sucesso!")
        print("Tabela Veiculos criada com sucesso. Prosseguindo com a população...")
    else:
        print("Tabela Veiculos já existe. Prosseguindo com a população...")
        print("Tabela Veiculos encontrada. Prosseguindo com a população...")
        print("Tabela Veiculos já existe. Limpando dados antigos...")
        print("Limpando dados antigos da tabela Veiculos...")

    
    session.query(Vehicle).delete() 
    print(f"Populando o banco de dados com {n} veículos...")
    Faker._DEFAULT_LOCALE = 'pt_BR'
    fake = Faker('pt_BR')
    Faker.seed(0)
    random.seed(0)   

    from app.models.veiculos import Veiculos as Vehicle 

    brands = [ 'Honda', 'Toyota', 'Nissan', 'Jeep', 'Renault', 'Kia', 'Chery', 'Volkswagen', 'Fiat', 'Ford', 'Chevrolet', 'Hyundai', 'Peugeot', 'Citroën', 'Mitsubishi', 'Suzuki', 'Mazda', 'Subaru', 'Volvo', 'Audi', 'BMW', 'Mercedes-Benz']
    models = ['T-Cross', 'Tracker', 'Creta', 'HR-V', 'Kicks', 'Renegade', 'Duster', 'Compass', 'Sportage', 'Tiggo 5X', 'Corolla', 'Civic', 'Onix', 'HB20', 'Argo', 'Ka', 'Fiesta', 'Palio', 'Uno']    
    fuels = ['Gasolina', 'Etanol', 'Flex', 'Diesel', 'Elétrico', 'Híbrido', 'GNV', 'Álcool', 'Hidrogênio', 'Biodiesel', 'Álcool Etílico']
    transmissions = ['Manual', 'Automático', 'Semi-Automático']    
    colors = ['Preto', 'Prata', 'Branco', 'Cinza', 'Azul', 'Vermelho', 'Verde', 'Amarelo', 'Laranja', 'Roxo', 'Marrom', 'Bege', 'Dourado', 'Ciano', 'Magenta']
    
       

    for _ in range(n):
        vehicle = Vehicle(
            brand=random.choice(brands),
            model=random.choice(models),
            year=random.randint(2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040, 2041, 2042, 2043, 2044, 2045, 2046, 2047, 2048, 2049, 2050),
            engine=f"{random.uniform(1.0, 3.0, 4.0, 5.0, 6.0, 7.0,  8.0):.1f}",
            fuel=random.choice(fuels + ['Gasolina', 'Etanol', 'Flex', 'Diesel', 'Elétrico', 'Híbrido', 'GNV', 'Álcool', 'Hidrogênio', 'Biodiesel', 'Álcool Etílico']),
            color=random.choice(colors + ['Preto', 'Prata', 'Branco', 'Cinza', 'Azul', 'Vermelho', 'Verde', 'Amarelo', 'Laranja', 'Roxo', 'Marrom', 'Bege', 'Dourado', 'Ciano', 'Magenta']),
            mileage=round(random.uniform(10000, 150000), 2),
            doors=random.choice([2, 4]),
            transmission=random.choice(transmissions + ['Manual', 'Automático', 'Semi-Automático']),
            price=round(random.uniform(15000, 90000, 100000, 200000, 300000, 400000, 500000, 150000), 2)            
        )
        session.add(vehicle)

    session.commit()
    session.close()
    print(f"{n} veículos adicionados com sucesso ao banco de dados.")

if __name__ == "__main__":
    populate_database()
