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
        return "Run time: {} sec.".format(round(total_time, 1))
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

    ilan.pid_gyro(19,250)
    ilan.turn(30)
    ilan.turn(-45)
    ilan.pid_gyro(19,300,False,precise_distance=False)

@timeit
def M08_Dolly_Camera():
    """מבצע את משימות M08"""
    ilan.pid_gyro(18.5,450,Kp=0,precise_distance=False)
    wait(350)
    ilan.drive_by_seconds(300,1.5)
    wait(500)
    ilan.wait_for_button(debug=False,text="Drive Back")
    ilan.speed_formula(50.8,450,Forward_Is_True=False,Kp=0)

@timeit
def M10_Sound_Mixr():
    """מבצע את משימות M10"""
    debug = False
    ilan.speed_formula(45,400)
    # ilan.wait_for_button(text="turn",debug=False)
    ilan.turn(14)
    ilan.speed_formula(40,400,False)
    # ilan.drive_by_seconds(400,0.8)
    ilan.turn(-80)
    wait(200)
    ilan.speed_formula(12,450)
    #ilan.wait_for_button(text="turn")
    ilan.turn(28,150)
    wait(500)
    ilan.robot.stop()
    ilan.speed_formula(53,200,Forward_Is_True=False)




"work in jebata!!!!!!!!!!!!!!!!!!!!!!"
@timeit
def flower_1():
    """מבצע משימות M14"""
    "נסיון 2 לפרח"
    """אחרי שהפונקציה לא עבדה החלטנו לעשות נסיון נוסף."""
    "r=אחורה"
    "F= ישר"
    debug=False
    precise_distance=True
    ilan.speed_formula(50,300)
    # ilan.wait_for_button("turn",debug=True)
    ilan.turn(-30)
    # ilan.wait_for_button("after turn",debug=True)
    ilan.speed_formula(55,320)
    # ilan.wait_for_button("turn right")
    ilan.turn(30)
    ilan.pid_gyro(8, 100, False)
    # ilan.wait_for_button("TRY",debug)
    ilan.turn(27.546)
    # ilan.wait_for_button("FLAWAR")
    ilan.pid_gyro(11.54, 100, False)
    # ilan.wait_for_button("drive back")
    ilan.turn(56)
    ilan.pid_gyro(12,150)
    ilan.turn(-5)
    ilan.turn(63)
    ilan.wait_for_button("F")
    ilan.speed_formula(100,400,Forward_Is_True=False)
    # ilan.wait_for_button("about to turn left")
    ilan.turn(-53.152)
    ilan.drive_by_seconds(-400, 2)
    # ilan.pid_gyro(-12,250)
    # ilan.wait_for_button("turn",debug)
    # ilan.turn_until_seconds(0.5,40)
    # ilan.wait_for_button("R",debug)
    # # ilan.speed_formula(-5,50)
    # ilan.wait_for_button("turn",debug)
    # ilan.robot.drive(-80,-35)
    # wait(2200)
    # ilan.robot.stop()
    # ilan.wait_for_button("R",debug)
    # ilan.speed_formula(10,300,Forward_Is_True=False)
    # ilan.wait_for_button("drive",debug)
    # ilan.speed_formula(10,200)
    # ilan.turn(-7,100)             
    # ilan.speed_formula(95,325)
    # # ilan.wait_for_button("turn",debug=True)
    # ilan.turn(-70.24546,250)
    # # ilan.wait_for_button("drive",debug=True)
    # ilan.pid_gyro(63,350)

@timeit
def oreng_man():

    ilan.speed_formula(47,350)
    ilan.turn(-17)
    ilan.speed_formula(6,300)
    ilan.speed_formula(13,200,Forward_Is_True=False)
    ilan.turn_until_seconds(2,40,turn_right=True)
    ilan.speed_formula(50,300,Forward_Is_True=False)

@timeit    
def test():

    ilan.pid_gyro(99,200)
    ilan.turn(-10)
    ilan.pid_gyro(10,250,Forward_Is_True=False)
 


@timeit
def M02_switch_scenery():

    """מבצע משימות M02 M03"""

    ilan.speed_formula(70,400)
    ilan.turn(-40,200)
    for i in range(1):
        ilan.speed_formula(5.5,150)
        ilan.speed_formula(8,150,False)
    ilan.turn(80)
    ilan.pid_gyro(60,400,False,precise_distance=False)

 

@timeit         
def Virtual_reality_artist_Creation_machine(): 

    """מבצע משימה M12,M13"""
    """R=אחורה"""
    ilan.left_medium_motor.dc(160)
    ilan.speed_formula(50, 250)  
    ilan.drive_by_seconds(50, 1)
    wait(500)
    ilan.left_medium_motor.stop()
    ilan.pid_gyro(22,100,Forward_Is_True=False,precise_distance=False)
    # ilan.pid_gyro(35,300,Forward_Is_True=False,precise_distance=False)
    ilan.drive_by_seconds(-300, 1.7)


