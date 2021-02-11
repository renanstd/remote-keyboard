from dearpygui import core, simple


core.set_main_window_size(300, 400)
# Callbacks
def activate(sender, data):
    # Disable inputs
    core.configure_item("IP", enabled=False)
    core.configure_item("Port", enabled=False)
    # core.configure_item("Content", enabled=True)

def send_key(sender, data):
    print("Type")

with simple.window("Remote Keyboard"):
    # Title
    core.add_text("Remote Keyboard 1.0")
    core.add_separator()
    # Inputs
    core.add_input_text("IP", label="Device IP")
    core.add_input_text("Port", label="Device port")
    core.add_separator()
    # Button
    core.add_selectable("Activate", callback=activate)
    # core.add_input_text(
    #     "Content",
    #     multiline=True,
    #     enabled=False,
    #     label="",
    #     width=260,
    #     callback=send_key
    # )


core.start_dearpygui(primary_window="Remote Keyboard")
