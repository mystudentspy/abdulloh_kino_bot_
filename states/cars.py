from aiogram.fsm.state import State, StatesGroup

class CarState(StatesGroup):
    car_name = State()
    car_color = State()
    car_model = State()
    car_year = State()
    car_price = State()
    car_mileage = State()
    car_photo = State()
    car_description = State()