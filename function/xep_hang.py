def grade(score):
    if score>=0.9: return 'A'
    elif score>=0.8: return 'B'
    elif score>=0.7: return 'c'
    elif score>=0.6: return 'D'
    elif score>=0.5: return 'E'
    else: return 'F'
while True:
    try:
        score=raw_input("Enter score: ")
        if score=='': break
        score = float(score)
        if 1 >= score >= 0:
            print 'Garde:', grade(score)
            continue
        print 'Bad Score!!!'
    except:
        print 'Please enter number (0 <= score <= 1.0)!!!'