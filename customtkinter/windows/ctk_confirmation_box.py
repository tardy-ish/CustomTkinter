from typing import Union, Tuple, Optional

from .widgets import CTkLabel
from .widgets import CTkEntry
from .widgets import CTkButton
from .widgets.theme import ThemeManager
from .ctk_toplevel import CTkToplevel


class CTkConfirmationBox(CTkToplevel):
    def __init__(self,
                 fg_color: Optional[Union[str, Tuple[str, str]]] = None,
                 text_color: Optional[Union[str, Tuple[str, str]]] = None,
                 button_fg_color: Optional[Union[str, Tuple[str, str]]] = None,
                 button_hover_color: Optional[Union[str, Tuple[str, str]]] = None,
                 button_text_color: Optional[Union[str, Tuple[str, str]]] = None,
                 entry_fg_color: Optional[Union[str, Tuple[str, str]]] = None,
                 entry_border_color: Optional[Union[str, Tuple[str, str]]] = None,
                 entry_text_color: Optional[Union[str, Tuple[str, str]]] = None,

                 title: str = "CTkConfirmationBox",
                 yes: callable= lambda: print("Pressed Yes"),
                 no: callable = lambda: print("Pressed No")
                ):
#     def __init__(self,__yes__,__no__ = lambda: print("Pressed No"), *args, **kwargs):
        # super().__init__(*args, **kwargs)

        super().__init__(fg_color=fg_color)

        self._fg_color = ThemeManager.theme["CTkToplevel"]["fg_color"] if fg_color is None else self._check_color_type(fg_color)
        self._text_color = ThemeManager.theme["CTkLabel"]["text_color"] if text_color is None else self._check_color_type(button_hover_color)
        self._button_fg_color = ThemeManager.theme["CTkButton"]["fg_color"] if button_fg_color is None else self._check_color_type(button_fg_color)
        self._button_hover_color = ThemeManager.theme["CTkButton"]["hover_color"] if button_hover_color is None else self._check_color_type(button_hover_color)
        self._button_text_color = ThemeManager.theme["CTkButton"]["text_color"] if button_text_color is None else self._check_color_type(button_text_color)
        self._entry_fg_color = ThemeManager.theme["CTkEntry"]["fg_color"] if entry_fg_color is None else self._check_color_type(entry_fg_color)
        self._entry_border_color = ThemeManager.theme["CTkEntry"]["border_color"] if entry_border_color is None else self._check_color_type(entry_border_color)
        self._entry_text_color = ThemeManager.theme["CTkEntry"]["text_color"] if entry_text_color is None else self._check_color_type(entry_text_color)

        self._user_input: Union[str, None] = None
        self._running: bool = False

        self.geometry("400x180")
        self.title(title)
        self.lift()  # lift window on top
        self.attributes("-topmost", True)  # stay on top
        self.protocol("WM_DELETE_WINDOW", self._on_closing)
        self.after(10, self._create_widgets)  # create widgets with slight delay, to avoid white flickering of background
        self.resizable(False, False)
        self.grab_set()  # make other windows not clickable
        self._yes = yes
        self._no = no

    def _create_widgets(self):

        self.grid_columnconfigure((0, 1), weight=1)
        self.rowconfigure(0, weight=1)

        self._label = CTkLabel(
                master=self,
                width=300,
                wraplength=300,
                fg_color="transparent",
                text="Are you sure?"
                )
        self._label.grid(
                row=0, 
                column=0, 
                columnspan=2, 
                padx=20, 
                pady=20, 
                sticky="ew"
                )

        self._yes_button = CTkButton(
                master=self,
                width=100,
                border_width=0,
                text='Yes',
                command=self._yes_event
                )
        self._yes_button.grid(
                row=2, 
                column=0, 
                columnspan=1, 
                padx=(20, 10), 
                pady=(0, 20), 
                sticky="ew"
                )

        self._no_button = CTkButton(
                master=self,
                width=100,
                border_width=0,
                text='No',
                command=self._no_event,
                )
        self._no_button.grid(
                row=2, 
                column=1, 
                columnspan=1, 
                padx=(10, 20), 
                pady=(0, 20), 
                sticky="ew"
                )

    def _yes_event(self):
        self._yes()
        self.grab_release()
        self.destroy()

    def _no_event(self):
        self._no()
        self.grab_release()
        self.destroy()

    def _on_closing(self):
        self._no()
        self.grab_release()
        self.destroy()
