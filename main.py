def gradingStudent(grades: list) -> list:
    # first initialize a new list
    new_scores = []
    for score in grades[1:]:
        # check if each score is above 38 and it has a remainder when divided by 5
        if score >= 38 and not score % 5 == 0:
          # get the base value of the score
            five_divisible = int(score / 5)
            if ((five_divisible+1) * 5) - score < 3:
                new_scores.append((five_divisible+1) * 5)
            else:
                new_scores.append(score)
        else:
            new_scores.append(score)
    return (new_scores)
