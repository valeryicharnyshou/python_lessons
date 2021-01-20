def user_data(name, surname, year_of_birth, city, e_mail, tel):
    print(f"Name - {name}; Surname - {surname}; Year of birth - {year_of_birth}; City - {city}; E-Mail - {e_mail}; "
          f"Telephone - {tel}")


user_name = input("Введите Ваше имя: ")
user_surname = input("Введите Вашу фамилию: ")
year = input("Введите Ваш год рождения: ")
town = input("Введите город проживания: ")
mail = input("Введите адрес электронной почты: ")
telephone = input("Введите номер телефона: ")
user_data(user_name, user_surname, year, town, mail, telephone)
