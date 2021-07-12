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
class_of_student = sampleDict["class"]
students_data = class_of_student["student"]
marks = students_data["marks"]
average_score = []


def student_average_score() -> float:
    for key in marks:
        average_score.append(marks[key])

    sum_of_numbers = sum(average_score)
    quantity_of_numbers = len(average_score)
    average_marks = float(sum_of_numbers // quantity_of_numbers)
    return average_marks

print(student_average_score())