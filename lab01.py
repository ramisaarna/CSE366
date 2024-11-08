import random

def read_student_ids(file_path):
    try:
        with open(file_path, 'r') as file:
            student_ids = [line.strip() for line in file if line.strip()]
        return student_ids
    except FileNotFoundError:
        print("Error: File not found.")
        return []

def select_students_for_viva(student_ids):
    viva_count = 1
    while student_ids:
        selected_student = random.choice(student_ids)
        print(f"Viva #{viva_count}: Selected Student ID - {selected_student}")
        student_ids.remove(selected_student)
        viva_count += 1

def main():
    file_path = 'student_ids.txt'
    student_ids = read_student_ids(file_path)
    
    if not student_ids:
        return  # Exit if file not found or empty
    
    all_students = student_ids.copy()
    
    while True:
        print("\nStarting viva selection process...")
        select_students_for_viva(student_ids)
        
        # Reset the list after all students have been picked
        student_ids = all_students.copy()
        print("\nAll students have been selected. Resetting the list for the next round.")

if __name__ == "__main__":
    main()

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-137
# Viva #2: Selected Student ID - 2024-1-05-131
# Viva #3: Selected Student ID - 2024-1-05-130
# Viva #4: Selected Student ID - 2024-1-05-138
# Viva #5: Selected Student ID - 2024-1-05-139
# Viva #6: Selected Student ID - 2024-1-05-128
# Viva #7: Selected Student ID - 2024-1-05-134
# Viva #8: Selected Student ID - 2024-1-05-136
# Viva #9: Selected Student ID - 2024-1-05-133
# Viva #10: Selected Student ID - 2024-1-05-141
# Viva #11: Selected Student ID - 2024-1-05-142
# Viva #12: Selected Student ID - 2024-1-05-135
# Viva #13: Selected Student ID - 2024-1-05-129
# Viva #14: Selected Student ID - 2024-1-05-140
# Viva #15: Selected Student ID - 2024-1-05-132

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-141
# Viva #2: Selected Student ID - 2024-1-05-136
# Viva #3: Selected Student ID - 2024-1-05-129
# Viva #4: Selected Student ID - 2024-1-05-142
# Viva #5: Selected Student ID - 2024-1-05-140
# Viva #6: Selected Student ID - 2024-1-05-131
# Viva #7: Selected Student ID - 2024-1-05-139
# Viva #8: Selected Student ID - 2024-1-05-130
# Viva #9: Selected Student ID - 2024-1-05-133
# Viva #10: Selected Student ID - 2024-1-05-132
# Viva #11: Selected Student ID - 2024-1-05-137
# Viva #12: Selected Student ID - 2024-1-05-128
# Viva #13: Selected Student ID - 2024-1-05-135
# Viva #14: Selected Student ID - 2024-1-05-134
# Viva #15: Selected Student ID - 2024-1-05-138

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-138
# Viva #2: Selected Student ID - 2024-1-05-139
# Viva #3: Selected Student ID - 2024-1-05-142
# Viva #4: Selected Student ID - 2024-1-05-128
# Viva #5: Selected Student ID - 2024-1-05-136
# Viva #6: Selected Student ID - 2024-1-05-131
# Viva #7: Selected Student ID - 2024-1-05-130
# Viva #8: Selected Student ID - 2024-1-05-135
# Viva #9: Selected Student ID - 2024-1-05-137
# Viva #10: Selected Student ID - 2024-1-05-129
# Viva #11: Selected Student ID - 2024-1-05-140
# Viva #12: Selected Student ID - 2024-1-05-132
# Viva #13: Selected Student ID - 2024-1-05-141
# Viva #14: Selected Student ID - 2024-1-05-133
# Viva #15: Selected Student ID - 2024-1-05-134

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-134
# Viva #2: Selected Student ID - 2024-1-05-142
# Viva #3: Selected Student ID - 2024-1-05-139
# Viva #4: Selected Student ID - 2024-1-05-133
# Viva #5: Selected Student ID - 2024-1-05-129
# Viva #6: Selected Student ID - 2024-1-05-141
# Viva #7: Selected Student ID - 2024-1-05-136
# Viva #8: Selected Student ID - 2024-1-05-137
# Viva #9: Selected Student ID - 2024-1-05-135
# Viva #10: Selected Student ID - 2024-1-05-140
# Viva #11: Selected Student ID - 2024-1-05-131
# Viva #12: Selected Student ID - 2024-1-05-130
# Viva #13: Selected Student ID - 2024-1-05-128
# Viva #14: Selected Student ID - 2024-1-05-138
# Viva #15: Selected Student ID - 2024-1-05-132

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-128
# Viva #2: Selected Student ID - 2024-1-05-138
# Viva #3: Selected Student ID - 2024-1-05-134
# Viva #4: Selected Student ID - 2024-1-05-137
# Viva #5: Selected Student ID - 2024-1-05-142
# Viva #6: Selected Student ID - 2024-1-05-133
# Viva #7: Selected Student ID - 2024-1-05-135
# Viva #8: Selected Student ID - 2024-1-05-139
# Viva #9: Selected Student ID - 2024-1-05-140
# Viva #10: Selected Student ID - 2024-1-05-130
# Viva #11: Selected Student ID - 2024-1-05-136
# Viva #12: Selected Student ID - 2024-1-05-132
# Viva #13: Selected Student ID - 2024-1-05-129
# Viva #14: Selected Student ID - 2024-1-05-131
# Viva #15: Selected Student ID - 2024-1-05-141

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-142
# Viva #2: Selected Student ID - 2024-1-05-136
# Viva #3: Selected Student ID - 2024-1-05-135
# Viva #4: Selected Student ID - 2024-1-05-131
# Viva #5: Selected Student ID - 2024-1-05-132
# Viva #6: Selected Student ID - 2024-1-05-134
# Viva #7: Selected Student ID - 2024-1-05-140
# Viva #8: Selected Student ID - 2024-1-05-139
# Viva #9: Selected Student ID - 2024-1-05-141
# Viva #10: Selected Student ID - 2024-1-05-128
# Viva #11: Selected Student ID - 2024-1-05-137
# Viva #12: Selected Student ID - 2024-1-05-129
# Viva #13: Selected Student ID - 2024-1-05-130
# Viva #14: Selected Student ID - 2024-1-05-133
# Viva #15: Selected Student ID - 2024-1-05-138

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-130
# Viva #2: Selected Student ID - 2024-1-05-134
# Viva #3: Selected Student ID - 2024-1-05-128
# Viva #4: Selected Student ID - 2024-1-05-129
# Viva #5: Selected Student ID - 2024-1-05-141
# Viva #6: Selected Student ID - 2024-1-05-140
# Viva #7: Selected Student ID - 2024-1-05-137
# Viva #8: Selected Student ID - 2024-1-05-133
# Viva #9: Selected Student ID - 2024-1-05-139
# Viva #10: Selected Student ID - 2024-1-05-138
# Viva #11: Selected Student ID - 2024-1-05-131
# Viva #12: Selected Student ID - 2024-1-05-132
# Viva #13: Selected Student ID - 2024-1-05-142
# Viva #14: Selected Student ID - 2024-1-05-135
# Viva #15: Selected Student ID - 2024-1-05-136

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-134
# Viva #2: Selected Student ID - 2024-1-05-139
# Viva #3: Selected Student ID - 2024-1-05-128
# Viva #4: Selected Student ID - 2024-1-05-135
# Viva #5: Selected Student ID - 2024-1-05-132
# Viva #6: Selected Student ID - 2024-1-05-136
# Viva #7: Selected Student ID - 2024-1-05-138
# Viva #8: Selected Student ID - 2024-1-05-137
# Viva #9: Selected Student ID - 2024-1-05-140
# Viva #10: Selected Student ID - 2024-1-05-130
# Viva #11: Selected Student ID - 2024-1-05-142
# Viva #12: Selected Student ID - 2024-1-05-133
# Viva #13: Selected Student ID - 2024-1-05-129
# Viva #14: Selected Student ID - 2024-1-05-141
# Viva #15: Selected Student ID - 2024-1-05-131

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-142
# Viva #2: Selected Student ID - 2024-1-05-136
# Viva #3: Selected Student ID - 2024-1-05-132
# Viva #4: Selected Student ID - 2024-1-05-128
# Viva #5: Selected Student ID - 2024-1-05-137
# Viva #6: Selected Student ID - 2024-1-05-129
# Viva #7: Selected Student ID - 2024-1-05-139
# Viva #8: Selected Student ID - 2024-1-05-133
# Viva #9: Selected Student ID - 2024-1-05-140
# Viva #10: Selected Student ID - 2024-1-05-130
# Viva #11: Selected Student ID - 2024-1-05-138
# Viva #12: Selected Student ID - 2024-1-05-141
# Viva #13: Selected Student ID - 2024-1-05-135
# Viva #14: Selected Student ID - 2024-1-05-134
# Viva #15: Selected Student ID - 2024-1-05-131

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-137
# Viva #2: Selected Student ID - 2024-1-05-140
# Viva #3: Selected Student ID - 2024-1-05-135
# Viva #4: Selected Student ID - 2024-1-05-129
# Viva #5: Selected Student ID - 2024-1-05-128
# Viva #6: Selected Student ID - 2024-1-05-142
# Viva #7: Selected Student ID - 2024-1-05-141
# Viva #8: Selected Student ID - 2024-1-05-134
# Viva #9: Selected Student ID - 2024-1-05-139
# Viva #10: Selected Student ID - 2024-1-05-136
# Viva #11: Selected Student ID - 2024-1-05-138
# Viva #12: Selected Student ID - 2024-1-05-132
# Viva #13: Selected Student ID - 2024-1-05-130
# Viva #14: Selected Student ID - 2024-1-05-131
# Viva #15: Selected Student ID - 2024-1-05-133

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-135
# Viva #2: Selected Student ID - 2024-1-05-142
# Viva #3: Selected Student ID - 2024-1-05-130
# Viva #4: Selected Student ID - 2024-1-05-131
# Viva #5: Selected Student ID - 2024-1-05-137
# Viva #6: Selected Student ID - 2024-1-05-139
# Viva #7: Selected Student ID - 2024-1-05-140
# Viva #8: Selected Student ID - 2024-1-05-129
# Viva #9: Selected Student ID - 2024-1-05-133
# Viva #10: Selected Student ID - 2024-1-05-132
# Viva #11: Selected Student ID - 2024-1-05-141
# Viva #12: Selected Student ID - 2024-1-05-128
# Viva #13: Selected Student ID - 2024-1-05-138
# Viva #14: Selected Student ID - 2024-1-05-134
# Viva #15: Selected Student ID - 2024-1-05-136

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-142
# Viva #2: Selected Student ID - 2024-1-05-141
# Viva #3: Selected Student ID - 2024-1-05-138
# Viva #4: Selected Student ID - 2024-1-05-130
# Viva #5: Selected Student ID - 2024-1-05-128
# Viva #6: Selected Student ID - 2024-1-05-133
# Viva #7: Selected Student ID - 2024-1-05-137
# Viva #8: Selected Student ID - 2024-1-05-131
# Viva #9: Selected Student ID - 2024-1-05-135
# Viva #10: Selected Student ID - 2024-1-05-140
# Viva #11: Selected Student ID - 2024-1-05-129
# Viva #12: Selected Student ID - 2024-1-05-132
# Viva #13: Selected Student ID - 2024-1-05-136
# Viva #14: Selected Student ID - 2024-1-05-139
# Viva #15: Selected Student ID - 2024-1-05-134

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-129
# Viva #2: Selected Student ID - 2024-1-05-128
# Viva #3: Selected Student ID - 2024-1-05-136
# Viva #4: Selected Student ID - 2024-1-05-134
# Viva #5: Selected Student ID - 2024-1-05-140
# Viva #6: Selected Student ID - 2024-1-05-130
# Viva #7: Selected Student ID - 2024-1-05-142
# Viva #8: Selected Student ID - 2024-1-05-139
# Viva #9: Selected Student ID - 2024-1-05-135
# Viva #10: Selected Student ID - 2024-1-05-131
# Viva #11: Selected Student ID - 2024-1-05-141
# Viva #12: Selected Student ID - 2024-1-05-132
# Viva #13: Selected Student ID - 2024-1-05-138
# Viva #14: Selected Student ID - 2024-1-05-137
# Viva #15: Selected Student ID - 2024-1-05-133

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-131
# Viva #2: Selected Student ID - 2024-1-05-138
# Viva #3: Selected Student ID - 2024-1-05-139
# Viva #4: Selected Student ID - 2024-1-05-132
# Viva #5: Selected Student ID - 2024-1-05-129
# Viva #6: Selected Student ID - 2024-1-05-130
# Viva #7: Selected Student ID - 2024-1-05-128
# Viva #8: Selected Student ID - 2024-1-05-133
# Viva #9: Selected Student ID - 2024-1-05-136
# Viva #10: Selected Student ID - 2024-1-05-137
# Viva #11: Selected Student ID - 2024-1-05-141
# Viva #12: Selected Student ID - 2024-1-05-142
# Viva #13: Selected Student ID - 2024-1-05-134
# Viva #14: Selected Student ID - 2024-1-05-140
# Viva #15: Selected Student ID - 2024-1-05-135

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-134
# Viva #2: Selected Student ID - 2024-1-05-141
# Viva #3: Selected Student ID - 2024-1-05-132
# Viva #4: Selected Student ID - 2024-1-05-135
# Viva #5: Selected Student ID - 2024-1-05-130
# Viva #6: Selected Student ID - 2024-1-05-142
# Viva #7: Selected Student ID - 2024-1-05-139
# Viva #8: Selected Student ID - 2024-1-05-131
# Viva #9: Selected Student ID - 2024-1-05-136
# Viva #10: Selected Student ID - 2024-1-05-140
# Viva #11: Selected Student ID - 2024-1-05-137
# Viva #12: Selected Student ID - 2024-1-05-128
# Viva #13: Selected Student ID - 2024-1-05-133
# Viva #14: Selected Student ID - 2024-1-05-129
# Viva #15: Selected Student ID - 2024-1-05-138

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-129
# Viva #2: Selected Student ID - 2024-1-05-133
# Viva #3: Selected Student ID - 2024-1-05-136
# Viva #4: Selected Student ID - 2024-1-05-142
# Viva #5: Selected Student ID - 2024-1-05-130
# Viva #6: Selected Student ID - 2024-1-05-131
# Viva #7: Selected Student ID - 2024-1-05-132
# Viva #8: Selected Student ID - 2024-1-05-128
# Viva #9: Selected Student ID - 2024-1-05-137
# Viva #10: Selected Student ID - 2024-1-05-135
# Viva #11: Selected Student ID - 2024-1-05-141
# Viva #12: Selected Student ID - 2024-1-05-138
# Viva #13: Selected Student ID - 2024-1-05-139
# Viva #14: Selected Student ID - 2024-1-05-134
# Viva #15: Selected Student ID - 2024-1-05-140

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-135
# Viva #2: Selected Student ID - 2024-1-05-140
# Viva #3: Selected Student ID - 2024-1-05-141
# Viva #4: Selected Student ID - 2024-1-05-133
# Viva #5: Selected Student ID - 2024-1-05-137
# Viva #6: Selected Student ID - 2024-1-05-138
# Viva #7: Selected Student ID - 2024-1-05-134
# Viva #8: Selected Student ID - 2024-1-05-130
# Viva #9: Selected Student ID - 2024-1-05-128
# Viva #10: Selected Student ID - 2024-1-05-139
# Viva #11: Selected Student ID - 2024-1-05-136
# Viva #12: Selected Student ID - 2024-1-05-132
# Viva #13: Selected Student ID - 2024-1-05-131
# Viva #14: Selected Student ID - 2024-1-05-129
# Viva #15: Selected Student ID - 2024-1-05-142

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-142
# Viva #2: Selected Student ID - 2024-1-05-136
# Viva #3: Selected Student ID - 2024-1-05-139
# Viva #4: Selected Student ID - 2024-1-05-132
# Viva #5: Selected Student ID - 2024-1-05-137
# Viva #6: Selected Student ID - 2024-1-05-129
# Viva #7: Selected Student ID - 2024-1-05-141
# Viva #8: Selected Student ID - 2024-1-05-134
# Viva #9: Selected Student ID - 2024-1-05-138
# Viva #10: Selected Student ID - 2024-1-05-131
# Viva #11: Selected Student ID - 2024-1-05-133
# Viva #12: Selected Student ID - 2024-1-05-130
# Viva #13: Selected Student ID - 2024-1-05-128
# Viva #14: Selected Student ID - 2024-1-05-140
# Viva #15: Selected Student ID - 2024-1-05-135

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-137
# Viva #2: Selected Student ID - 2024-1-05-128
# Viva #3: Selected Student ID - 2024-1-05-132
# Viva #4: Selected Student ID - 2024-1-05-133
# Viva #5: Selected Student ID - 2024-1-05-138
# Viva #6: Selected Student ID - 2024-1-05-131
# Viva #7: Selected Student ID - 2024-1-05-141
# Viva #8: Selected Student ID - 2024-1-05-129
# Viva #9: Selected Student ID - 2024-1-05-135
# Viva #10: Selected Student ID - 2024-1-05-130
# Viva #11: Selected Student ID - 2024-1-05-140
# Viva #12: Selected Student ID - 2024-1-05-139
# Viva #13: Selected Student ID - 2024-1-05-136
# Viva #14: Selected Student ID - 2024-1-05-134
# Viva #15: Selected Student ID - 2024-1-05-142

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-131
# Viva #2: Selected Student ID - 2024-1-05-132
# Viva #3: Selected Student ID - 2024-1-05-135
# Viva #4: Selected Student ID - 2024-1-05-138
# Viva #5: Selected Student ID - 2024-1-05-136
# Viva #6: Selected Student ID - 2024-1-05-139
# Viva #7: Selected Student ID - 2024-1-05-130
# Viva #8: Selected Student ID - 2024-1-05-137
# Viva #9: Selected Student ID - 2024-1-05-141
# Viva #10: Selected Student ID - 2024-1-05-142
# Viva #11: Selected Student ID - 2024-1-05-129
# Viva #12: Selected Student ID - 2024-1-05-140
# Viva #13: Selected Student ID - 2024-1-05-128
# Viva #14: Selected Student ID - 2024-1-05-134
# Viva #15: Selected Student ID - 2024-1-05-133

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-132
# Viva #2: Selected Student ID - 2024-1-05-136
# Viva #3: Selected Student ID - 2024-1-05-134
# Viva #4: Selected Student ID - 2024-1-05-142
# Viva #5: Selected Student ID - 2024-1-05-133
# Viva #6: Selected Student ID - 2024-1-05-131
# Viva #7: Selected Student ID - 2024-1-05-138
# Viva #8: Selected Student ID - 2024-1-05-141
# Viva #9: Selected Student ID - 2024-1-05-128
# Viva #10: Selected Student ID - 2024-1-05-139
# Viva #11: Selected Student ID - 2024-1-05-140
# Viva #12: Selected Student ID - 2024-1-05-130
# Viva #13: Selected Student ID - 2024-1-05-135
# Viva #14: Selected Student ID - 2024-1-05-137
# Viva #15: Selected Student ID - 2024-1-05-129

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-135
# Viva #2: Selected Student ID - 2024-1-05-128
# Viva #3: Selected Student ID - 2024-1-05-134
# Viva #4: Selected Student ID - 2024-1-05-139
# Viva #5: Selected Student ID - 2024-1-05-132
# Viva #6: Selected Student ID - 2024-1-05-138
# Viva #7: Selected Student ID - 2024-1-05-129
# Viva #8: Selected Student ID - 2024-1-05-140
# Viva #9: Selected Student ID - 2024-1-05-133
# Viva #10: Selected Student ID - 2024-1-05-137
# Viva #11: Selected Student ID - 2024-1-05-141
# Viva #12: Selected Student ID - 2024-1-05-142
# Viva #13: Selected Student ID - 2024-1-05-131
# Viva #14: Selected Student ID - 2024-1-05-130
# Viva #15: Selected Student ID - 2024-1-05-136

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-135
# Viva #2: Selected Student ID - 2024-1-05-128
# Viva #3: Selected Student ID - 2024-1-05-130
# Viva #4: Selected Student ID - 2024-1-05-140
# Viva #5: Selected Student ID - 2024-1-05-132
# Viva #6: Selected Student ID - 2024-1-05-131
# Viva #7: Selected Student ID - 2024-1-05-134
# Viva #8: Selected Student ID - 2024-1-05-142
# Viva #9: Selected Student ID - 2024-1-05-139
# Viva #10: Selected Student ID - 2024-1-05-137
# Viva #11: Selected Student ID - 2024-1-05-136
# Viva #12: Selected Student ID - 2024-1-05-141
# Viva #13: Selected Student ID - 2024-1-05-133
# Viva #14: Selected Student ID - 2024-1-05-138
# Viva #15: Selected Student ID - 2024-1-05-129

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-142
# Viva #2: Selected Student ID - 2024-1-05-138
# Viva #3: Selected Student ID - 2024-1-05-140
# Viva #4: Selected Student ID - 2024-1-05-129
# Viva #5: Selected Student ID - 2024-1-05-135
# Viva #6: Selected Student ID - 2024-1-05-132
# Viva #7: Selected Student ID - 2024-1-05-131
# Viva #8: Selected Student ID - 2024-1-05-136
# Viva #9: Selected Student ID - 2024-1-05-128
# Viva #10: Selected Student ID - 2024-1-05-141
# Viva #11: Selected Student ID - 2024-1-05-137
# Viva #12: Selected Student ID - 2024-1-05-139
# Viva #13: Selected Student ID - 2024-1-05-130
# Viva #14: Selected Student ID - 2024-1-05-134
# Viva #15: Selected Student ID - 2024-1-05-133

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-139
# Viva #2: Selected Student ID - 2024-1-05-131
# Viva #3: Selected Student ID - 2024-1-05-137
# Viva #4: Selected Student ID - 2024-1-05-136
# Viva #5: Selected Student ID - 2024-1-05-141
# Viva #6: Selected Student ID - 2024-1-05-133
# Viva #7: Selected Student ID - 2024-1-05-140
# Viva #8: Selected Student ID - 2024-1-05-138
# Viva #9: Selected Student ID - 2024-1-05-132
# Viva #10: Selected Student ID - 2024-1-05-130
# Viva #11: Selected Student ID - 2024-1-05-128
# Viva #12: Selected Student ID - 2024-1-05-135
# Viva #13: Selected Student ID - 2024-1-05-129
# Viva #14: Selected Student ID - 2024-1-05-134
# Viva #15: Selected Student ID - 2024-1-05-142

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-137
# Viva #2: Selected Student ID - 2024-1-05-138
# Viva #3: Selected Student ID - 2024-1-05-130
# Viva #4: Selected Student ID - 2024-1-05-132
# Viva #5: Selected Student ID - 2024-1-05-128
# Viva #6: Selected Student ID - 2024-1-05-131
# Viva #7: Selected Student ID - 2024-1-05-140
# Viva #8: Selected Student ID - 2024-1-05-135
# Viva #9: Selected Student ID - 2024-1-05-129
# Viva #10: Selected Student ID - 2024-1-05-139
# Viva #11: Selected Student ID - 2024-1-05-141
# Viva #12: Selected Student ID - 2024-1-05-133
# Viva #13: Selected Student ID - 2024-1-05-134
# Viva #14: Selected Student ID - 2024-1-05-142
# Viva #15: Selected Student ID - 2024-1-05-136

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-133
# Viva #2: Selected Student ID - 2024-1-05-132
# Viva #3: Selected Student ID - 2024-1-05-137
# Viva #4: Selected Student ID - 2024-1-05-136
# Viva #5: Selected Student ID - 2024-1-05-140
# Viva #6: Selected Student ID - 2024-1-05-135
# Viva #7: Selected Student ID - 2024-1-05-134
# Viva #8: Selected Student ID - 2024-1-05-128
# Viva #9: Selected Student ID - 2024-1-05-139
# Viva #10: Selected Student ID - 2024-1-05-138
# Viva #11: Selected Student ID - 2024-1-05-131
# Viva #12: Selected Student ID - 2024-1-05-142
# Viva #13: Selected Student ID - 2024-1-05-141
# Viva #14: Selected Student ID - 2024-1-05-129
# Viva #15: Selected Student ID - 2024-1-05-130

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-139
# Viva #2: Selected Student ID - 2024-1-05-132
# Viva #3: Selected Student ID - 2024-1-05-142
# Viva #4: Selected Student ID - 2024-1-05-137
# Viva #5: Selected Student ID - 2024-1-05-129
# Viva #6: Selected Student ID - 2024-1-05-140
# Viva #7: Selected Student ID - 2024-1-05-130
# Viva #8: Selected Student ID - 2024-1-05-138
# Viva #9: Selected Student ID - 2024-1-05-141
# Viva #10: Selected Student ID - 2024-1-05-131
# Viva #11: Selected Student ID - 2024-1-05-135
# Viva #12: Selected Student ID - 2024-1-05-134
# Viva #13: Selected Student ID - 2024-1-05-128
# Viva #14: Selected Student ID - 2024-1-05-133
# Viva #15: Selected Student ID - 2024-1-05-136

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-137
# Viva #2: Selected Student ID - 2024-1-05-139
# Viva #3: Selected Student ID - 2024-1-05-129
# Viva #4: Selected Student ID - 2024-1-05-128
# Viva #5: Selected Student ID - 2024-1-05-133
# Viva #6: Selected Student ID - 2024-1-05-136
# Viva #7: Selected Student ID - 2024-1-05-131
# Viva #8: Selected Student ID - 2024-1-05-141
# Viva #9: Selected Student ID - 2024-1-05-135
# Viva #10: Selected Student ID - 2024-1-05-132
# Viva #11: Selected Student ID - 2024-1-05-142
# Viva #12: Selected Student ID - 2024-1-05-134
# Viva #13: Selected Student ID - 2024-1-05-138
# Viva #14: Selected Student ID - 2024-1-05-130
# Viva #15: Selected Student ID - 2024-1-05-140

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-137
# Viva #2: Selected Student ID - 2024-1-05-133
# Viva #3: Selected Student ID - 2024-1-05-131
# Viva #4: Selected Student ID - 2024-1-05-130
# Viva #5: Selected Student ID - 2024-1-05-138
# Viva #6: Selected Student ID - 2024-1-05-132
# Viva #7: Selected Student ID - 2024-1-05-128
# Viva #8: Selected Student ID - 2024-1-05-129
# Viva #9: Selected Student ID - 2024-1-05-142
# Viva #10: Selected Student ID - 2024-1-05-134
# Viva #11: Selected Student ID - 2024-1-05-139
# Viva #12: Selected Student ID - 2024-1-05-141
# Viva #13: Selected Student ID - 2024-1-05-136
# Viva #14: Selected Student ID - 2024-1-05-140
# Viva #15: Selected Student ID - 2024-1-05-135

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-135
# Viva #2: Selected Student ID - 2024-1-05-134
# Viva #3: Selected Student ID - 2024-1-05-138
# Viva #4: Selected Student ID - 2024-1-05-132
# Viva #5: Selected Student ID - 2024-1-05-140
# Viva #6: Selected Student ID - 2024-1-05-128
# Viva #7: Selected Student ID - 2024-1-05-139
# Viva #8: Selected Student ID - 2024-1-05-133
# Viva #9: Selected Student ID - 2024-1-05-129
# Viva #10: Selected Student ID - 2024-1-05-130
# Viva #11: Selected Student ID - 2024-1-05-137
# Viva #12: Selected Student ID - 2024-1-05-142
# Viva #13: Selected Student ID - 2024-1-05-131
# Viva #14: Selected Student ID - 2024-1-05-136
# Viva #15: Selected Student ID - 2024-1-05-141

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-137
# Viva #2: Selected Student ID - 2024-1-05-141
# Viva #3: Selected Student ID - 2024-1-05-130
# Viva #4: Selected Student ID - 2024-1-05-139
# Viva #5: Selected Student ID - 2024-1-05-136
# Viva #6: Selected Student ID - 2024-1-05-140
# Viva #7: Selected Student ID - 2024-1-05-142
# Viva #8: Selected Student ID - 2024-1-05-132
# Viva #9: Selected Student ID - 2024-1-05-138
# Viva #10: Selected Student ID - 2024-1-05-128
# Viva #11: Selected Student ID - 2024-1-05-134
# Viva #12: Selected Student ID - 2024-1-05-131
# Viva #13: Selected Student ID - 2024-1-05-133
# Viva #14: Selected Student ID - 2024-1-05-129
# Viva #15: Selected Student ID - 2024-1-05-135

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-128
# Viva #2: Selected Student ID - 2024-1-05-137
# Viva #3: Selected Student ID - 2024-1-05-136
# Viva #4: Selected Student ID - 2024-1-05-138
# Viva #5: Selected Student ID - 2024-1-05-133
# Viva #6: Selected Student ID - 2024-1-05-140
# Viva #7: Selected Student ID - 2024-1-05-129
# Viva #8: Selected Student ID - 2024-1-05-141
# Viva #9: Selected Student ID - 2024-1-05-139
# Viva #10: Selected Student ID - 2024-1-05-131
# Viva #11: Selected Student ID - 2024-1-05-132
# Viva #12: Selected Student ID - 2024-1-05-135
# Viva #13: Selected Student ID - 2024-1-05-134
# Viva #14: Selected Student ID - 2024-1-05-142
# Viva #15: Selected Student ID - 2024-1-05-130

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-129
# Viva #2: Selected Student ID - 2024-1-05-132
# Viva #3: Selected Student ID - 2024-1-05-135
# Viva #4: Selected Student ID - 2024-1-05-138
# Viva #5: Selected Student ID - 2024-1-05-139
# Viva #6: Selected Student ID - 2024-1-05-137
# Viva #7: Selected Student ID - 2024-1-05-142
# Viva #8: Selected Student ID - 2024-1-05-131
# Viva #9: Selected Student ID - 2024-1-05-133
# Viva #10: Selected Student ID - 2024-1-05-134
# Viva #11: Selected Student ID - 2024-1-05-128
# Viva #12: Selected Student ID - 2024-1-05-136
# Viva #13: Selected Student ID - 2024-1-05-140
# Viva #14: Selected Student ID - 2024-1-05-130
# Viva #15: Selected Student ID - 2024-1-05-141

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-131
# Viva #2: Selected Student ID - 2024-1-05-133
# Viva #3: Selected Student ID - 2024-1-05-141
# Viva #4: Selected Student ID - 2024-1-05-142
# Viva #5: Selected Student ID - 2024-1-05-139
# Viva #6: Selected Student ID - 2024-1-05-129
# Viva #7: Selected Student ID - 2024-1-05-130
# Viva #8: Selected Student ID - 2024-1-05-138
# Viva #9: Selected Student ID - 2024-1-05-132
# Viva #10: Selected Student ID - 2024-1-05-128
# Viva #11: Selected Student ID - 2024-1-05-140
# Viva #12: Selected Student ID - 2024-1-05-134
# Viva #13: Selected Student ID - 2024-1-05-136
# Viva #14: Selected Student ID - 2024-1-05-137
# Viva #15: Selected Student ID - 2024-1-05-135

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-136
# Viva #2: Selected Student ID - 2024-1-05-128
# Viva #3: Selected Student ID - 2024-1-05-133
# Viva #4: Selected Student ID - 2024-1-05-139
# Viva #5: Selected Student ID - 2024-1-05-140
# Viva #6: Selected Student ID - 2024-1-05-135
# Viva #7: Selected Student ID - 2024-1-05-138
# Viva #8: Selected Student ID - 2024-1-05-142
# Viva #9: Selected Student ID - 2024-1-05-134
# Viva #10: Selected Student ID - 2024-1-05-130
# Viva #11: Selected Student ID - 2024-1-05-132
# Viva #12: Selected Student ID - 2024-1-05-141
# Viva #13: Selected Student ID - 2024-1-05-137
# Viva #14: Selected Student ID - 2024-1-05-131
# Viva #15: Selected Student ID - 2024-1-05-129

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-137
# Viva #2: Selected Student ID - 2024-1-05-132
# Viva #3: Selected Student ID - 2024-1-05-139
# Viva #4: Selected Student ID - 2024-1-05-130
# Viva #5: Selected Student ID - 2024-1-05-138
# Viva #6: Selected Student ID - 2024-1-05-140
# Viva #7: Selected Student ID - 2024-1-05-131
# Viva #8: Selected Student ID - 2024-1-05-142
# Viva #9: Selected Student ID - 2024-1-05-129
# Viva #10: Selected Student ID - 2024-1-05-135
# Viva #11: Selected Student ID - 2024-1-05-136
# Viva #12: Selected Student ID - 2024-1-05-133
# Viva #13: Selected Student ID - 2024-1-05-134
# Viva #14: Selected Student ID - 2024-1-05-141
# Viva #15: Selected Student ID - 2024-1-05-128

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-129
# Viva #2: Selected Student ID - 2024-1-05-137
# Viva #3: Selected Student ID - 2024-1-05-142
# Viva #4: Selected Student ID - 2024-1-05-139
# Viva #5: Selected Student ID - 2024-1-05-130
# Viva #6: Selected Student ID - 2024-1-05-128
# Viva #7: Selected Student ID - 2024-1-05-136
# Viva #8: Selected Student ID - 2024-1-05-138
# Viva #9: Selected Student ID - 2024-1-05-135
# Viva #10: Selected Student ID - 2024-1-05-140
# Viva #11: Selected Student ID - 2024-1-05-132
# Viva #12: Selected Student ID - 2024-1-05-133
# Viva #13: Selected Student ID - 2024-1-05-134
# Viva #14: Selected Student ID - 2024-1-05-131
# Viva #15: Selected Student ID - 2024-1-05-141

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-141
# Viva #2: Selected Student ID - 2024-1-05-139
# Viva #3: Selected Student ID - 2024-1-05-132
# Viva #4: Selected Student ID - 2024-1-05-142
# Viva #5: Selected Student ID - 2024-1-05-130
# Viva #6: Selected Student ID - 2024-1-05-131
# Viva #7: Selected Student ID - 2024-1-05-129
# Viva #8: Selected Student ID - 2024-1-05-133
# Viva #9: Selected Student ID - 2024-1-05-128
# Viva #10: Selected Student ID - 2024-1-05-137
# Viva #11: Selected Student ID - 2024-1-05-136
# Viva #12: Selected Student ID - 2024-1-05-138
# Viva #13: Selected Student ID - 2024-1-05-135
# Viva #14: Selected Student ID - 2024-1-05-134
# Viva #15: Selected Student ID - 2024-1-05-140

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-140
# Viva #2: Selected Student ID - 2024-1-05-128
# Viva #3: Selected Student ID - 2024-1-05-142
# Viva #4: Selected Student ID - 2024-1-05-139
# Viva #5: Selected Student ID - 2024-1-05-133
# Viva #6: Selected Student ID - 2024-1-05-138
# Viva #7: Selected Student ID - 2024-1-05-135
# Viva #8: Selected Student ID - 2024-1-05-141
# Viva #9: Selected Student ID - 2024-1-05-131
# Viva #10: Selected Student ID - 2024-1-05-134
# Viva #11: Selected Student ID - 2024-1-05-137
# Viva #12: Selected Student ID - 2024-1-05-136
# Viva #13: Selected Student ID - 2024-1-05-132
# Viva #14: Selected Student ID - 2024-1-05-130
# Viva #15: Selected Student ID - 2024-1-05-129

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-139
# Viva #2: Selected Student ID - 2024-1-05-141
# Viva #3: Selected Student ID - 2024-1-05-132
# Viva #4: Selected Student ID - 2024-1-05-134
# Viva #5: Selected Student ID - 2024-1-05-142
# Viva #6: Selected Student ID - 2024-1-05-135
# Viva #7: Selected Student ID - 2024-1-05-130
# Viva #8: Selected Student ID - 2024-1-05-138
# Viva #9: Selected Student ID - 2024-1-05-128
# Viva #10: Selected Student ID - 2024-1-05-137
# Viva #11: Selected Student ID - 2024-1-05-131
# Viva #12: Selected Student ID - 2024-1-05-136
# Viva #13: Selected Student ID - 2024-1-05-140
# Viva #14: Selected Student ID - 2024-1-05-133
# Viva #15: Selected Student ID - 2024-1-05-129

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-130
# Viva #2: Selected Student ID - 2024-1-05-134
# Viva #3: Selected Student ID - 2024-1-05-131
# Viva #4: Selected Student ID - 2024-1-05-142
# Viva #5: Selected Student ID - 2024-1-05-133
# Viva #6: Selected Student ID - 2024-1-05-128
# Viva #7: Selected Student ID - 2024-1-05-136
# Viva #8: Selected Student ID - 2024-1-05-141
# Viva #9: Selected Student ID - 2024-1-05-135
# Viva #10: Selected Student ID - 2024-1-05-138
# Viva #11: Selected Student ID - 2024-1-05-139
# Viva #12: Selected Student ID - 2024-1-05-137
# Viva #13: Selected Student ID - 2024-1-05-140
# Viva #14: Selected Student ID - 2024-1-05-129
# Viva #15: Selected Student ID - 2024-1-05-132

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-128
# Viva #2: Selected Student ID - 2024-1-05-140
# Viva #3: Selected Student ID - 2024-1-05-137
# Viva #4: Selected Student ID - 2024-1-05-134
# Viva #5: Selected Student ID - 2024-1-05-136
# Viva #6: Selected Student ID - 2024-1-05-133
# Viva #7: Selected Student ID - 2024-1-05-142
# Viva #8: Selected Student ID - 2024-1-05-141
# Viva #9: Selected Student ID - 2024-1-05-135
# Viva #10: Selected Student ID - 2024-1-05-131
# Viva #11: Selected Student ID - 2024-1-05-139
# Viva #12: Selected Student ID - 2024-1-05-129
# Viva #13: Selected Student ID - 2024-1-05-132
# Viva #14: Selected Student ID - 2024-1-05-130
# Viva #15: Selected Student ID - 2024-1-05-138

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-142
# Viva #2: Selected Student ID - 2024-1-05-141
# Viva #3: Selected Student ID - 2024-1-05-139
# Viva #4: Selected Student ID - 2024-1-05-130
# Viva #5: Selected Student ID - 2024-1-05-137
# Viva #6: Selected Student ID - 2024-1-05-133
# Viva #7: Selected Student ID - 2024-1-05-140
# Viva #8: Selected Student ID - 2024-1-05-128
# Viva #9: Selected Student ID - 2024-1-05-129
# Viva #10: Selected Student ID - 2024-1-05-135
# Viva #11: Selected Student ID - 2024-1-05-132
# Viva #12: Selected Student ID - 2024-1-05-131
# Viva #13: Selected Student ID - 2024-1-05-138
# Viva #14: Selected Student ID - 2024-1-05-136
# Viva #15: Selected Student ID - 2024-1-05-134

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-135
# Viva #2: Selected Student ID - 2024-1-05-133
# Viva #3: Selected Student ID - 2024-1-05-136
# Viva #4: Selected Student ID - 2024-1-05-134
# Viva #5: Selected Student ID - 2024-1-05-128
# Viva #6: Selected Student ID - 2024-1-05-131
# Viva #7: Selected Student ID - 2024-1-05-137
# Viva #8: Selected Student ID - 2024-1-05-132
# Viva #9: Selected Student ID - 2024-1-05-139
# Viva #10: Selected Student ID - 2024-1-05-130
# Viva #11: Selected Student ID - 2024-1-05-140
# Viva #12: Selected Student ID - 2024-1-05-129
# Viva #13: Selected Student ID - 2024-1-05-138
# Viva #14: Selected Student ID - 2024-1-05-141
# Viva #15: Selected Student ID - 2024-1-05-142

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-138
# Viva #2: Selected Student ID - 2024-1-05-141
# Viva #3: Selected Student ID - 2024-1-05-130
# Viva #4: Selected Student ID - 2024-1-05-128
# Viva #5: Selected Student ID - 2024-1-05-131
# Viva #6: Selected Student ID - 2024-1-05-137
# Viva #7: Selected Student ID - 2024-1-05-140
# Viva #8: Selected Student ID - 2024-1-05-133
# Viva #9: Selected Student ID - 2024-1-05-136
# Viva #10: Selected Student ID - 2024-1-05-132
# Viva #11: Selected Student ID - 2024-1-05-135
# Viva #12: Selected Student ID - 2024-1-05-142
# Viva #13: Selected Student ID - 2024-1-05-129
# Viva #14: Selected Student ID - 2024-1-05-139
# Viva #15: Selected Student ID - 2024-1-05-134

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-131
# Viva #2: Selected Student ID - 2024-1-05-137
# Viva #3: Selected Student ID - 2024-1-05-139
# Viva #4: Selected Student ID - 2024-1-05-133
# Viva #5: Selected Student ID - 2024-1-05-132
# Viva #6: Selected Student ID - 2024-1-05-130
# Viva #7: Selected Student ID - 2024-1-05-135
# Viva #8: Selected Student ID - 2024-1-05-138
# Viva #9: Selected Student ID - 2024-1-05-140
# Viva #10: Selected Student ID - 2024-1-05-136
# Viva #11: Selected Student ID - 2024-1-05-128
# Viva #12: Selected Student ID - 2024-1-05-134
# Viva #13: Selected Student ID - 2024-1-05-129
# Viva #14: Selected Student ID - 2024-1-05-142
# Viva #15: Selected Student ID - 2024-1-05-141

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-142
# Viva #2: Selected Student ID - 2024-1-05-133
# Viva #3: Selected Student ID - 2024-1-05-132
# Viva #4: Selected Student ID - 2024-1-05-129
# Viva #5: Selected Student ID - 2024-1-05-136
# Viva #6: Selected Student ID - 2024-1-05-138
# Viva #7: Selected Student ID - 2024-1-05-140
# Viva #8: Selected Student ID - 2024-1-05-139
# Viva #9: Selected Student ID - 2024-1-05-128
# Viva #10: Selected Student ID - 2024-1-05-134
# Viva #11: Selected Student ID - 2024-1-05-135
# Viva #12: Selected Student ID - 2024-1-05-130
# Viva #13: Selected Student ID - 2024-1-05-137
# Viva #14: Selected Student ID - 2024-1-05-141
# Viva #15: Selected Student ID - 2024-1-05-131

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-133
# Viva #2: Selected Student ID - 2024-1-05-128
# Viva #3: Selected Student ID - 2024-1-05-137
# Viva #4: Selected Student ID - 2024-1-05-129
# Viva #5: Selected Student ID - 2024-1-05-139
# Viva #6: Selected Student ID - 2024-1-05-131
# Viva #7: Selected Student ID - 2024-1-05-132
# Viva #8: Selected Student ID - 2024-1-05-134
# Viva #9: Selected Student ID - 2024-1-05-130
# Viva #10: Selected Student ID - 2024-1-05-136
# Viva #11: Selected Student ID - 2024-1-05-141
# Viva #12: Selected Student ID - 2024-1-05-135
# Viva #13: Selected Student ID - 2024-1-05-142
# Viva #14: Selected Student ID - 2024-1-05-140
# Viva #15: Selected Student ID - 2024-1-05-138

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-132
# Viva #2: Selected Student ID - 2024-1-05-139
# Viva #3: Selected Student ID - 2024-1-05-130
# Viva #4: Selected Student ID - 2024-1-05-140
# Viva #5: Selected Student ID - 2024-1-05-129
# Viva #6: Selected Student ID - 2024-1-05-131
# Viva #7: Selected Student ID - 2024-1-05-138
# Viva #8: Selected Student ID - 2024-1-05-133
# Viva #9: Selected Student ID - 2024-1-05-142
# Viva #10: Selected Student ID - 2024-1-05-136
# Viva #11: Selected Student ID - 2024-1-05-134
# Viva #12: Selected Student ID - 2024-1-05-141
# Viva #13: Selected Student ID - 2024-1-05-137
# Viva #14: Selected Student ID - 2024-1-05-135
# Viva #15: Selected Student ID - 2024-1-05-128

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-138
# Viva #2: Selected Student ID - 2024-1-05-141
# Viva #3: Selected Student ID - 2024-1-05-131
# Viva #4: Selected Student ID - 2024-1-05-129
# Viva #5: Selected Student ID - 2024-1-05-130
# Viva #6: Selected Student ID - 2024-1-05-132
# Viva #7: Selected Student ID - 2024-1-05-136
# Viva #8: Selected Student ID - 2024-1-05-134
# Viva #9: Selected Student ID - 2024-1-05-128
# Viva #10: Selected Student ID - 2024-1-05-139
# Viva #11: Selected Student ID - 2024-1-05-142
# Viva #12: Selected Student ID - 2024-1-05-137
# Viva #13: Selected Student ID - 2024-1-05-140
# Viva #14: Selected Student ID - 2024-1-05-135
# Viva #15: Selected Student ID - 2024-1-05-133

# All students have been selected. Resetting the list for the next round.

# Starting viva selection process...
# Viva #1: Selected Student ID - 2024-1-05-140
# Viva #2: Selected Student ID - 2024-1-05-136
# Viva #3: Selected Student ID - 2024-1-05-142
# Viva #4: Selected Student ID - 2024-1-05-138
# Viva #5: Selected Student ID - 2024-1-05-131
# Viva #6: Selected Student ID - 2024-1-05-130
# Viva #7: Selected Student ID - 2024-1-05-141
# Viva #8: Selected Student ID - 2024-1-05-133
# Viva #9: Selected Student ID - 2024-1-05-137
# Viva #10: Selected Student ID - 2024-1-05-135
# Viva #11: Selected Student ID - 2024-1-05-132
# Viva #12: Selected Student ID - 2024-1-05-139
# Viva #13: Selected Student ID - 2024-1-05-129
# Viva #14: Selected Student ID - 2024-1-05-128
# Viva #15: Selected Student ID - 2024-1-05-134

# All students have been selected. Resetting the list for the next round.



