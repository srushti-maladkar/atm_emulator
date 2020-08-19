# Welcome message
# Enter the card
# Language selection - English, Hindi, Marathi
# Enter Pin
# Verify Pin
# Show Menu - Withdraw, Chnage Pin, Check balance
#   Withdraw - Saving, Current
#       Saving - Enter Amount
#           Processing Prompt and collect cash message
# Print Receipt option - Y/N
# Remove Card prompt
# Exit transaction
import time
from users import users

print("Welcome to HDFC BANK\n\n")
ins_card = input("Please press 'I' to insert your card for service: ")
if ins_card == 'I' or ins_card == 'i':
    lang_list = ["English", "Hindi", "Marathi"]
    for lang_idx, value in enumerate(lang_list, start=1):
        print(f'{lang_idx}. {value}')
    lang = input("Please select language from above options: ")

    if lang == '2' or lang == '3':
        print(
            f'Sorry for inconvinience.{lang} is currently not available. Please select 1 ')

    attempts = 1

    while attempts <= 3:
        user_pin = int(input("Please enter your card pin(XXXX): "))
        if user_pin in users:
            first_name = users[user_pin]["first_name"]
            last_name = users[user_pin]["last_name"]
            account_no = users[user_pin]["account_no"]
            balance = users[user_pin]["balance"]
            currency = users[user_pin]["currency"]
            print(
                f"Hello {first_name}. Please select from menu to perform required operation")

            options = ['Withdraw', 'Change Pin', 'Check balance']

            for option, value in enumerate(options, start=1):
                print(f'{option}. {value}')

            opt_sel = int(input("Choose Option: "))

            while True:
                if opt_sel in [1, 2, 3]:
                    if opt_sel == 3:
                        print("Please wait....")
                        time.sleep(1.0)
                        print(f'Your account balance is {currency}{balance}')
                    elif opt_sel == 1:
                        print('Please enter amount to withdraw')
                    elif opt_sel == 2:
                        print("Please provide 6 digit OTP send on your mobile number")
                        otp = int(input("Enter OTP: "))
                        print("Please set new pin")
                        new_pin = int(input("Enter new pin: "))
                        if len.new_pin = 4:
                            user_pin = new_pin
                            print("Pin is changed")
                            print(user_pin)
                        else:
                            print("Invalid input provided")
                pass

            break
        else:
            attempts += 1
            print(f'Invalid pin. You have {4 - attempts} attempts remaining.')
else:
    print("Card not inserted\nPlease insert card to proceed further.\nThank You!!")
