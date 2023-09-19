from flet import *
from flet import colors

jumbotron = AppBar(
    toolbar_height=90,
    bgcolor="#E3002A",
    title=Row([
        Container(
            padding = padding.all(4),
            border = border.all(3, "white"),
            border_radius = border_radius.all(30),
            content= Text("Localização", color="white", size=20)
        ),
        Container(
            content=Image(
                src="image/images.png",
                width=100,
                height=70
            )
        )
    ])
)