@timeit
def M08_Doli_camera_2():
    """מבצע משימה M08 המשך"""
    t=False
    "r=אחורה"
    ilan.pid_gyro(34,320,precise_distance=False)
    wait(200)
    # ilan.turn(-0.35)
    ilan.wait_for_button(debug=t,text="R")
    ilan.pid_gyro(14.95,230,Forward_Is_True=False,precise_distance=False)
    ilan.wait_for_button(debug=t,text="turn")
    ilan.turn(-35)
    ilan.pid_gyro(6,300, Forward_Is_True=False)
    ilan.wait_for_button(debug=t,text="turn")
    ilan.turn(10)
    ilan.drive_by_seconds(-200,0.5)
    ilan.wait_for_button(debug=t,text="turn")
    ilan.turn(3)
    ilan.drive_by_seconds(-500,1.5)

@timeit
def orenge():
    "מבצע משימה 1234"

    ilan.drive_by_seconds(25,30)


# @timeit
# def Show():


#     """M06 M07מבצע משימות"""

#     Debug=True
#     speed_shay = 1200
#     ilan.wait_for_button("speen motor",Debug)
#     ilan.left_medium_motor.run_angle(speed_shay,-250)
#     ilan.wait_for_button("speen motor",Debug)
#     ilan.left_medium_motor.run_angle(speed_shay,250)
#     ilan.wait_for_button("speen motor",Debug)
#     ilan.left_medium_motor.run_angle(speed_shay,-250)
#     ilan.wait_for_button("speen motor",Debug)
#     ilan.left_medium_motor.run_angle(speed_shay,250)
#     ilan.wait_for_button("speen motor",Debug)
#     ilan.left_medium_motor.run_angle(speed_shay,-250)
#     ilan.wait_for_button("speen motor",Debug)
#     ilan.left_medium_motor.run_angle(speed_shay,250)
#     ilan.wait_for_button("speen motor",Debug)
#     ilan.left_medium_motor.run_angle(speed_shay,-250)
#     ilan.wait_for_button("speen motor",Debug)
#     ilan.left_medium_motor.run_angle(speed_shay,250)


@timeit
def Show1():

    """M06 M07מבצע משימות"""
    Debug=False
    # ilan.left_medium_motor.run_time(400,800) 
    ilan.wait_for_button("drive back",Debug)
    ilan.pid_gyro(43,200,False,precise_distance=True)
    ilan.wait_for_button("turn",Debug)
    ilan.turn(-100)
    # ilan.wait_for_button("drive back",Debug)   
    # ilan.drive_by_seconds(-200,0.8)
    # ilan.wait_for_button("drive forword",Debug)
    # ilan.drive_by_seconds(200,1.5)
    ilan.drive_by_seconds(200,1.3)
    ilan.wait_for_button("speen motor",Debug)
    wait(200)
    # ilan.left_medium_motor.run_angle(500, -300)
    # ilan.left_medium_motor.run_angle(900, 100)
    ilan.turn(5)
    ilan.left_medium_motor.run_angle(900,-600)
    ilan.turn(-5)
    ilan.wait_for_button("drive back",Debug)
    ilan.drive_by_seconds(-300,0.5)
    # ilan.wait_for_button("turn",Debug)
    ilan.left_medium_motor.run_angle(600,400,wait=False)
    ilan.turn(-80)
    # ilan.wait_for_button("drive back",Debug)
    # ilan.pid_gyro(65,300,False,precise_distance=False)
    ilan.drive_by_seconds(-400,2.1)
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
        
        ("1 - Show On!!!",Show1),
        ("2 - Dolly Camera", M08_Dolly_Camera),
        ("3 - Virtual reality artist",Virtual_reality_artist_Creation_machine),
        ("4 - Flower",flower_1),
        ("5 - Sound Mixer", M10_Sound_Mixr),
        ("6 - Dolly Camera B",M08_Doli_camera_2),
        ("7 - Switch scenery", M02_switch_scenery),
        ("oreng", oreng_man),
        ("oreng man",oreng_man),
        # ("      clean", orenge),
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

                if current_run == 0:
                    elsapsed_time.reset()

                run_time=Runs[current_run][1]()
            
                current_run += 1

                if current_run >= len(Runs):
                    current_run = 0

                ilan.write("{}\nElapsed: {} s \n{}".format(run_time,round(elsapsed_time.time()/1000.0, 1), Runs[current_run][0]))
        except Exception as EX :
            print(str(EX))
            wait(1500)
            
running()
