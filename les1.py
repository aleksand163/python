user_input = input("Введите время в секундах >>> ")

user_seconds = int(user_input)

hours = user_seconds // 3600
minutes = (user_seconds % 3600) // 60
seconds = (user_seconds % 3600) % 60

# hours, minutes, seconds = user_seconds // 3600, (user_seconds % 3600) // 60, (user_seconds % 3600) % 60

print(f"{hours:>02}:{minutes:>02}:{seconds:>02}")