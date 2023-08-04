def arithmetic_arranger(problems, show_answer=False):
    numbers = []
    supported_operators = ['+', '-']
    arranged_problems = ""

    if len(problems) > 5:
        return "Error: Too many problems."

    # keep 2D array for tracking
    for problem in problems:
        s = problem.split()
        numbers.append(s)

    if any(map(lambda x: len(x[0]) > 4 or len(x[2]) > 4, numbers)):
        return "Error: Numbers cannot be more than four digits."

    if any(map(lambda x: x[1] not in supported_operators, numbers)):
        return "Error: Operator must be '+' or '-'."

    if not all(map(lambda x: x[0].isdigit() and x[2].isdigit(), numbers)):
        arranged_problems = "Error: Numbers must only contain digits."
        return arranged_problems

    
    top = ''
    bottom = ''
    separator = ''
    solutions = ''
        
    for index, e in enumerate(numbers):
        max_len = int(max(len(e[0]), len(e[2])))
        top += e[0].rjust(max_len + 2)
        bottom += e[1] + e[2].rjust(max_len + 1)
        separator += ('-' * (max_len + 2))
        solutions += str(eval(' '.join(e))).rjust(max_len + 2)

        # Do not add trailing whitespace on final output
        if index < len(numbers) - 1:
            top += " " * 4
            bottom += " " * 4
            separator += " " * 4
            solutions += " " * 4

    if show_answer:
        arranged_problems = "\n".join((top, bottom, separator, solutions))
    else:
        arranged_problems = "\n".join((top, bottom, separator))

    return arranged_problems