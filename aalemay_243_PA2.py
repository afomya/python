#-------------------------------------------------------------------------------
# Name: Afomya Sisay Alemayehu
# Programming Assignment 2
# Due Date: 02/21/2022
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: (https://www.w3schools.com/python/default.asp)
#-------------------------------------------------------------------------------
# Comments and assumptions: A note to the grader as to any problems or
# uncompleted aspects of the assignment, as well as any assumptions about the
# meaning of the specification.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------

# assignment 1: figuring out color based on the wavelength
# use def spectral_color(wavelength)
# I used the graph on the assignment instructions and wikipedia for the wavelength of
# infrared and ultraviolet

def spectral_color(wavelength):
    if wavelength > 100 and wavelength <=379:  
        color_name = "ultraviolet"
    elif wavelength >= 380 and wavelength <= 449:
        color_name = "violet"
    elif wavelength >= 450 and wavelength <= 484:
        color_name = "blue"
    elif wavelength >= 485 and wavelength <= 499:
        color_name = "cyan"
    elif wavelength >= 500 and wavelength <= 564:
        color_name = "green"
    elif wavelength >= 565 and wavelength <= 589:
        color_name = "yellow"
    elif wavelength >= 590 and wavelength <= 624:
        color_name = "orange"
    elif wavelength >= 625 and wavelength <= 749:
        color_name = "red"
    elif wavelength >= 750 and wavelength <= 1000000:
        color_name = "infrared"
    else:
        color_name = "Error"
    return color_name


# assignment 2: calculate the rate of change of prices as the bad broker would do
# if the rate of change is up  50 percent, Buy
# if the rate of change is below by 50 percent, Hold
# if the rate of change is not changing much, range is within 50, Sell
# return the stock fate

def bad_broker(price, prev_price):
    rate_of_change = (price - prev_price) / prev_price
    # rate_of_change = round(rate_of_change, 2)
    if rate_of_change > 0.5:
        stock_fate = "BUY"
    elif rate_of_change < -0.5:
        stock_fate = "HOLD"
    else:
        stock_fate = "SELL"
    return stock_fate


# Turn on the vacuum if the dirt sensor detects dirt
# When there is no dirt detected, move forward as long as there is a wall to the
# left side and no wall in front.
# If there is a wall in front (blocking the robot) the robot should turn
# Stop if there are no walls or dirt detected
# side_sensor: A string. can be either "wall" or "clear"
# front_sensor: A string. can be either "wall" or "clear"
# dirt_sensor: A string. can be either "dirt" or "clear"
# Return value: one of four strings, "stop" or "turn"or "vacuum" or "forward"

# use def robot_actions(side_sensor, front_sensor, dirt_sensor):

def robot_actions(side_sensor, front_sensor, dirt_sensor):
    action1 = side_sensor == "wall" and front_sensor == "clear"
    if dirt_sensor == "dirt" and dirt_sensor != "clear":
        instruction = "vacuum"
    elif front_sensor == "wall":
        instruction = "turn"
    elif side_sensor == "wall" and front_sensor == "clear":
        instruction = "forward"
    else:
        instruction = "stop"
    return instruction

