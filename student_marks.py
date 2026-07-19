empty_list = []
print(empty_list)
marks = [85, 72, 90, 66, 78]
print("Student marks:", marks)

sample_list = [10, 20, 30] * 2
print("Sample list doubled:", sample_list)

print("The total number of marks:", len(marks))

print("First mark:", marks[0])
print("Last mark:", marks[-1])

_slice = marks[0:3]
print("The first three mark:", _slice)

backward = marks[::-1]
print("The mark list backwards:", backward)

def match_marks(mark_list):
    count = 0
    matched_marks = []
 
    for mark in mark_list:
        mark_text = str(mark)
 
        if len(mark_text) > 1 and mark_text[0] == mark_text[-1]:
            count += 1
            matched_marks.append(mark)
 
    print("Marks with first and last digit same:", matched_marks)
    return count
 
same_digit_count = match_marks([88, 72, 99, 65, 77])
print("Number of matching marks:", same_digit_count)


total = 0
for mark in marks:
  total += mark
average = total / len(marks)
print("The sum of the marks:", total)
print("The average mark:", average)
marks.sort()
 
print("Smallest mark is:", marks[0])
print("Largest mark is:", marks[-1])
