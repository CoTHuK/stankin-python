def convert(ma):
    if not isinstance(ma, (int, float)) or isinstance(ma, bool):
        raise TypeError("Ток должен быть числом (int или float).")

    PVmin = 0
    PVmax = 75
    
    if ma == 0:
        return "Датчик отключен"
    elif 0 < ma < 3.9:
        return "Датчик неисправен"
    elif ma > 20.1:
        return "Датчик неисправен"
    elif 4 <= ma <= 20:
        PV = (ma - 4) * (PVmax - PVmin) / (20 - 4) + PVmin
        return f"Температура: {PV:.2f} °C"
    else:
        return "Неизвестный сигнал (проверьте датчик)"


if __name__ == "__main__":
    bob = [0, 2.5, 4, 12, 20, 21]
    for i in bob:
        try:
            print(f"Ток: {i} мА -> {convert(i)}")
        except TypeError as e:
            print(e)

    try:
        print(convert("12мА"))
    except TypeError as e:
        print(f"Поймали ошибку: {e}")