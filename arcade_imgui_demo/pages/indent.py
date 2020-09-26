import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page


class Indent(Page):
    def __init__(self, window):
        super().__init__(window, "indent", "Indent")

    def on_render(self):
        imgui.begin("Example: item indenting")

        imgui.text("Some text with bullets:")

        imgui.bullet_text("Bullet A")
        imgui.indent()
        imgui.bullet_text("Bullet B (first indented)")
        imgui.bullet_text("Bullet C (indent continues)")
        imgui.unindent()
        imgui.bullet_text("Bullet D (indent cleared)")

        imgui.end()

def install(app):
    app.add_page(Indent(app))

