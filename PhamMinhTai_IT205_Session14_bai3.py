student_records = [
    {
        "student_id": "SV001",
        "name": "Nguyễn Văn A",
        "math": 8.5,
        "physics": 7.0,
        "chemistry": 9.0
    },
    {
        "student_id": "SV002",
        "name": "Trần Thị B",
        "math": 4.0,
        "physics": 5.5,
        "chemistry": 5.0
    },
    {
        "student_id": "SV003",
        "name": "Lê Văn C",
        "math": 9.5,
        "physics": 9.0,
        "chemistry": 8.5
    }
]


def calculate_average(student):
    return (student["math"] + student["physics"] + student["chemistry"]) / 3


def generate_report(records):
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    total = len(records)
    passed = 0
    failed = 0

    for student in records:
        avg = calculate_average(student)

        if avg >= 5:
            passed += 1
        else:
            failed += 1

    passed_percent = (passed / total) * 100
    failed_percent = (failed / total) * 100

    print("\n--- BÁO CÁO HỌC VỤ ---")
    print("Tổng số sinh viên:", total)
    print(f"Số lượng qua môn (ĐTB >= 5.0): {passed} sinh viên (Chiếm {passed_percent:.2f}%)")
    print(f"Số lượng trượt (ĐTB < 5.0): {failed} sinh viên (Chiếm {failed_percent:.2f}%)")
    print("----------------------")


generate_report(student_records)