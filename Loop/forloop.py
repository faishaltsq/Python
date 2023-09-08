
#menghitung rata-rata tinggi badan
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  
#membuat variabel untuk looping dan menghitung jumlah tinggi badan

total_height = 0

for height in student_heights:
      total_height += height

#menghitung jumlah mahasiswa

total_people = 0

for people in student_heights:
      total_people += 1
      
#menghitung rata-rata tinggi badan
average = total_height/total_people
print(round(average))





#membuat perulangan menampilkan nilai tertinggi

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)


highest_score = 0

for score in student_scores:
      if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")