# CLASS CREATION

class SportsWriting():
    def __init__(self, language="", headline="", facts_5w1h="", subtype="", individual_event=False, posting=False, experience=False):
        self.__language = language
        self.headline = headline
        self.__facts_5w1h = facts_5w1h
        self.__subtype = subtype
        self.individual_event = individual_event
        self.posting = posting
        self.__experience = experience

    def write(self):
        self.headline = input("Enter the headline of the sports article: ")
        print("")
        self.__facts_5w1h = input("Enter the 5W1H facts (Who, What, When, Where, Why, How): ")
        print("")

        print(f"Sports Article Headline: {self.headline}")
        print(f"5W1H Facts: {self.__facts_5w1h}")

    def revise(self):
        revise = input("Do you want to revise the sports article? (yes/no): ").lower()
        if revise == "yes":
            change_headline = input("Do you want to revise the headline? (yes/no): ").lower()
            if change_headline == "yes":
                self.headline = input("Enter the revised headline of the sports article: ")
                print("")
            elif change_headline == "no":
                self.headline = self.headline
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
                return self.revise()
            change_facts_5w1h = input("Do you want to revise the 5W1H facts? (yes/no): ").lower()
            if change_facts_5w1h == "yes":
                self.__facts_5w1h = input("Enter the revised 5W1H facts (Who, What, When, Where, Why, How): ")
                print("")
            elif change_facts_5w1h == "no":
                self.__facts_5w1h = self.__facts_5w1h
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
                return self.revise()
            change_subtype = input("Do you want to revise the subtype? (yes/no): ").lower()
            if change_subtype == "yes":
                self.__subtype = input("Enter the revised subtype of the sports article: ")
                print("")
            elif change_subtype == "no":
                self.__subtype = self.__subtype
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
                return self.revise()

            print(f"Revised Sports Article Headline: {self.headline}")
            print(f"Revised 5W1H Facts: {self.__facts_5w1h}")
            print(f"Revised Subtype: {self.__subtype}")
        else:
            print("No revisions made.")

        return "Revision complete!"

    def watch(self, sport_name):
        print(f"Watching the {sport_name} event for the article.")
        print("")

# PROGRAM FUNCTIONS

def create_sports_article():
    article = SportsWriting()
    language = input("Before we begin, what language are you writing the article in? ")
    article.__language = language
    print("")
    subtype = input("What kind of sports article are you writing? ")
    article.__subtype = subtype
    print("")
    experience = input("Do you have experience writing sports articles in this language? (yes/no): ").lower()
    if experience == "yes":
        article.__experience = True
    elif experience == "no":
        article.__experience = False
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        return create_sports_article()
    print("")
    individual_event = input("Are you an individual sports writer or part of collaborative publishing> (individual/collab): ").lower()
    if individual_event == "individual":
        article.individual_event = True
    elif individual_event == "collab":
        article.individual_event = False
    else:
        print("Invalid input. Please enter 'individual' or 'collab'.")
        return create_sports_article()
    print("")
    posting = input("Will this article be posted? (yes/no): ").lower()
    if posting == "yes":
        article.posting = True
    elif posting == "no":
         article.posting = False
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        return create_sports_article()
    print("")
    return SportsWriting(language=language, subtype=subtype, individual_event=article.individual_event, posting=article.posting, experience=article.__experience)

def display_article_info(article):
    print(f"Headline: {article.headline}")
    print(f"5W1H Facts: {article._SportsWriting__facts_5w1h}")
    print(f"Subtype: {article._SportsWriting__subtype}")

# EXECUTION

writer_name=input("Enter your name: ")
print("")

# CREATING OBJECT 1

choice = input(f"Welcome, {writer_name}! Would you like to write a sports article? (yes/no): ").lower()
print("")
if choice == "yes":
    article1 = create_sports_article()
    article1.watch(input("Enter the sport name you are covering: "))
    article1.write()
    article1.revise()
    print("Sports article information obtained successfully!")
    print("")

    # CREATING OBJECT 2

    choice2 = input("Would you like to write another sports article? (yes/no): ").lower()
    print("")
    if choice2 == "yes":
        article2 = create_sports_article()
        article2.watch(input("Enter the sport name you are covering: "))
        article2.write()
        article2.revise()
        print("Sports article information obtained successfully!")
        print("")

        # DISPLAYING OBJECT INFORMATION
    
        display_article_info(article1)
        print("")
        display_article_info(article2)
        print("")

        # PERFORMING METHODS ON ARTICLE1

        print("\nPerforming methods on Sports Article 1:")
        article1.revise()
        print("")

        display_article_info(article1)
        print("")
        display_article_info(article2)
        print("")
        print("Great articles!")

    elif choice2 == "no":
        display_article_info(article1)
        print("Article not created. Thank you!")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        exit()
elif choice == "no":
    print("Article not created. Thank you!")
else:
    print("Invalid input. Please enter 'yes' or 'no'.")
    exit()