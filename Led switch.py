import flet
from flet import Page
import serial

ser = serial.Serial("com7",baudrate=9600,timeout=3)

def main(page: Page):
    page.horizontal_alignment = "center"
    page.theme_mode = "light"

    def switch_case(e,c):
        if c==0:
            print(e.control.value,"red")
            if e.control.value ==True:
                ser.write("r".encode("utf-8"))
            else:
                ser.write("x".encode("utf-8"))
        if c==1:
            print(e.control.value,"blue")
            if e.control.value ==True:
                ser.write("b".encode("utf-8"))
            else:
                ser.write("c".encode("utf-8"))
        if c==2:
            print(e.control.value,"green")
            if e.control.value ==True:
                ser.write("g".encode("utf-8"))
            else:
                ser.write("v".encode("utf-8"))

    frame = flet.Column(
        expand=20,
    )

    color = "red","green","blue"
    lab = "Red Led","Green Led","Blue Led"
    state = False,False,False
    for i in range(len(color)):
        btn2 = flet.Switch(active_color=f"{color[i]}",value=state[i],label=f"{lab[i]}",
                           on_change=lambda e, c=i:switch_case(e,c))
        
        frame.controls.append(btn2)
    
    
    con = flet.Container(
        padding=3,
        margin=3,
        border_radius=20,
        # width=300,
        bgcolor = "red400",
        width=300,
        content = flet.Card(
        elevation=20,
        content=frame,        
        ),
        
    )
    page.update()
    page.add(con)
    # 

flet.app(target=main)
