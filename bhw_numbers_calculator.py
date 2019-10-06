#!/usr/bin/env python3
# Thank @mkhramenkov for calcPi
import sys


def calcPi(x: int):
    k, a, b, a1, b1 = 2, 4, 1, 12, 4
    while x > 0:
        p, q, k = k * k, 2 * k + 1, k + 1
        a, b, a1, b1 = a1, b1, p * a + q * a1, p * b + q * b1
        d, d1 = a / b, a1 / b1
        while d == d1 and x > 0:
            yield str(int(d))
            x -= 1
            a, a1 = 10 * (a % b), 10 * (a1 % b1)
            d, d1 = a / b, a1 / b1


def get_digits(digit_count: int) -> str:
    digits = ""
    for digit in calcPi(digit_count + 1):
        digits += digit
    return digits


def check_input():
    if len(sys.argv) != 3:
        sys.exit("usage: ./bhw_numbers_calculator.py group_number input_file")
    else:
        return int(sys.argv[1]), sys.argv[2], f"numbers{int(sys.argv[1])}.txt"


def get_digit_number(task_number:int, group_number: int, student_number: int) -> int:
    return (task_number - 1) * 300 + (group_number - 183) * 35 + student_number


def parse_students(input_file: str) -> dict:
    students = dict()
    with open(input_file, 'r') as file:
        for student_data in file:
            index, student = student_data.split('\t')
            split_student = student.split(' ')
            students[int(index)] = split_student[0] + ' ' + split_student[1].split('\n')[0]

    return students


def write_result(digits: str, group_number: int, first_task_number: int,
        last_task_number: int, student_numbers: dict(), output_file: str) -> None:
    with open(output_file, 'w') as file:
        file.write(f"Made by @cdraugr.\nГруппа БПМИ{group_number}:\n")
        for task_number in range(first_task_number, last_task_number + 1):
            file.write(f"Номер {task_number}:\n")

            subparagraphs = [[] for _ in range(10)]
            for student_number, student_name in student_numbers.items():
                subparagraphs[
                    int(digits[get_digit_number(task_number, group_number, student_number)])
                ].append(student_name)

            for subparagraph_index in range(10):
                if len(subparagraphs[subparagraph_index]):
                    file.write(f"\tПодпункт {task_number}.{subparagraph_index}:\n")
                    for student_name in subparagraphs[subparagraph_index]:
                        file.write(f"\t\t{student_name}\n")

            file.write('\n')

def main() -> None:
    first_task_number = 1
    last_task_number = 50

    group_number, input_file, output_file = check_input()
    student_numbers = parse_students(input_file)

    digits = get_digits(get_digit_number(
        last_task_number, group_number, max(student_numbers.keys()) + 1)
    )

    write_result(digits, group_number, first_task_number,
        last_task_number, student_numbers, output_file)


if __name__ == "__main__":
    main()
