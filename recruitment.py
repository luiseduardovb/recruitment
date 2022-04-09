def get_skills():
    # Add at least 3 random skills for the user to select from
    return ["Python", "Javascript", "Typescript"]


def show_skills(skills):
    # Pretty print skills to the user
    # Write your code here
    for count,skill in enumerate(skills, start=1):
        print(count,skill)


def get_user_skills(skills):
    # Show the available skills and have user pick from them
    # Write your code here
    print('\n')
    show_skills(skills)
    print('\n')

    skill_one_option = input("Choose a skill from above by entering its number: ")
    skill_two_option = input("Choose another skill from above by entering its number: ")

    skill_one= skills[int(skill_one_option) - 1]
    skill_two = skills[int(skill_two_option) - 1]

    skills = [skill_one, skill_two]

    return skills



def get_user_cv(skills):
    # Get the users CV from their inputs
    # Write your code here
    cv = {}
    print("Welcome to the special recruitment program, please answer the following questions: ")
    name = input("What's your name?: ")
    age = input("How old are you?: " )
    years_of_experience = input("How many years of experience do you have?: ")

    cv['name'] = name
    cv['age'] = age
    cv['experience'] = years_of_experience
    cv['skills'] = get_user_skills(skills)

    return cv



def check_acceptance(cv, desired_skill):
    # Check if the cv is acceptable or not and return a boolean based on that
    # Write your code here
    age = int(cv['age'])
    years_of_experience = int(cv['experience'])



    has_age_range = age >= 25 and age <= 40
    has_enough_experience = years_of_experience >= 3
    has_desired_skill = desired_skill in cv['skills']

    if(has_age_range and has_enough_experience and has_desired_skill):
        return True
    else:
        return False 


def main():
    # Write your main logic here by combining the functions above into the
    # desired outcome
    skills = get_skills()
    cv = get_user_cv(skills)
    desired_skill = skills[2]

    candidate = cv['name']
    meets_criteria = check_acceptance(cv,desired_skill)

    if(meets_criteria):
        print(f"You have been accepted, {candidate}.")
    else:
        print(f"Your application has been rejected, {candidate}.")




if __name__ == "__main__":
    main()
