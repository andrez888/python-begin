from przyklad import dwa

hujowa_ocena = 1


def check_promotion(subjects_final_grades):
    for subject, grade in subjects_final_grades.items():
        if grade == hujowa_ocena:
            return dwa.FAILED

    return dwa.PASSED
