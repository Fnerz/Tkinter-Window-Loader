import tkinter as tk

class main:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.current_appyed_widgets = {} # stored as a dict so you can accses the widget by name. like you can append something to a listbox

        # disclaimers
        # till now there are only two "window functions" supported. These are "geometry" and "title". ill probaly add some in the feutere as i will need them.
        # everything is a bit quirky and its only tested to a certin extend

        # general rules
        # coords are always given as a tuple in a (x, y) format
        
        # How to create a window?

        # changing the window
        # for the window function notation/syntax
        # [function as string , function spacific args]
        # E.G
        # ["title", "My Title"]
        # ["geometry", (400, 400)]

        # and for the widgets:
        # [widget name as string, tk.widget, tuple with x y coords as ints]
        # E.G
        # ["MyLabel", tk.Label(master=self.window, text="Hello World"), (10, 10)]

        # special syntax
        # if you want to have a button that calls a funciotn with args, youll need to do that via lambda. see the example below

        # if youre finished the with creating a window you can just call the self.laod_window funciton with a list of all the widgets and window settings
        # all the currently loaded widgets are stored in the self.current_appyed_widgets variable. you can accsess the widgets with the standart dict sysntax
        # for example lets protend we have a listbox with the name my_box loaded.
        # now we can add a new item by just calling self.current_appyed_widgets["my_box"].insert(0,"New Item")

        self.start_window: list[list] = [
            ["title", "My First Widnow"],
            ["geometry", (400 , 400)],
            ["my_label", tk.Label(master=self.window, text="Hello world"), (10, 10)],
            ["my_button", tk.Button(master=self.window, text="add item", command=lambda: self.current_appyed_widgets["box"].insert(0,"Look, a new item appeared")), (10,40)],
            ["box", tk.Listbox(master=self.window, width=30), (100, 40)],
            ["button_2", tk.Button(master=self.window, text="Load Diffrent Widnow", command=lambda: self.load_window(self.second_window)), (200, 220)]
            ]
        
        self.second_window: list[list] = [
            ["title", "Thats a diffrent widnow"],
            ["geometry", (150, 100)],
            ["another_button", tk.Button(master=self.window, text="Load the other window", command=lambda: self.load_window(self.start_window)), (10,10)]
        ]

        self.load_window(self.start_window)
        self.window.mainloop()

    def load_window(self, window: list[list]) -> None:
        for widget in self.current_appyed_widgets.values():
            widget.place_forget()
        self.current_appyed_widgets = {}
        
        for widget_info in window:
            if widget_info[0] == "title":
                self.window.title(widget_info[1])
                continue
            if widget_info[0] == "geometry":
                self.window.geometry(f"{widget_info[1][0]}x{widget_info[1][1]}")
                continue

            widget_info[1].place(x=widget_info[2][0], y=widget_info[2][1])
            self.current_appyed_widgets[widget_info[0]] = widget_info[1]


if __name__ == "__main__":
    main()
            
