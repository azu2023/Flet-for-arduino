import flet as flt
from flet import Container, Page, ProgressRing,Stack, Text, alignment,Slider
import base64
import serial

ser = serial.Serial(port='com7',baudrate=9600)

dir = "D:\Images_for_py/tools/"
img_top = open(dir+"pointer.png",'rb')
top = base64.b64encode(img_top.read())
img_next = open(dir+"light.png",'rb')
next = base64.b64encode(img_next.read())

class Countdown(flt.UserControl):
    def __init__(self):
        super().__init__()
        
    def did_mount(self):
        self.update_timer()

    def update_timer(self):
        while True:
            val = ser.readline().decode("utf-8")
            self.ring.value = float(val)
            self.txt.value = f"{int(self.ring.value*100)}%"
            self.update()
    

    def build(self):
        
        self.ring = ProgressRing(
                    value=0,
                    width=300,
                    height=300,
                    color=flt.colors.RED_700,
                    stroke_width=15
                    
                )
        self.txt = Text("0%",color=flt.colors.RED_700,size=30)
    
        self.frame = flt.Column(
        [
        Stack(
            [
                Container(self.txt, alignment=alignment.center),
                self.ring,
            ],
            width=300,
            height=300,
        ),
        
        ],

        )
        
        return self.frame
    
def main(page: Page):
    page.theme_mode = "light"
    section = flt.Container(    
    content=flt.Row([
        flt.Card(
            elevation=40,
            content=flt.Container(
                padding=30,
                border_radius = flt.border_radius.all(30),
                bgcolor="#1e1e1e",
                content=flt.Column(
                [
                
                    Countdown(),
                    
                ],
                ),
            )
        ),
        
    ],
        alignment=flt.MainAxisAlignment.CENTER,
    )
)

    page.add(section)
    
    page.update()
    # auto()

flt.app(target=main)
