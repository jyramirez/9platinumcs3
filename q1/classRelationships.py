# CLASS CREATION

class Sports():
    def __init__(self, sport_name="", event_type="", sport_individual=False):
        self.sport_name = sport_name
        self.event_type = event_type
        self.sport_individual = sport_individual

    def play(self):
        print(f"Playing {self.sport_name}.")

    def practice(self):
        print(f"Practicing {self.sport_name}.")

    def display(self):
        print(f"Sport Name: {self.sport_name}")
        print(f"Event Type: {self.event_type}")
        print(f"Individual Sport: {self.sport_individual}")

class SportsWriting():
    def __init__(self, language="", headline="", facts_5w1h="", subtype="", sport=None, individual_event=False, posting=False, experience=False):
        self.__language = language
        self.headline = headline
        self.__facts_5w1h = facts_5w1h
        self.__subtype = subtype
        self.individual_event = individual_event
        self.posting = posting
        self.__experience = experience

        self.__covered_sport = []

    def add_sport(self, sport):
            if isinstance(sport, Sports):
                self.__covered_sport.append(sport)
                print(f"Added {sport.sport_name} to the covered sports.")
            else:
                print("Invalid sport. Please provide a valid Sports object.")

    def display_covered_sports(self):
            if self.__covered_sport:
                print("Covered Sports:")
                for sport in self.__covered_sport:
                    print(f"- {sport.sport_name}")
            else:
                print("No sports covered yet.")

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

    def display(self):
        print(f"Sports Article Headline: {self.headline}")
        print(f"5W1H Facts: {self.__facts_5w1h}")
        print(f"Subtype: {self.__subtype}")
        print(f"Individual Event: {self.individual_event}")
        print(f"Posting: {self.posting}")
        print(f"Experience: {self.__experience}")

#CREATING OBJECTS BEFORE RELATION

print("BEFORE RELATIONSHIP")
print("")

Article1 = SportsWriting(language="English", headline="#SPORTS | School Intramurals Begin", facts_5w1h="Who: Students of PSHS-BRC, What: SY 2026-2027 Intramurals, When: Last Week of September, Where: PSHS-BRC Gymnasium, Why: Event, How: Many Matches", subtype="Sports News", individual_event=True, posting=True, experience=True)
display1 = Article1.display()
print("")

Sports1 = Sports(sport_name="Basketball", event_type="Elimination", sport_individual=False)
Sports2 = Sports(sport_name="Badminton", event_type="Elimination", sport_individual=True)
Sports3 = Sports(sport_name="Volleyball", event_type="Elimination", sport_individual=False)
display2 = Sports1.display()
print("")
display3 = Sports2.display()
print("")
display4 = Sports3.display()
print("")
display5 = Article1.display_covered_sports()
print("")

# RELATING OBJECTS

print("BUILDING RELATIONSHIP")
print("")

Article1.add_sport(Sports1)
Article1.add_sport(Sports2)
Article1.add_sport(Sports3)

print("")
print("AFTER RELATIONSHIP")
print("")

print(f"{Article1.headline}")
display6 = Article1.display_covered_sports()


