from engine.engines import WilloughbyEngine, CapuletEngine, SternmanEngine
from battery.batteries import SpindlerBattery, NubbinBattery
from tire.tires import OctoprimeTire, CarriganTire
from car import Car

class CarFactory(Car):
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage): 
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = OctoprimeTire([0,0,0,0])
        return Car(engine,battery,tires)
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage): 
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTire([0,0,0.5,0])
        return Car(engine,battery,tires)
    def create_palindrome(current_date, last_service_date, warning_light_on):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTire([0,0,0.5,0])
        return Car(engine,battery,tires)
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = CarriganTire([0,0,0.5,0])
        return Car(engine,battery,tires)
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine  = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = OctoprimeTire([0,0,0.5,0])
        return Car(engine,battery,tires)
