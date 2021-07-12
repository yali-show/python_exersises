sampleDict = {
   "class":{
      "student":{
         "name":"Mike",
         "marks":{
            "physics":70,
            "history":80
         }
      }
   }
}


def student_average_score(sample_dict) -> float:
    class_of_student = sample_dict["class"]
    students_data = class_of_student["student"]
    marks = students_data["marks"]
    sum_of_numbers = 0
    count = 0
    for key in marks:
        sum_of_numbers += marks[key]
        count += 1
    quantity_of_numbers = count
    average_marks = float(sum_of_numbers // quantity_of_numbers)
    return average_marks

print(student_average_score(sampleDict))