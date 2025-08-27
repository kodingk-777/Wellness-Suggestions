import random

#What you need today (You can add as many as you want :))

wellness_suggestions = [
    "Rest earlier than you think you need; tomorrow will thank you.",
    "Spend less time proving, more time simply being.",
    "Give yourself the grace to pause before responding.",
    "Some doors close gently; don’t try to reopen them tonight.",
    "You don’t need to solve everything at once — let some mysteries stay unsolved.",
    "Don’t mistake constant motion for real progress.",
    "Protect your energy as carefully as your time.",
    "Allow silence to speak louder than explanation.",
    "Not every weight is yours to carry — set one down.",
    "Honor the difference between loneliness and solitude.",
    "Let endings be endings; not every thread needs tying today.",
    "Tend to your body as you would to something sacred.",
    "Remember: sometimes rest is the most productive choice.",
    "Choose gentleness over urgency — with yourself first.",
    "Your worth is not measured by how much you accomplish in a day.",
    "Resist the pull to compare your path with another’s.",
    "Don’t overstay where your spirit has already left.",
    "The answer you seek is not online — it is already within you.",
    "Don’t rush what only time can ripen.",
    "Speak less, listen more — especially to yourself.",
    "Your presence is enough; you don’t always need to perform.",
    "Forgive the version of you who didn’t know better.",
    "Stop rehearsing conversations that may never happen.",
    "Don’t postpone joy until everything is perfect.",
    "Make peace with the unfinished — it teaches patience.",
    "Not every battle is yours; conserve your strength.",
    "When in doubt, choose simplicity over spectacle.",
    "Rest is not laziness; it is preparation for clarity.",
    "Your future self is already grateful for today’s small kindnesses.",
    "Release the need to explain yourself to those who won’t understand.",
    "Some people are lessons, not lifetimes.",
    "Focus on direction, not speed.",
    "Let quiet routines anchor you when the world feels uncertain.",
    "You don’t need to answer every question right away.",
    "Trust the pauses as much as the forward steps.",
    "Your softness is not weakness — it is wisdom.",
    "Be careful not to confuse busyness with meaning.",
    "Choose one truth to hold onto, and let the rest pass.",
    "Take yourself out of the center of the storm; observe instead.",
    "Nourish your spirit before you nourish your schedule.",
    "Don’t give away your peace for someone else’s chaos.",
    "Allow yourself to outgrow what once fit.",
    "Look backward only long enough to see how far you’ve come.",
    "The most important 'yes' is the one you give to yourself.",
    "Don’t let urgency steal the beauty of slowness.",
    "Some things are solved by patience, not effort.",
    "Take care not to abandon yourself while caring for others.",
    "You don’t need to fill every silence — let it hold you.",
    "End today gently; tomorrow will carry its own weight."
]

user_name = input("Enter your name: ")
user_star_sign = input("Enter your star sign: ")

print(f"Hello, {user_name}! Pick a day and month (1-31) and I'll tell you what you need that day: ")

day = int(input("Day: "))
month = (input("Month: "))

wellness_suggestions = wellness_suggestions[day % len(wellness_suggestions)]

print(f"\n{user_name}, as a {user_star_sign}, on {day} of {month}:")
print(f"✨ {wellness_suggestions}")