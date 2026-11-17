
from create_table import create_table
from harajatlar import add_harajat, get_harajatlar, jami_harajat


def main():
    create_table()

    while True:
        print("\n===== KUNLIK XARAJATLAR =====")
        print("1. Xarajat qo'shish")
        print("2. Xarajatlarni ko'rish")
        print("3. Jami xarajat")
        print("4. Chiqish")

        tanlov = input("Tanlang: ")

        if tanlov == "1":
            nom = input("Xarajat nomi: ")
            try:
                summa = float(input("Summasi: "))
            except ValueError:
                print("Summa raqam bo'lishi kerak!")
                continue
            sana = input("Sana (YYYY-MM-DD): ")
            kategoriya = input("Kategoriya: ")

            add_harajat(nom, summa, sana, kategoriya)
            print("Saqlandi!")

        elif tanlov == "2":
            data = get_harajatlar()

            if data:
                for row in data:
                    print(row)
            else:
                print("Hozircha xarajatlar yo'q.")

        elif tanlov == "3":
            print("Jami xarajat:", jami_harajat(), "so'm")

        elif tanlov == "4":
            print("Dastur tugadi!")
            break

        else:
            print("Noto'g'ri tanlov!")


if __name__ == "__main__":
    main()
