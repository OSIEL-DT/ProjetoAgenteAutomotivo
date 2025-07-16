from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.vehicle import Vehicle, Base
from faker import Faker
import random


DB_URL = "sqlite:///vehicles.db"

def populate_database(n=100):
    fake = Faker()
    engine = create_engine(DB_URL)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    brands = ['Ford', 'Fiat', 'Chevrolet', 'Volkswagen', 'Hyundai']
    models = ['Uno', 'Ka', 'Gol', 'Onix', 'HB20', 'Civic', 'Corolla']
    fuels = ['Gasolina', 'Etanol', 'Flex', 'Diesel']
    transmissions = ['Manual', 'Automático']
    colors = ['Preto', 'Prata', 'Branco', 'Cinza', 'Azul']

    for _ in range(n):
        vehicle = Vehicle(
            brand=random.choice(brands),
            model=random.choice(models),
            year=random.randint(2005, 2023),
            engine=f"{random.uniform(1.0, 3.0):.1f}",
            fuel=random.choice(fuels),
            color=random.choice(colors),
            mileage=round(random.uniform(10000, 150000), 2),
            doors=random.choice([2, 4]),            
            transmission=random.choice(transmissions),
            price=round(random.uniform(15000, 90000), 2)

        )
        session.add(vehicle)

    session.commit()
    session.close()
    print(f"Populando o banco de dados com {n} veículos...")
    print("Banco de dados conectado com sucesso!")
    print(f"{n} veículos adicionados com sucesso ao banco de dados.")


if __name__ == "__main__":
    populate_database()
