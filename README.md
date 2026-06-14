# GradeMatrix

## Fair, Fast & Intelligent Student Performance Analysis

GradeMatrix is a Python-based desktop application that helps teachers evaluate student performance more accurately using **Weighted Averages** instead of traditional Simple Averages.

The project was developed to solve a common problem in academic evaluation: recent student performance should matter more than old test scores. GradeMatrix uses **Linear Algebra and Matrix Multiplication** through NumPy to efficiently calculate weighted scores for hundreds or even thousands of students in seconds.

---

## 🚀 Why GradeMatrix?

Most schools calculate student performance using a **Simple Average**, which treats every test equally.

### Problem with Simple Averages

* A student who improves significantly before final exams still appears weak because old low scores reduce the average.
* A strong student who performs poorly in one recent test may be unfairly penalized.
* Simple averages fail to represent the student's current academic condition.

### Our Solution

GradeMatrix uses a **Weighted Average System** where teachers assign higher importance (weights) to recent tests.

Example:

| Test   | Score | Weight |
| ------ | ----- | ------ |
| Test 1 | 40    | 1      |
| Test 2 | 50    | 1      |
| Test 3 | 80    | 3      |

Recent performance influences the final score more heavily, producing a fairer evaluation.

---

## ✨ Features

* Modern graphical user interface built with CustomTkinter
* Upload student marks from CSV files
* Dynamically assign weights to each test
* Calculate both:

  * Simple Average
  * Weighted Average
* Uses NumPy Matrix Multiplication for high-speed calculations
* Automatically sorts students by performance
* Generates a new CSV file containing results
* Helps identify students who may need extra coaching ("Last Minute Batch")

---

## 🧮 The Mathematics Behind GradeMatrix

Instead of calculating scores one student at a time, GradeMatrix uses Matrix Multiplication.

Let:

**A = Student Marks Matrix**

A =

| Student | Test1 | Test2 | Test3 |
| ------- | ----- | ----- | ----- |
| S1      | 70    | 80    | 90    |
| S2      | 50    | 60    | 70    |

**W = Weight Matrix**

W =

| Weight |
| ------ |
| 1      |
| 2      |
| 3      |

The program computes:

Weighted Scores = A × W

This vectorized operation allows NumPy to process hundreds or thousands of records extremely quickly.

---

## ⚡ Why Matrix Multiplication?

Imagine packing 200 lunchboxes.

* A traditional loop packs one lunchbox at a time.
* Matrix multiplication acts like a giant automated machine filling all lunchboxes simultaneously.

Both methods produce the same result, but matrix operations are significantly faster and more efficient.

---

## 🛠 Technologies Used

* Python 3
* NumPy
* Pandas
* CustomTkinter
* Tkinter

---

## 📂 Input CSV Format

Example:

```csv
Student_Name,Test1,Test2,Test3
Rahul,45,52,70
Priya,80,85,90
Aman,30,40,65
```

* First column must contain student names.
* Remaining columns should contain test marks.

---

## 📊 Output

The generated CSV file contains:

* Original marks
* Simple Average
* Weighted Average

Students are automatically sorted from lowest to highest weighted score, making it easy to identify students requiring additional support.

---

## ▶️ Installation

### Clone the Repository

```bash
git clone https://github.com/shivansh291/GradeMatrix.git
cd GradeMatrix
```

### Install Dependencies

```bash
pip install pandas numpy customtkinter
```

### Run the Application

```bash
python script.py
```

---

## 🎯 Educational Impact

GradeMatrix helps schools:

* Evaluate students more fairly
* Recognize improvement trends
* Identify struggling students quickly
* Make data-driven academic decisions
* Reduce teacher workload through automation

---

## Future Improvements

* Excel (.xlsx) support
* Performance graphs and visualizations
* Student trend analytics
* PDF report generation
* Cloud database integration
* Machine learning-based performance prediction

---

## Project Team

Developed as an Intellectual Property (IP) Project to demonstrate the practical application of:

* Linear Algebra
* Matrix Multiplication
* Data Analysis
* Python Programming
* User Interface Design

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.
