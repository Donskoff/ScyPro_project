from masks import get_mask_card_number, get_mask_account

def mask_account_card(bank_details: str) -> str:
    if "Счёт" in bank_details:
        bank_details_list = bank_details.split()
        bank_details_list[-1] = get_mask_account(bank_details_list[-1])
        new_bank_details = " ".join(bank_details_list)
        return new_bank_details
    else:
        print("Это номер карты")
    # return

bank_details_data = input("Введите данные банковской карты или счёта ... ")

output_data = mask_account_card(bank_details_data)
print(output_data)