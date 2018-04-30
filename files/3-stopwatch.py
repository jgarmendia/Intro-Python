# template for "Stopwatch: The Game"
import simplegui

# define global variables
time = 0
width = 300
height = 200
attempts = 0
success = 0
run = False


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    a = (t // 600)
    b = ((t // 10) % 60) // 10
    c = ((t // 10) % 60) % 10
    d = (t % 10)
    """ format a:bc.d"""
    t = str(a) + ":" + str(b) + str(c) + "." + str(d)
    return t
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global run
    """Start the game"""
    timer.start()
    run = True


    
def stop():
    global run, success, attempts
    """Stop the game"""
    timer.stop()
    if (time % 10) == 0 and run == True:
        success += 1
        attempts += 1
        run = False
    elif run == True:
        attempts += 1
        run = False
        
      
def reset():
    """Stop and reset the game"""
    global time, attempts, success
    timer.stop()
    time = 0
    attempts = 0
    success = 0
    run = True
    

# define event handler for timer with 0.1 sec interval
def timer():
    global time
    time += 1
    print time

    

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), [width // 2, height // 2], 30, "White")
    canvas.draw_text(str(attempts) + "/" + str(success), [250, 20], 20, "Red")

          
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", width, height)
label = frame.add_label("Stop time whenever not decimal for points!")
timer = simplegui.create_timer(100, timer)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

# register event handlers
frame.set_draw_handler(draw)


# start frame
frame.start()

# Please remember to review the grading rubric


  