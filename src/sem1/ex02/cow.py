def convert(temp):
    if not isinstance(temp, (int, float)) or isinstance(temp, bool):
        raise TypeError("Температура должна быть числом (int или float).")

    if temp < 34.9:
        return "Требуется внимание (датчик свалился или корова плохо себя чувствует)"
    elif 34.9 <= temp < 37.4:
        return "Корова замерзла, требуется обогрев"
    elif 37.5 <= temp <= 39.0:
        return "Нормальная температура тела"
    elif 39.1 <= temp <= 39.5:
        return "Корова перегрелась, требуется охлаждение"
    elif temp >= 39.6:
        return "Срочно вызывайте ветеринара, коровка заболела"
    else:
        return "Температура в средней области, стоит понаблюдать за коровкой"

if __name__ == "__main__":
    bob = [34.5, 36.0, 38.0, 39.2, 39.8]
    for t in bob:
        try:
            print(f"Температура: {t} °C -> {convert(t)}")
        except TypeError as e:
            print(e)

    try:
        print(convert("горячая"))
    except TypeError as e:
        print(f"Поймали ошибку: {e}")