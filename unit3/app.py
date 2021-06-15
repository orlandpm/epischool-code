from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    title = "The Haunted House"
    
    text = """It is a dark and cold night and the moon is full. You walk up to the haunted house.  
    As you approach the door, it creaks open and a chill runs down your spine!"""

    choices = [
        ('enter_house',"Go inside"),
        ('run_away',"Run away as fast as you can!!!")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/inside")
def enter_house():
    title = "You go inside..."
    
    text = """... and the door slams shut behind you!  And then -- absolute silence.  It is so quiet you can hear the 
    sound of your own heart beating.  A dusty wooden staircase leads up to the second floor.  Through a tangle of cobwebs
    you can see the faint, flickering light of a small candle."""

    choices = [
        ('up_stairs',"Go up the stairs"),
        ('run_away',"Try to escape out the front door")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/escape")
def run_away():
    title = "You run away!"
    
    text = """You bolt away from the house to safety.  You hear the sound of a sinister voice cackling madly behind you."""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/stairs")
def up_stairs():
    title = "Look out!"
    
    text = """As you climb the stairs, a sea of spiders rains down on you from the cobwebs.  You feel the excruciating bites of 
    ten thousand tiny fangs as they eat you alive."""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)
