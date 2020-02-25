def student_languages():
    """Task from lecture about languages of students

    Print dict with student index as a key and list of all languages
    known by this student as value
    Print set of languages known by at least one student
    Print set of languages known by all students
    """

    nmb_of_student = int(input('Enter numbers of students: '))
    dict_student_languages = {}

    for student_nmb in range(1, nmb_of_student + 1):
        lang_nmb_of_student = int(input(f'Enter numbers of languages of '
                                        f'{student_nmb} student: '))
        dict_student_languages[student_nmb] = []

        for lang_nmb in range(1, lang_nmb_of_student + 1):
            lang = input(f'Enter language {lang_nmb} of '
                         f'{student_nmb} student: ')
            dict_student_languages[student_nmb].append(lang)

    print(f'All languages of students: {dict_student_languages}'
          if len(dict_student_languages) else f'All languages: None')

    lang_set = set()
    for key, value in dict_student_languages.items():
        lang_set = lang_set | set(value)
    print(f'Languages known by at least one student: {lang_set}'
          if len(lang_set) else f'No languages known by at least one student')

    for key, value in dict_student_languages.items():
        lang_set = lang_set & set(value)
    print(f'Languages known by all students: {lang_set}'
          if len(lang_set) else 'No languages known by all students')


if __name__ == '__main__':
    student_languages()
