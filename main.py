import turtle
import pandas

screen = turtle.Screen()
screen.title("Guess india state")
map_img = "india_states.gif"
screen.addshape(map_img)
turtle.shape(map_img)

state_df = pandas.read_csv("state_cords.csv")
guessed_states = []
user_input = screen.textinput(f"Guess states {len(guessed_states)}/{state_df.size}", "Please type the name of state in india`")

# Function to get the coordinates of a click
# def get_coordinates(x, y):
#     print("Clicked at coordinates (x, y):", x, y)
#
# # Register the function to be called on click events
# screen.onclick(get_coordinates)

turtle.mainloop()