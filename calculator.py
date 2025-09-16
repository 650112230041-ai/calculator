import flet as ft
import math

def main(page: ft.Page):
    page.title = "เครื่องคิดเลข"
    page.window_width = 300
    page.window_height = 450

    display = ft.TextField(value="", text_align="right", width=280, height=60, read_only=True)

    def button_clicked(e):
        btn_value = e.control.text

        if btn_value == "=":
            try:
                expr = display.value.replace("^", "**")  # ใช้ ^ เป็นโอเปอเรเตอร์ยกกำลัง
                result = eval(expr, {"__builtins__": None}, {"math": math})
                display.value = str(result)
            except:
                display.value = "Error"

        elif btn_value == "C":
            display.value = ""

        elif btn_value == "√":
            try:
                if display.value.strip() != "":
                    val = eval(display.value.replace("^", "**"), {"__builtins__": None}, {"math": math})
                    display.value = str(math.sqrt(val))
            except:
                display.value = "Error"

        else:
            display.value += btn_value

        page.update()

    # เพิ่มปุ่ม ^ และ √
    buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["C", "0", "=", "+"],
        ["^", "√"]
    ]

    rows = []
    for row in buttons:
        btn_row = [
            ft.ElevatedButton(text=btn, width=60, height=60, on_click=button_clicked)
            for btn in row
        ]
        rows.append(ft.Row(btn_row, alignment="center"))

    page.add(
        ft.Column(
            [display] + rows,
            alignment="center",
            horizontal_alignment="center",
            spacing=10,
        )
    )

ft.app(target=main)
