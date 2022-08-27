from tire.tire import Tire

class CarriganTire(Tire):

  def __init__(self, wear):
    self.wear=wear

  def needs_service(self):
    for tire in self.wear:
      if tire >= 0.9:
        return True 
    return False

class OctoprimeTire(Tire):
    def __init__(self, wear):
      self.wear=wear

    def needs_service(self):
      sum=0
      for tire in self.wear:
        sum += tire
      if sum >=3:
        return True
      else:
        return False