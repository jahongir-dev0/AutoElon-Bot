from aiogram.dispatcher.filters.state import StatesGroup, State


class NewPost(StatesGroup):
    # Post yaratish uchun zarur bo'lgan barcha state'lar
    Avto = State()       # Avtomobil nomi
    Yil = State()        # Yil
    Probeg = State()     # Probeg
    Kraska = State()     # Kraska
    Benzin = State()     # Benzin tur
    Narx = State()       # Narx
    Tel = State()        # Telefon
    Manzil = State()     # Manzil
    AvtoRasm = State()   # Avtomobil rasm
    Confirm = State()    # Tasdiqlash