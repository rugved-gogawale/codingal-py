money=int(input("Enter the amount of money you want to withdraw: "))
note1=money // 50
note2=(money % 50) // 20
note3=((money % 50) % 20) // 10
note4=(((money % 50) % 20) % 10) // 5
print(note1, "notes of 50")
print(note2, "notes of 20")
print(note3, "notes of 10")
print(note4, "notes of 5")
