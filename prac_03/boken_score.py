"""
CP1404/CP5632 - Practical - Suggested Solution
Fixed program to determine score status, with function
"""
def main():
    score = float(input("Enter score: "))
    print(determine_score(score))


def determine_score(score):
   if score < 0 or score > 100:
      return "Invalid score"
   elif score >= 90:
      return "Excellent"
   elif score >= 50:
      return "Passable"
   else:
      return "Bad"

main()