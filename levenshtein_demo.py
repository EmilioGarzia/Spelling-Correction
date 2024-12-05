# Levenshtein edit distance: usage demo
#
# @author Emilio Garzia, 2024

from spelling_correction.Levenshtein import levenshtein

if __name__ == "__main__":
    source = "Elephant"
    target = "relevant"

    edit_distance_calculator = levenshtein(source=source, target=target)

    print(f"Levenshtein Matrix\n{edit_distance_calculator.distance_matrix}\n")
    print(f"Backtrace Matrix\n{edit_distance_calculator.backtrace_matrix}\n")
    print(f"Backtrace Matrix in ASCII\n{edit_distance_calculator.backtrace_to_ascii()}\n")
    print(f"Minimum edit distance: {edit_distance_calculator.get_edit_distance()}\n")
    
    print("Operation history")
    for operation in edit_distance_calculator.operations_history():
        print(operation)