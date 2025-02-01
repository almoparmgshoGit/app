from flet import * 
from time import sleep

def main(page:Page):
    page.title = "تطبيق المجال"
    page.window.width = 390
    page.window.height = 740
    page.window.top = 10
    page.window.left = 960
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = colors.WHITE


    page.appbar = AppBar(
        title=Text("عمل روابط وتساب مجانا"),
        bgcolor='green',
        leading=Icon(icons.HOME),
        center_title=True,
        leading_width=80,
        actions=[
            PopupMenuButton(
               #Item Button
                items=[
                    PopupMenuItem(text='انشاء حساب مجال' , icon=icons.CODE),
                    PopupMenuItem(text='شرح التطبيق' , icon=icons.APP_BLOCKING),
                    PopupMenuItem(text='المطورين' , icon=icons.DEVELOPER_MODE_SHARP),
                    PopupMenuItem(),
                    PopupMenuItem(text="تقييم التطبيق" , icon=icons.STAR_HALF),
                ]
            ),
        ]
    )


    def button_clicked(e):
        t.value = f"Dropdown value is:  {dd.value}"
        page.update()

        t = Text()
        b = ElevatedButton(text="Submit", on_click=button_clicked)
        dd= ""
        page.add(dd, b, t)
    def link(e):
        l = f"https://wa.me/{int(number.value)}"
        print(l)
        number.value = ""
        alert = AlertDialog(
            title= Text("تم انشاء الرابط" , size=18 , color="green")
        )
        page.overlay.append(alert)
        alert.open = True
        page.update()
    def button_clicked(e):
        page.bgcolor = dd.value
        page.update()
    t = Text()
    b = ElevatedButton(text="Submit", on_click=button_clicked)
    dd = Dropdown(
        width=200,
        bgcolor=colors.AMBER,
        color= colors.WHITE,
        icon=icons.COLOR_LENS,
        options=[
            dropdown.Option("Red"),
            dropdown.Option("Green"),
            dropdown.Option("Blue"),
        ],
    )

    
    audio1 = Audio(
        src="/Users/coderx/Desktop/قران/ساعتين من الهدوء والإسترخاء للقارئ بدر التركي.m4a" ,
    )
    
    page.overlay.append(audio1)
    page.add(
        Text("This is an app with background audio."),
        ElevatedButton("Stop playing", on_click=lambda _: audio1.pause()),
        ElevatedButton("Stop2 playing", on_click=lambda _: audio1.resume()),
        ElevatedButton("Start playing", on_click=lambda _: audio1.play()),
    )
    page.add(dd, b, t)
    number = TextField(label="رقم الهاتف اخي" , text_align='center' , prefix_icon=icons.PHONE , color=colors.BLACK)
    btn = ElevatedButton('انشاء' , width=170 , color=colors.WHITE , on_click=link)
    
    page.add(number , btn)

    page.update()
app(main)
