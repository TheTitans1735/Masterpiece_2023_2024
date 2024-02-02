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

# @timeit
# def program_test():
#     debug = False
#     ilan.pid_gyro(47,250)
#     ilan.drive_by_seconds(100,1)
#     wait(1)
#     ilan.wait_for_button("Drive back", debug)
#     ilan.pid_gyro(53,250,Forward_Is_True= False,precise_distance= False)

@timeit
def M01_3D_Movie():

    """מבצע את משימה M01"""

    #  ביצוע משימה M01
    ilan.pid_gyro(19,250)
    ilan.turn(30)
    ilan.turn(-45)
    ilan.pid_gyro(19,300,False,precise_distance=False)

@timeit
def M08_Dolly_Camera():
    """מבצע את משימות M08"""
    ilan.pid_gyro(18.5,250,Kp=0, precise_distance=False)
    wait(500)
    ilan.drive_by_seconds(320,1)
    wait(500)
    ilan.wait_for_button(debug=False,text="Drive Back")
    ilan.speed_formula(48.8,300,Forward_Is_True=False,Kp=0)

@timeit
def M10_Sound_Mixr():
    """מבצע את משימות M10"""
    debug = False
    ilan.speed_formula(45,400)
    #ilan.drive_by_seconds(400,2)
    # ilan.wait_for_button(text="df")
    ilan.turn(14)
    ilan.speed_formula(40,400,False)
    # ilan.drive_by_seconds(400,0.8)
    ilan.turn(-80)
    ilan.speed_formula(12,450)
    #ilan.wait_for_button(text="turn")
    ilan.turn(28)
    ilan.drive_by_seconds(-200,1)

@timeit
def flower():
# """מבצע משימות M14"""
    
    precise_distance=False
    # ilan.pid_gyro(61,300,precise_distance=False)
    ilan.speed_formula(53,400)
    # ilan.wait_for_button("a")
    ilan.turn(-28)
    # ilan.wait_for_button("after turn",debug=True)
    ilan.pid_gyro(49,320)
    # ilan.turn(40)
    # ilan.wait_for_button(text="g")
    ilan.speed_formula(16,300,Forward_Is_True=False)
    # ilan.wait_for_button(text="g")
    # ilan.pid_gyro(-9)
    ilan.turn(30)
    ilan.pid_gyro(-10,200)
    ilan.turn(90)
    ilan.pid_gyro(-15,200)
    ilan.turn(-45)
    ilan.pid_gyro(20,200)


@timeit
def M02_switch_scenery():

    """מבצע משימות M02 M03"""

    ilan.turn(-3)
    # ilan.wait_for_button(text="eeee")
    #ilan.pid_gyro(56,300,precise_distance=False)
    ilan.pid_gyro(59,250)
    ilan.turn(-70,200)
    ilan.stop_on_line
    ilan.drive_by_seconds(100,1.2)
    ilan.drive_by_seconds(-75,1)
    ilan.drive_by_seconds(100,1)
    ilan.drive_by_seconds(-75,1)
    ilan.wait_for_button(text="turn")
    ilan.turn(135,200)
    # ilan.drive_by_seconds(-500,2)
    ilan.wait_for_button(text="drive forword")
    ilan.pid_gyro(39,250)
    ilan.wait_for_button(text="turn")
    ilan.turn(-90,200)
    ilan.pid_gyro(5,250)

@timeit
def Virtual_reality_artist_Creation_machine(): 

    """מבצע משימה M12,M13"""

    ilan.pid_gyro(48,250,precise_distance=False)
    # # ilan.wait_for_button(text="text",debug=True)
    ilan.left_medium_motor.dc(75)
    wait(1000)
    ilan.left_medium_motor.stop()
    ilan.pid_gyro(2,300)
    ilan.left_medium_motor.dc(75)
    wait(2400)
    ilan.left_medium_motor.stop()
    # ilan.drive_by_seconds(-250,2.011)
    # ilan.pid_gyro(46.5,300,Forward_Is_True= False,precise_distance=False)

@timeit
def M08_Doli_camera_2():
    """מבצע משימה M08 המשך"""
    ttt=False
    ilan.pid_gyro(34,300,precise_distance=False)
    wait(200)
    ilan.wait_for_button(debug = ttt,text = "turn")
    ilan.turn(-0.75)
    ilan.wait_for_button(debug = ttt,text = "drive back")
    ilan.pid_gyro(15.95,230,Forward_Is_True=False)
    ilan.wait_for_button(debug = ttt,text = "turn")
    ilan.turn(-35)
    ilan.pid_gyro(10,300, Forward_Is_True=False)
    ilan.wait_for_button(debug = ttt,text = "turn")
    ilan.turn(10)
    ilan.drive_by_seconds(-100, 0.5)
    ilan.turn(10, 50)
    ilan.drive_by_seconds(-400, 1.5)

@timeit
def Show():

    """M06 M07מבצע משימות"""
    Debug=False
    # Debug=True
    # ilan.left_medium_motor.run_time(400,800) 
    # ilan.wait_for_button("",Debug)
    ilan.pid_gyro(46,200,False,precise_distance=True)
    ilan.wait_for_button("turn",Debug)
    ilan.turn(-100)
    ilan.wait_for_button("drive back",Debug)
    # ilan.drive_by_seconds(-200,0.8)
    # ilan.wait_for_button("drive forword",Debug)
    # ilan.drive_by_seconds(200,1.5)
    ilan.drive_by_seconds(200,1)
    ilan.wait_for_button("speen motor",Debug)
    ilan.left_medium_motor.run_angle(800,-250)
    ilan.wait_for_button("drive back",Debug)
    ilan.drive_by_seconds(-300,0.5)
    ilan.wait_for_button("turn",Debug)
    ilan.left_medium_motor.run_angle(600,250,wait=False)
    ilan.turn(-50)
    ilan.wait_for_button("drive back",Debug)
    # ilan.pid_gyro(65,300,False,precise_distance=False)
    ilan.drive_by_seconds(-400,2)
    # ilan.turn(90)

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
    # running = True
    # while running:
    #      ilan.color = input("color: ")
    #      if ilan.color == "yellow" or ilan.color == "pink" or ilan.color == "blue":
    #         running = False

    Runs = [
        ("1 - 3D movie", M01_3D_Movie),
        # ("program test", program_test),
        ("3 - Dolly Camera", M08_Dolly_Camera),
        ("4 - switch scenery", M02_switch_scenery),
        ("5 - Sound Mixer", M10_Sound_Mixr),
        ("6 - Virtual reality artist",Virtual_reality_artist_Creation_machine),
        ("7 - Dolly Camera B",M08_Doli_camera_2),
        ("8 - Show On!!!",Show),
        ("9 - flower",flower)
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
