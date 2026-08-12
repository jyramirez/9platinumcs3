# CODE

birth_year = int(input("Enter your birth year: "))
zodiac = ["Rat (鼠 / Shǔ)", "Ox (牛 / Niú)", "Tiger (虎 / Hǔ)", "Rabbit (兔 / Tù)", "Dragon (龙 / Lóng)", "Snake (蛇 / Shé)", "Horse (马 / Mǎ)", "Goat (羊 / Yáng)", "Monkey (猴 / Hóu)", "Rooster (鸡 / Jī)", "Dog (狗 / Gǒu)", "Pig (猪 / Zhū)"]


if birth_year >= 1900:
    zodiac_num = (birth_year-1900)%12
    print(f"Your Chinese Zodiac Sign is: {zodiac[zodiac_num]}")

else:
    print("Invalid Year, it should not be earlier than 1900")

--

# DOCUMENTATION

![code](images/image-1.png)
![code](images/image.png)
