from app.models.vehicle import Vehicle

def test_vehicle_creation():
    car = vehicle(
        brand="Ford",
        model="Focus",
        year=2018,
        engine="2.0L",
        fuel_type="Gasoline",
        color="Red",
        mileage=50000,
        doors=4,
        transmission="Automatic",
        price=75000.00
    )
    assert car.brand == "Ford"
    assert car.price > 0
