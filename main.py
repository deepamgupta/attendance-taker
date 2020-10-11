def get_present_students_from_file(input_file_name):
    f = open(input_file_name, 'r')
    present_students = f.readlines()
    f.close()

    for i in range(len(present_students)):
        present_students[i] = present_students[i].strip().replace('\t', ' ')

    return present_students


def eveluate_attendance(present_students_list):
    attendance = {
        "PARIJAT SINGH KUBREY": " ",
        "HARSH VARDHAN": " ",
        "SUSHIL SINGH": " ",
        "VIVEK KULASTE": " ",
        "ABHINAV PANDEY": " ",
        "ADYA TRISAL": " ",
        "AISHWARYA AGRAWAL": " ",
        "AKSHAT KARODIYA": " ",
        "ALINOOR MULTANI": " ",
        "AMAN NAGLE": " ",
        "ANURAG GRIYAM": " ",
        "ASHUTOSH SINGH": " ",
        "ASHUTOSH VERMA": " ",
        "ASHVITA PATIDAR": " ",
        "AYUSH KOTWALLA": " ",
        "DEEP KOTHARI": " ",
        "DEEPAM GUPTA": " ",
        "DEV KUMAR": " ",
        "DIGVIJAY VERMA": " ",
        "DIVYA LAKHOTIA": " ",
        "EESHWARI BHATORE": " ",
        "GURUCHARAN PURTE": " ",
        "HARISH BHABHAR": " ",
        "HARISH PARMAR": " ",
        "HARSHITA BHOMADIYA": " ",
        "ISHITA JAIN": " ",
        "JASMAN JATAV": " ",
        "JATIN GUPTA": " ",
        "KRISHNA LOHARE": " ",
        "LOKENDRA MANDLOI": " ",
        "MADHUSUDAN YADAV": " ",
        "MANISH JHAMELE": " ",
        "NEHA DAWAR": " ",
        "NILAY OSTWAL": " ",
        "NITI MANGWANI": " ",
        "PARTH ARORA": " ",
        "PRADYUMNA UPADHYAY": " ",
        "PRATIBHA CHOUHAN": " ",
        "PRATIK MEHTA": " ",
        "PRIYANSH TIWARI": " ",
        "RAHUL WASKALE": " ",
        "RAJAT KARAHE": " ",
        "RAKSHA ASTARE": " ",
        "RAMAN DHAKAR": " ",
        "RASHI MALVIYA": " ",
        "RISHAV THAKUR": " ",
        "RITHIK PANDITA": " ",
        "RUDRANSH CHOUDHARY": " ",
        "SAGAR CHOUBEY": " ",
        "SAMYAK JAIN": " ",
        "SARTHAK JOSHI": " ",
        "SARTHAK NEEMA": " ",
        "SATYAM PATEL": " ",
        "SHEETAL KOTHE": " ",
        "SIDDHANT JAIN": " ",
        "SONU GUPTA": " ",
        "SUMIT KR SINGH": " ",
        "TASHI AGRAWAL": " ",
        "UNNATI DIXIT": " ",
        "VANSHIKA SUNDRANI": " ",
        "VICKY NIGAM": " ",
        "YASH SONI": " ",
        "YOGESH SINGH": " ",
        "KISHAN JOSHI": " ",
        "JAINISHA KHOWAL": " ",
        "AKANKSHA DUBEY": " ",
        "ASHUTOSH BARDE": " ",
        "AYUSH KARMA": " ",
        "BHOOMIKA PANDEY": " ",
        "DISHA KHARE": " ",
        "KAMINI SINGH CHAUHAN ": " ",
        "PRASHANT ARJARIYA": " ",
        "PRATEEK ONKAR": " ",
        "RAJNI YADAV": " ",
        "RAVINDRA KUMAR KUSHWAHA": " ",
        "SAKSHI CHAURASIYA": " ",
        "VIPUL PORWAL": " ",
    }

    for student in present_students_list:
        if student in attendance:
            attendance[student] = 'P'

    return list(attendance.values())


def print_attendance_to_file(output_file_name, attendance_list):
    f = open(output_file_name, 'w')
    f.write('\n'.join(attendance_list))
    f.close()


if __name__ == '__main__':
    present_students_list = get_present_students_from_file('input.txt')
    attendance_list = eveluate_attendance(present_students_list)
    print_attendance_to_file('output.txt', attendance_list)


# present_num = int(input("Enter students present_num : "))
# present_student_list = []
#
# for i in range(present_num):
#     student = input()
#     present_student_list.append(student.replace('\t', ' '))
#
# for student in present_student_list:
#     if student in attendance:
#         attendance[student] = 'P'
#
# for val in attendance.values():
#     print(val)
