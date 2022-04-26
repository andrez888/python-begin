# Za pomocą from ... import możemy importować zarówno cały moduł jak i pojedyncze funckje/zmienne
print(__name__)
from przyklad import dwa
from przyklad.cztery  import calculate_student_final_grades
from przyklad.trzy  import check_promotion
from przyklad.jeden  import is_student_in_school
# from przyklad import *

print("Witaj w elektronicznym dzienniku!")

student_name = input("Podaj imię ucznia żeby dowiedzieć się czy zdał/zdała do następnej klasy: ")

if not is_student_in_school(student_name):
    print(f"Niestety {student_name} nie ma na liście...")
else:
    final_grades = calculate_student_final_grades(student_name)
    promotion_result = check_promotion(final_grades)

    if promotion_result == dwa.PASSED:
        print(f"Gratuluję! {student_name} zdał/zdała do następnej klasy :)")
    elif promotion_result == dwa.FAILED:
        print(f"Niestety {student_name} nie zdał/nie zdała")
    else:
        print("Coś poszło nie tak... Zgłoś to obsłudze systemu")