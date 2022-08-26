from operator import truediv
from datetime import datetime

class BatteryInterface():
  def needs_service():
    pass

class SpindlerBattery(BatteryInterface):
  def __init__(self, last_service_date, current_date):
    self.last_service_date = last_service_date
    self.current_date = current_date

  def needs_service(self):
     service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
     if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
      return True
     else:
      return False

class NubbinBattery(BatteryInterface):
  def __init__(self, last_service_date, current_date):
    self.last_service_date = last_service_date
    self.current_date = current_date

  def needs_service(self):
    service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
    if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
      return True
    else:
      return False
