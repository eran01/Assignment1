subj1_all_students={'Sub': 'History', 'Tony':[80,85], 'Paulie': [90,75], 'Silvio': [65, 95], 'Christopher': [45,52], 'Ralph': [99,87], 'Livia': [100,100]}
subj2_all_students={'Sub': 'Math', 'Tony':[60,95], 'Paulie': [86,71], 'Silvio': [100, 66], 'Christopher': [32,78], 'Corrado':[76,99],'Livia': [90,90]}

def compare_subjects_within_student(subj1_all_students, subj2_all_students):
    for i in subj1_all_students.keys():
        if i in subj2_all_students.keys() and type(subj1_all_students[i])==list and type(subj2_all_students[i])==list:
            X=0
            X=max(max(subj1_all_students[i]), max(subj2_all_students[i]))
            if X in subj1_all_students[i]:
                print(i+" "+  subj1_all_students['Sub'])
            if X in subj2_all_students[i]:
                print(i+" "+  subj2_all_students['Sub'])
                
compare_subjects_within_student(subj1_all_students, subj2_all_students)
