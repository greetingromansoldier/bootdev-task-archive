---
title: "Pupil Records"
date: 2025-03-24
tags: [PupilRecords, StudentClass]
---

# Pupil Records

Players can recruit wizard pupils into their armies. Depending on the pupil's marks, they gain different in-game abilities.

---

## Assignment: Student Class

### 1. Complete the Constructor
1. Set the `name` parameter to the `name` instance variable.
2. Initialize a private data member called `__courses` to an empty dictionary.

### 2. Create the `calculate_letter_grade` Method
- **Parameter**: `score`
- **Logic**:
  - If `score` is 90 or above: **return `"A"`**
  - If `score` is between 80 and 89 (inclusive): **return `"B"`**
  - If `score` is between 70 and 79 (inclusive): **return `"C"`**
  - If `score` is between 60 and 69 (inclusive): **return `"D"`**
  - Otherwise: **return `"F"`**

### 3. Create the `add_course` Method
- **Parameters**: `course_name`, `score`
- **Steps**:
  1. Calculate the letter grade using the `calculate_letter_grade` method.
  2. Use `course_name` as the key in the `__courses` dictionary.
  3. Assign the calculated letter grade as the corresponding value.

### 4. Create the `get_courses` Method
- **Return**: The private `__courses` dictionary.
