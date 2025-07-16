import pytest
from app.models.vehicle import Vehicle, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

DB_URL = "sqlite:///test_vehicles.db"

@pytest.fixture(scope="module")
def session():
    if os.path.exists("test_vehicles.db"):
        os.remove("test_vehicles.db")
    engine = create_engine(DB_URL)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sess = Session()

    # Cria dados fictícios
    sess.add(Vehicle(
        brand="Fiat", model="Uno", year=2010,
        engine="1.0", fuel="Flex", color="Prata",
        mileage=100000, doors=4, transmission="Manual",
        price=20000
    ))
    sess.commit()
    yield sess
    sess.close()
    os.remove("test_vehicles.db")

def test_vehicle_insertion(session):
    result = session.query(Vehicle).filter_by(brand="Fiat").first()
    assert result is not None
    assert result.model == "Uno"
    assert result.year == 2010
    assert result.price == 20000    
    assert result.color == "Prata"
    assert result.mileage == 100000
    assert result.doors == 4
    assert result.transmission == "Manual"
    assert result.engine == "1.0"
    assert result.fuel == "Flex"
    print("Teste de inserção de veículo concluído com sucesso.")
    print("Todos os testes passaram com sucesso.")