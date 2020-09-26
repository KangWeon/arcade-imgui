import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page


class Tooltip(Page):
    def __init__(self, window):
        super().__init__(window, "tooltip", "Tooltip")

    def on_render(self):
        imgui.begin("Example: tooltip")
        imgui.button("Click me!")
        if imgui.is_item_hovered():
            imgui.begin_tooltip()
            imgui.text("This button is clickable.")
            imgui.text("This button has full window tooltip.")
            texture_id = imgui.get_io().fonts.texture_id
            imgui.image(texture_id, 512, 64, border_color=(1, 0, 0, 1))
            imgui.end_tooltip()
        imgui.end()

def install(app):
    app.add_page(Tooltip(app))
