def relation_to_luke(name):
    remember = {
        "Darth Vader": "father",
        "Leia": "sister",
        "Han": "brother in law",
        "R2D2": "Droid"
    }

    for person,rlshp in remember.items():
        if name == person:
            luke_remember = "Luke, I am your " + rlshp + "."

    return luke_remember
print(relation_to_luke("Leia"))