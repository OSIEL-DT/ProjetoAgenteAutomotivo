from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Vehicle(Base):
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True)
    brand = Column(String)
    model = Column(String)
    year = Column(Integer)
    engine = Column(String)
    fuel = Column(String)
    color = Column(String)
    mileage = Column(Float)
    doors = Column(Integer)
    transmission = Column(String)
    price = Column(Float)

    def to_dict(self):
        return {
            "brand": self.brand,
            "model": self.model,
            "year": self.year,
            "engine": self.engine,
            "fuel": self.fuel,
            "color": self.color,
            "mileage": self.mileage,
            "doors": self.doors,
            "transmission": self.transmission,
            "price": self.price
        }    

    def __repr__(self):
        return f"<Vehicle(brand={self.brand}, model={self.model}, year={self.year}, price={self.price}, mileage={self.mileage}, fuel={self.fuel}, transmission={self.transmission}, color={self.color}, doors={self.doors})>"
    def __init__(self, brand, model, year, engine, fuel, color, mileage, doors, transmission, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine = engine
        self.fuel = fuel
        self.color = color
        self.mileage = mileage
        self.doors = doors
        self.transmission = transmission
        self.price = price  
        return self
    
