from datetime import datetime
from engine import WilloughbyEngine, CapuletEngine, SternmanEngine
from battery import SpindlerBattery, NubbinBattery
from serviceable import Serviceable


class Car(Serviceable):
    def __init__(engine,battery,self):
        self.engine= engine
        self.battery= battery

    def needs_service(self):
        if self.battery.needs_service() or self.engine.needs_service():
            True
        else:
            False

class CarFactory(Car):
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage): 
        Car(CapuletEngine(current_mileage, last_service_mileage),SpindlerBattery(last_service_date, current_date))
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage): 
        Car(WilloughbyEngine(current_mileage, last_service_mileage),SpindlerBattery(last_service_date, current_date))
    def create_palindrome(current_date, last_service_date, warning_light_on):
        Car(SternmanEngine(warning_light_on),SpindlerBattery(last_service_date, current_date))
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
         Car(WilloughbyEngine(current_mileage, last_service_mileage),NubbinBattery(last_service_date, current_date))
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
         Car(CapuletEngine(current_mileage, last_service_mileage),NubbinBattery(last_service_date, current_date))
