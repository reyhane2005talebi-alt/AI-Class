scores = {"Ali": 18, "Sara": 20, "Reza": 9, "Mina": 14, "Omid": 11.5}

passed = []
sum-score = 0

for name, score in scores.items():

    if score >= 17:
        rank = "عالی"
    elif score >= 14:
        rank = "خوب"
    elif score >= 10:
        rank = "قبول"
    else:
        rank = "مردود"

    print(f"{name}: {score} = {rank}")

    if score >= 10:
        passed.append(name)

    sum-score += score

average = sum_score / len(scores)

top_student = max(scores)#این سوال بپرسم از استاد

print("قبول‌شده‌ها:", passed)
print("میانگین کلاس:", round(average, 2))
print("نفر اول:", top_student)
