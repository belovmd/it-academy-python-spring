def student_languages():
    """Task from lecture about languages of students

    Print number of languages known by all students
    Print list of languages known by all students
    Print number of languages known by at least one student
    Print list of languages known by at least one student
    """

    nmb_of_students = int(input('Enter number of students: '))

    stud_languages, lang_set = [], set()

    for stud_nmb in range(nmb_of_students):
        lang_nmb_of_student = int(input(
            f'Enter nmb of lang of {stud_nmb + 1} stud: '))

        stud_languages.append([])

        for lang_nmb in range(lang_nmb_of_student):
            lang = input(f'Enter lang {lang_nmb + 1} of {stud_nmb + 1} stud: ')
            stud_languages[stud_nmb].append(lang)
            lang_set.add(lang)

    all_languages = lang_set

    for languages in stud_languages:
        lang_set = lang_set & set(languages)

    print('Nmb of lang known by all students:', len(lang_set))
    print('Lang known by all students:', *lang_set)
    print('Nmb of lang known by at least one student:', len(all_languages))
    print('Lang known by at least one student:', *all_languages)


if __name__ == '__main__':
    student_languages()
