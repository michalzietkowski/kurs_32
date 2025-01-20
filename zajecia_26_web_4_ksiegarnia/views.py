from file_handler import file_handler


def get_data_for_main_view():
    return file_handler.data

def get_history_for_history_view(from_value, to_value):
    if from_value and to_value:
        return file_handler.history[int(from_value):int(to_value)]
    return file_handler.history

def save_data_for_book_purchase(form_input):
    file_handler.data["ksiegozbior"].append(
        {
                "tytul": form_input.get("tytul"),
                "autor": form_input.get("autor"),
                "rok_wydania": 1990,
                "ilosc_dostepnych_ksiazek": form_input.get("ilosc_ksiazek"),
                "ilosc_ksiazek": form_input.get("ilosc_ksiazek"),
                "cena_wypozyczenia": 15,
        }
    )
    file_handler.save_data_to_data_file(
        balance=file_handler.data["saldo"],
        book_collection=file_handler.data["ksiegozbior"]
    )

def save_data_for_balance_change(form_input):
    file_handler.data["saldo"] += float(form_input.get("kwota"))
    file_handler.save_data_to_data_file(
        balance=file_handler.data["saldo"],
        book_collection=file_handler.data["ksiegozbior"]
    )