import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"  # loads image
screen.addshape(image)  # loads a new image as a new shape of the turtle
turtle.shape(image)     # change turtle shape into an image file

screen.tracer(0)

data = pandas.read_csv("50_states.csv")     # loads and reads csv data
states_list = data["state"].to_list()   # converts state column into a list
turtle_writing = turtle.Turtle()    # creates a new turtle object for writing names of states
turtle_writing.penup()
turtle_writing.hideturtle()

correct_guesses = []    # list that keeps correctly guessed states


while len(correct_guesses) < 50:   # the game runs until all states are guessed
    answer_state = (screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state's name?")).title()     # creates popup window for input, counts guessed states in the title, capitalizes first letter of each word of an input

    if answer_state == "Exit":  # to exit the game
        break
    if answer_state in states_list and answer_state not in correct_guesses:     # if users input is correct and is not guessed already
        answer_row = data[data.state == answer_state]  # gets hold of the row of the state
        x = int(answer_row.x)  # gets hold of the x coordinate of the state
        y = int(answer_row.y)  # gets hold of the y coordinate of the state

        turtle_writing.setposition(x, y)    # set turtle's position to x, y coordinates of the state
        turtle_writing.write(answer_state)  # write state's name
        correct_guesses.append(answer_state)    # appends correct guess to the list

# create list with missing states
missing_states = [state for state in states_list if state not in correct_guesses]     # adds state to missing states list if its not among guessed states

# writes missing states on the map
for state in missing_states:    # each of the missing states
    answer_row = data[data.state == state]  # gets hold of the row of the state
    x = int(answer_row.x)  # gets hold of the x coordinate of the state
    y = int(answer_row.y)  # gets hold of the y coordinate of the state
    turtle_writing.color("red")     # write in red
    turtle_writing.setposition(x, y)  # set turtle's position to x, y coordinates of the state
    turtle_writing.write(state)  # write state's name
screen.update()     # updates screen after the loop runs, missing state's names appear all together and not one by one

new_data = pandas.DataFrame(missing_states)     # creates dataframe
new_data.to_csv("states_to_learn.csv")  # creates csv

screen.exitonclick()
