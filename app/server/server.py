from app.models.vehicle import Vehicle, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.protocol.mcp import start_server

DB_URL = "sqlite:///vehicles.db"
engine = create_engine(DB_URL)
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)

def filter_vehicles(filters):
    session = Session()
    query = session.query(Vehicle)

    
    if 'brand' in filters:
        query = query.filter(Vehicle.brand.ilike(f"%{filters['brand']}%"))
    if 'year' in filters:
        query = query.filter(Vehicle.year == filters['year'])
    if 'fuel' in filters:
        query = query.filter(Vehicle.fuel.ilike(f"%{filters['fuel']}%"))
    if 'price_max' in filters:
        query = query.filter(Vehicle.price <= filters['price_max'])
    if 'price_min' in filters:
        query = query.filter(Vehicle.price >= filters['price_min'])
    if 'mileage_max' in filters:
        query = query.filter(Vehicle.mileage <= filters['mileage_max'])
   

    results = [v.to_dict() for v in query.limit(20).all()]    
    session.close()
    return results

if __name__ == "__main__":
    start_server(filter_vehicles)
