import customtkinter as ctk
from time import *

class Clock( ctk.CTkFrame ) :
    def __init__( self, master ) :
        super().__init__( master )    

        self.date_label = ctk.CTkLabel(
                master,
                font = ("Segoe Script", 20),
                fg_color = "transparent",
                text = strftime( "%B %d, %Y" ),
        )
        self.date_label.pack(
                side = 'top',
                pady = ( 10, 0 )
        )
        self.day_label = ctk.CTkLabel(
                master,
                font = ("Segoe Script", 20),
                fg_color = "transparent",
                text = strftime( "%A" ),
        )
        self.day_label.pack(
                side = 'top',
        )          
        self.time_label = ctk.CTkLabel( 
                master,
                font = ("Segoe Script", 20),
                fg_color = "transparent",
                text = strftime( "%H:%M:%S %p" ),
        )
        self.time_label.pack(
                side = 'top',
                pady = ( 20 , 0)
        )     
        self.time_label.after( 1000, func = self.update )
    def update( self ):
        self.time_label.configure( text = strftime( "%H:%M:%S %p" ) )
        self.day_label.configure( text = strftime( "%A" ) )
        self.date_label.configure( text = strftime( "%B %d, %Y" ) )
        self.time_label.after( 1000, func = self.update )
