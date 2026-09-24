# CLASS FOR RELATIONSHIPS

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

# PARENT CLASS

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

    def display(self):
        print(f"Sports Article Headline: {self.headline}")
        print(f"5W1H Facts: {self.__facts_5w1h}")
        print(f"Subtype: {self.__subtype}")
        print(f"Individual Event: {self.individual_event}")
        print(f"Posting: {self.posting}")
        print(f"Experience: {self.__experience}")

# CHILD CLASS

class SportsFeatureWriting(SportsWriting):
    def __init__(self, language="", headline="", facts_5w1h="", subtype="", individual_event=False, posting=False, experience=False, theme="", narrative=""):
        super().__init__(language, headline, facts_5w1h, subtype, individual_event, posting, experience)
        self.theme = theme
        self.__narrative = narrative

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
        super().write()
        self.theme = input("Enter the theme of the sports feature article: ")
        print("")
        self.__narrative = input("Enter the narrative of the sports feature article: ")
        print("")

        print(f"Sports Feature Article Theme: {self.theme}")
        print(f"Narrative: {self.__narrative}")

    def revise(self):
        super().revise()
        revise_theme = input("Do you want to revise the theme? (yes/no): ").lower()
        if revise_theme == "yes":
            self.theme = input("Enter the revised theme of the sports feature article: ")
            print("")
        elif revise_theme == "no":
            self.theme = self.theme
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            return self.revise()

        revise_narrative = input("Do you want to revise the narrative? (yes/no): ").lower()
        if revise_narrative == "yes":
            self.__narrative = input("Enter the revised narrative of the sports feature article: ")
            print("")
        elif revise_narrative == "no":
            self.__narrative = self.__narrative
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            return self.revise()

        print(f"Revised Sports Feature Article Theme: {self.theme}")
        print(f"Revised Narrative: {self.__narrative}")

        return "Revision complete!"

    def interview(self, athlete_name):
        print(f"Conducting an interview with {athlete_name} for the sports feature article.")
        print("")

    def display(self):
        super().display()
        print(f"Sports Feature Article Theme: {self.theme}")
        print(f"Narrative: {self.__narrative}")

# EXECUTION

print("Parent Class")
Article1 = SportsWriting(language="English", headline="#SPORTS | School Intramurals Begin", facts_5w1h="Who: Students of PSHS-BRC, What: SY 2026-2027 Intramurals, When: Last Week of September, Where: PSHS-BRC Gymnasium, Why: Event, How: Many Matches", subtype="Sports News", individual_event=True, posting=True, experience=True)
display1 = Article1.display()
print("")

print("Child Class")
Article2 = SportsFeatureWriting(language="English", headline="#SPORTS | School Intramurals Begin", facts_5w1h="Who: Students of PSHS-BRC, What: SY 2026-2027 Intramurals, When: Last Week of September, Where: PSHS-BRC Gymnasium, Why: Event, How: Many Matches", subtype="Sports News", individual_event=True, posting=True, experience=True, theme="Teamwork", narrative="Exposition: Start of Intramurals, Rising Action: Teamwork, Climax: Teamwork, Falling Action: Teamwork, Resolution: End of Intramurals")
display2 = Article2.display()
print("")

print("Inheritance")
# Article2 (Child Object) accesses PARENT attributes directly:
print(f"Parent attribute (headline) accessed via Child Object: {Article2.headline}")
print(f"Parent attribute (posting) accessed via Child Object: {Article2.posting}")

#Article2 can run both PARENT and CHILD methods:
print("Calling Parent Method from Child Object:")
Article2.watch("Basketball")  # Method inherited from SportsWriting
print("Calling Child-Specific Method:")
Article2.interview("BRC Student")  # Method inherited from SportsFeatureWriting

# AGGREGATION

print("Aggregation")
Sports1 = Sports(sport_name="Basketball", event_type="Elimination", sport_individual=False)
Sports2 = Sports(sport_name="Badminton", event_type="Elimination", sport_individual=True)
Sports3 = Sports(sport_name="Volleyball", event_type="Elimination", sport_individual=False)

print("Before Aggregation")
print("")
display2 = Sports1.display()
print("")
display3 = Sports2.display()
print("")
display4 = Sports3.display()
print("")
display5 = Article2.display_covered_sports()
print("")

# AGGREGATING

Article2.add_sport(Sports1)
Article2.add_sport(Sports2)
Article2.add_sport(Sports3)

print("After Aggregation")
print("")
print(f"{Article2.headline}")
display6 = Article2.display_covered_sports()