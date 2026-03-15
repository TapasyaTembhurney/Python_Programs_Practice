marks = [56,89,99,98,97]
extra_marks = [ 99 , 100]
print(marks)

marks.append(88)
print(marks)

marks.pop()
print(marks)

marks.extend(extra_marks)
print("The extra marks added is :",marks)

marks.insert(5 , 96)
print("The newly inserted element is :",marks)

marks.sort()
print("The Sorted lists is :", marks)

marks.remove(56)
print(marks)

marks.reverse()
print("The reversed element is : ", marks)

copied = marks.copy()
print(copied)

count = marks.count(99)
print("The count of given element is : ", count)

index = marks.index(97)
print("The index of given element is : ",index)

marks.clear()
print(marks)

