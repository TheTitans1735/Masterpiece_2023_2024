#!/usr/bin/env pybricks-micropython

from robot import Robot
from pybricks.parameters import Button, Color, Stop
from pybricks.tools import StopWatch, wait
import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print('Function {}{} {} Took {} seconds'.format(func.__name__, args, kwargs, total_time))
        ilan.write("Run time: {} sec.".format(round(total_time, 1)))
        return result
    return timeit_wrapper


ilan = Robot() 

##### Center Run #####

@timeit
def program_test():
    debug = False
    ilan.pid_gyro(47,250)
    ilan.drive_by_seconds(100,1)
    wait(1)
    ilan.wait_for_button("Drive back", debug)
    ilan.pid_gyro(53,250,Forward_Is_True= False,precise_distance= False)

@timeit
def M01_3D_Movie():

    """מבצע את משימה M01"""

    #  ביצוע משימה M01
    ilan.pid_gyro(19,250)
    ilan.turn(50)
    ilan.turn(-45)
    ilan.pid_gyro(19,300,False,precise_distance=False)

@timeit
def M08_Dolly_Camera():
    """מבצע את משימות M08"""
    ilan.pid_gyro(43.8,320,Kp=0, precise_distance=False)
    ilan.wait_for_button(debug=False,text="Drive Back")
    ilan.pid_gyro(43.8,300,False,Kp=0, precise_distance=False)

@timeit
def run_3():
    pass


@timeit
def M02_switch_scenery():

    """מבצע משימה M02"""

    ilan.pid_gyro(50,300,precise_distance=False)
    ilan.turn(-75)
    for i in range (2):
        ilan.drive_by_seconds(100,1)
        ilan.drive_by_seconds(-75,1)
    ilan.turn(65)
    ilan.drive_by_seconds(-500,1.5)

@timeit
def run_5(): 

    """ביצוע משימה M03"""

    pass
    

TEXT_MENU = """Choose Run: 
  < - Left run 
  > - Right AP 
  O - Center run 
  V - Down run 
  ^ - Up run"""



##### פונקציה להפעלת הריצות באמצעות כפתורי הרובוט #####

def running ():
    
    """!! One Function To Rule Them All !!"""

    ilan.beep()
        # ilan.write(TEXT_MENU)
       
    Runs = [
        ("1 - 3D movie", M01_3D_Movie),
        ("program test", program_test),
        ("3 - Dolly Camera", M08_Dolly_Camera),
        ("4 - switch scenery", M02_switch_scenery),
        ("5 - ", run_5),
    ]

    current_run = 0
    ilan.write(Runs[current_run][0])
    elsapsed_time = StopWatch()

    while True:

        try:
        

            if (Button.UP in ilan.ev3.buttons.pressed()):
                current_run += 1

                if current_run >= len(Runs):
                    current_run = 0
                    
                ilan.write(Runs[current_run][0])

                wait(300)

            if (Button.DOWN in ilan.ev3.buttons.pressed()):
                current_run -= 1

                if current_run < 0:
                    current_run = len(Runs) - 1
            
                ilan.write(Runs[current_run][0])
                
                wait(300)

            if Button.CENTER in ilan.ev3.buttons.pressed():

                # if current_run == 0:
                elsapsed_time.reset()

                Runs[current_run][1]()
            
                # current_run += 1

                if current_run >= len(Runs):
                    current_run = 0

                ilan.write("Elapsed: {} s \n{}".format(round(elsapsed_time.time()/1000.0, 1), Runs[current_run][0]))
        except Exception as EX :
            print(str(EX))
            wait(1500)
            
            
running()
