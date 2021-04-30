"""

The program will display and calculate the number of grades, the mean grade, and the percentage of grades that are above the average grades. There should be two functions. 

The first function will start with a for loop to count the number of grades, starting at zero, compare it with the average grade, and if the grade is bigger, increase the count.
Then it will return the count divided by the grades.

The second function, the main function, will open Final.txt file. From here, we will print the number of grades. Afterwards, we will calculate the average grade. Finally, the program 
will print the average grade and the percentage of grades above the average.

"""


"""

First funcion, calculate_percent_above_average().
    Set count = 0.
    Use for loop to compare grades.
    If grade > average, increase count by one.
    Return count divided by grade.

Second funtion, main().
    Set givenFile = open("Final.txt")
    grades = []

    Use loop to count number of grades in Final.txt.
    print("Number of grades:", grades)

    Set average grade = 0.
    Use for loop to compare grades.
        average = average + grade

    average = average / grade
    print("Average grade:", average)
    print("Percentage of grades above average:")

    I don't know how to complete the part on "Percentage of grades above average."

main

"""


def calculate_percent_above_average(grades, average):

    count = 0
    for score in grades:
        if score > average:
            count = count + 1
    return (count / grades)


def main():

    givenFile = open("Final.txt")
    grades = []

    for line in givenFile:
        grades.append(int(line))
    print("Number of grades:", grades)

    average = 0
    for score in grades:
        average = average + grades
    average = average / grades

    print("Average grade:", average)
    print("Percentage of grades above average:")

    givenfile.close()


main()
