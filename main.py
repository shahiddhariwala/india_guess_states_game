import turtle
import pandas

screen = turtle.Screen()
screen.title("Guess indian state")
map_img = "india_states.gif"
screen.addshape(map_img)
turtle.shape(map_img)

state_df = pandas.read_csv("state_cords.csv")
guessed_states = []
states_name = list(state_df.state)

while len(guessed_states) != state_df["state"].count():
    user_input = screen.textinput(f"Guess states {len(guessed_states)}/{state_df.state.count()}",
                                  "Please type the name of state in india`").title()
    if user_input == "Exit":
        break

    if user_input in states_name:
        state_data = state_df[state_df.state == user_input]
        state_turtle = turtle.Turtle()
        state_turtle.penup()
        state_turtle.color("red")
        state_turtle.goto(int(state_data.x), int(state_data.y))
        state_turtle.hideturtle()
        state_turtle.write(f"{user_input}", False, "center", ("Fira-sans", 18, "normal"))
        guessed_states.append(user_input)

with open("missed_state.txt", "w") as data:
    for state in states_name:
        if state not in guessed_states:
            data.writelines(f"{state}\nMis")

# Function to get the coordinates of a click
# def get_coordinates(x, y):
#     print("Clicked at coordinates (x, y):", x, y)
#
# # Register the function to be called on click events
# screen.onclick(get_coordinates)

turtle.mainloop()