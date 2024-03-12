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
    ilan.pid_gyro(18.5,450,Kp=0,precise_distance=False)
    wait(350)
    ilan.drive_by_seconds(450,1)
    wait(500)
    ilan.wait_for_button(debug=False,text="Drive Back")
    ilan.speed_formula(50.8,450,Forward_Is_True=False,Kp=0)

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
    wait(200)
    ilan.speed_formula(12,450)
    #ilan.wait_for_button(text="turn")
    ilan.turn(28,150)
    wait(500)
    ilan.robot.stop()
    ilan.speed_formula(56,200)

@timeit
def flower():
# """מבצע משימות M14"""
    Debug=True
    precise_distance=True
    # ilan.right_medium_motor.dc(50)
    # ilan.right_medium_motor.stop()
    ilan.speed_formula(55.5 ,250)
    # ilan.wait_for_button("a")
    ilan.turn(-30)
    # ilan.wait_for_button("after turn",debug=True)
    ilan.speed_formula(30,320)
    # ilan.wait_for_button("turn",debug=True)
    ilan.turn(4)
    ilan.speed_formula(19,300)
    # ilan.turn(40)
    # ilan.wait_for_button("F",debug=True)
    ilan.pid_gyro(-13,300)
    # ilan.wait_for_button("G",debug=True)
    # ilan.pid_gyro(-9)
    # ilan.turn(20)
    ilan.turn_until_seconds(1,22)
    # ilan.wait_for_button("R",debug=True)
    ilan.speed_formula(-3,100)
    # ilan.wait_for_button("S",debug=True)
    ilan.robot.drive(-80,-24)
    wait(2200)
    ilan.robot.stop()
    # ilan.wait_for_button("T",debug=True)
    ilan.speed_formula(10,300,Forward_Is_True=False)
    # ilan.wait_for_button("A",debug=True)
    ilan.turn(-10,150)
    # ilan.wait_for_button("B",debug=True)
    ilan.speed_formula(105,325)
    # ilan.wait_for_button("d",debug=True)
    ilan.turn(-65  )
    # ilan.wait_for_button("E",debug=True)
    ilan.speed_formula(63,300)
   
@timeit    
def test():
    # ilan.right_medium_motor.dc(5000)
    # wait(2500)
    # ilan.robot.drive(-100,360)
    # wait(100000000000000000)
    # ilan.robot.stop()
    # ilan.drive_angle(2,220,200)
    # ilan.pid_gyro(99,200)
    # ilan.turn(-10)
    # ilan.pid_gyro(10,250,Forward_Is_True=False)
    ilan.turn_until_seconds(1,22)



@timeit
def M02_switch_scenery():

    """מבצע משימות M02 M03"""

    
    ilan.turn(-3)
    # ilan.wait_for_button(text="eeee")
    #ilan.pid_gyro(56,300,precise_distance=False)
    ilan.speed_formula(59,400)
    ilan.turn(-70,200)
    ilan.stop_on_line
    ilan.drive_by_seconds(100,1.4)
    ilan.drive_by_seconds(-75,1)
    # ilan.drive_by_seconds(100,0.90)
    # ilan.drive_by_seconds(-75,0.80)
    # ilan.wait_for_button(text="turn")
    ilan.turn(135,200)
    # ilan.drive_by_seconds(-500,2)
    # ilan.wait_for_button(text="drive forword")
    ilan.speed_formula(41.5,400)
    # ilan.wait_for_button(text="turn")
    ilan.turn(90,200)
    ilan.pid_gyro(9,250,Forward_Is_True=False)
    ilan.turn(-15)
    wait(100)
    ilan.pid_gyro(2,250,Forward_Is_True=False)
    ilan.turn(20)
    ilan.wait_for_button(text="A")
    ilan.speed_formula(50,400)
    ilan.turn(65)
    ilan.speed_formula(62,400,)
    # ilan.pid_gyro(1,250,Forward_Is_True=False)
    # ilan.speed_formula(5,250)
    # ilan.turn(100)
    # ilan.speed_formula(50,300)
    # ilan.turn(-80)
    # ilan.speed_formula(60,400)
    # ilan.turn(-20)

 

@timeit         
def Virtual_reality_artist_Creation_machine(): 

    """מבצע משימה M12,M13"""

    ilan.pid_gyro(50,350,precise_distance=False)
    # ilan.wait_for_button(text="text",debug=True)
    ilan.left_medium_motor.dc(160)
    wait(1750)
    ilan.left_medium_motor.stop()
    ilan.pid_gyro(48,400,False,precise_distance=False)
    # ilan.drive_by_seconds(-250,2.011)
    # ilan.pid_gyro(46.5,300,Forward_Is_True= False,precise_distance=False)

@timeit
def M08_Doli_camera_2():
    """מבצע משימה M08 המשך"""
    # ttt=True
    ttt=False
    ilan.pid_gyro(34,320,precise_distance=False)
    wait(200)
    ilan.wait_for_button(debug = ttt,text = "turn")
    # ilan.turn(-0.35)
    ilan.wait_for_button(debug = ttt,text = "drive back")
    ilan.pid_gyro(14.95,230,Forward_Is_True=False,precise_distance=False)
    ilan.wait_for_button(debug = ttt,text = "turn")
    ilan.turn(-35)
    ilan.pid_gyro(6,300, Forward_Is_True=False)
    ilan.wait_for_button(debug = ttt,text = "turn")
    ilan.turn(10)
    ilan.drive_by_seconds(-200,0.5)
    ilan.wait_for_button(debug = ttt,text = "turn")
    ilan.turn(3)
    ilan.drive_by_seconds(-500,1.5)

@timeit
def ORNGE_MEN():
    "מבצע משימה 1234"

    ilan.pid_gyro(90,6666666666666666666666)
    ilan.turn(-10)
    ilan.pid_gyro(10,6666666666666666666666,Forward_Is_True=False)
    


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
    Debug=True
    # Debug=True
    # ilan.left_medium_motor.run_time(400,800) 
    ilan.wait_for_button("",Debug)
    ilan.pid_gyro(45,200,False,precise_distance=True)
    ilan.wait_for_button("turn",Debug)
    ilan.turn(-100)
    # ilan.wait_for_button("drive back",Debug)   
    # ilan.drive_by_seconds(-200,0.8)
    # ilan.wait_for_button("drive forword",Debug)
    # ilan.drive_by_seconds(200,1.5)
    ilan.drive_by_seconds(200,1.1)
    # ilan.wait_for_button("speen motor",Debug)
    ilan.left_medium_motor.run_angle(900,-300)
    # ilan.wait_for_button("drive back",Debug)
    ilan.drive_by_seconds(-300,0.5)
    # ilan.wait_for_button("turn",Debug)
    ilan.left_medium_motor.run_angle(600,250,wait=False)
    ilan.turn(-80)
    ilan.wait_for_button("drive back",Debug)
    # ilan.pid_gyro(65,300,False,precise_distance=False)
    ilan.drive_by_seconds(-400,2.1)
    # ilan.turn(90)
    ilan

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
        ("4 - Flower",flower),
        ("5 - Sound Mixer", M10_Sound_Mixr),
        ("6 - Dolly Camera B",M08_Doli_camera_2),
        ("7 - Switch scenery", M02_switch_scenery),
        ("TEST",test),        
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
