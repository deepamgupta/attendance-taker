import os


def get_present_students_from_file(input_file_path):
    with open(input_file_path, 'r') as file:
        present_students_string = file.read().casefold()

    return present_students_string


def evaluate_attendance(present_students_string):
    attendance = {
        "parijat singh kubrey": " ",
        "harsh vardhan": " ",
        "sushil singh": " ",
        "vivek kulaste": " ",
        "abhinav pandey": " ",
        "adya trisal": " ",
        "aishwarya agrawal": " ",
        "akshat karodiya": " ",
        "alinoor multani": " ",
        "aman nagle": " ",
        "anurag griyam": " ",
        "ashutosh singh": " ",
        "ashutosh verma": " ",
        "ashvita patidar": " ",
        "ayush kotwalla": " ",
        "deep kothari": " ",
        "deepam gupta": " ",
        "dev kumar": " ",
        "digvijay verma": " ",
        "divya lakhotia": " ",
        "eeshwari bhatore": " ",
        "gurucharan purte": " ",
        "harish bhabhar": " ",
        "harish parmar": " ",
        "harshita bhomadiya": " ",
        "ishita jain": " ",
        "jasman jatav": " ",
        "jatin gupta": " ",
        "krishna lohare": " ",
        "lokendra mandloi": " ",
        "madhusudan yadav": " ",
        "manish jhamele": " ",
        "neha dawar": " ",
        "nilay ostwal": " ",
        "niti mangwani": " ",
        "parth arora": " ",
        "pradyumna upadhyay": " ",
        "pratibha chouhan": " ",
        "pratik mehta": " ",
        "priyansh tiwari": " ",
        "rahul waskale": " ",
        "rajat karahe": " ",
        "raksha astare": " ",
        "raman dhakar": " ",
        "rashi malviya": " ",
        "rishav thakur": " ",
        "rithik pandita": " ",
        "rudransh choudhary": " ",
        "sagar choubey": " ",
        "samyak jain": " ",
        "sarthak joshi": " ",
        "sarthak neema": " ",
        "satyam patel": " ",
        "sheetal kothe": " ",
        "siddhant jain": " ",
        "sonu gupta": " ",
        "sumit kr singh": " ",
        "tashi agrawal": " ",
        "unnati dixit": " ",
        "vanshika sundrani": " ",
        "vicky nigam": " ",
        "yash soni": " ",
        "yogesh singh": " ",
        "kishan joshi": " ",
        "jainisha khowal": " ",
        "akanksha dubey": " ",
        "ashutosh barde": " ",
        "ayush karma": " ",
        "bhoomika pandey": " ",
        "disha khare": " ",
        "kamini singh chauhan ": " ",
        "prashant arjariya": " ",
        "prateek onkar": " ",
        "rajni yadav": " ",
        "ravindra kumar kushwaha": " ",
        "sakshi chaurasiya": " ",
        "vipul porwal": " ",
    }

    for student in attendance.keys():
        if present_students_string.find(student) != -1:
            attendance[student] = "P"

    return list(attendance.values())


def print_attendance_to_file(output_file_path, attendance_list):
    f = open(output_file_path, 'w')
    f.write('\n'.join(attendance_list))
    f.close()


if __name__ == '__main__':
    cur_dir = os.getcwd()
    input_file_path = os.path.join(cur_dir, "input.csv")
    output_file_path = os.path.join(cur_dir, "output.csv")

    present_students_string = get_present_students_from_file(input_file_path)
    attendance_list = evaluate_attendance(present_students_string)
    print_attendance_to_file(output_file_path, attendance_list)
