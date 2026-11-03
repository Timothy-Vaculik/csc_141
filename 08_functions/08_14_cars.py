# Timothy Vaculik
# cars with functions
# I think is is difficulty of 6/10

def make_car(manufacturer, model, **car_info):
    """Build a dictionary containing everything we know about a car."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

my_chevy = make_car('chevrolet', 'camaro', color='blue', tow_package=True)
print(my_chevy)

my_tesla = make_car('tesla', 'model s', color='red', autopilot=True)
print(my_tesla)