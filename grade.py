
def main():
    score = int(input("Score: "))
    print(f"Grade: {grade(score)}")

def grade(score):
    if score >= 90 and score <= 100:
        return "A"
    elif score >= 80 and score < 90:
        return "B"
    elif score >= 70 and score < 80:
        return "C"
    elif score >= 60 and score < 70:
        return "D"
    else:
        return "F"


main()
    



    


