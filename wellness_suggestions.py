# wellness_suggestions.py  (or rename to app.py)
import streamlit as st
import random
import datetime

# --- data ---
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

# --- UI ---
st.set_page_config(page_title="Useless Wellness Oracle", page_icon="✨", layout="centered")
st.title("✨ Useless Wellness Oracle ✨")
st.caption("useless guidance, one day at a time")

colA, colB = st.columns(2)
with colA:
    user_name = st.text_input("Your name", "")
with colB:
    user_star_sign = st.text_input("Your star sign", "")

col1, col2 = st.columns(2)
today = datetime.date.today()
with col1:
    day = st.number_input("Day", min_value=1, max_value=31, value=today.day, step=1)
with col2:
    month = st.selectbox(
        "Month",
        ["January","February","March","April","May","June",
         "July","August","September","October","November","December"],
        index=today.month - 1
    )

if st.button("Reveal suggestion"):
    # deterministic by date (so same day → same suggestion), but you can swap to random.choice
    index = int(day) % len(wellness_suggestions)
    suggestion = wellness_suggestions[index]

    st.success(f"{user_name or 'Friend'}, as a {user_star_sign or 'stargazer'}, on {int(day)} of {month}:")
    st.write(f"**{suggestion}**")
