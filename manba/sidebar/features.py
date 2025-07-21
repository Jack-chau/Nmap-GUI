import customtkinter as ctk
from time import *

class Appearance( ctk.CTkFrame ) :
    def __init__( self, master ) :
        super( ).__init__( master )
        self.appearance_label = ctk.CTkLabel(
                master,
                text = "Appearance Mode :",
                
        )
        self.appearance_optionmenu = ctk.CTkOptionMenu(
                master,
                values = [  "Light", "Dark" ],
                anchor = "center",
                command = self.change_appearance,
        )
        self.scale_label = ctk.CTkLabel(
                master,
                text = "UI Scaling:",
        )        
        self.scale_optionmenu = ctk.CTkOptionMenu(
                master,
                values = [ '50%', '80%', '100%', '120%', '140%' ],
                anchor = "center",
                command = self.change_scale
        )
        self.scale_optionmenu.set( "100%" )

        # self.change_theme = ctk.CTkOptionMenu(
        #         master,
        #         values = [ 'breeze', 'cherry', 'coffee', 'lavender' ],
        #         anchor = "center",
        #         command = self.change_theme
        # )


    def change_appearance( self, new_appearance_mode : str ):
        ctk.set_appearance_mode( str( new_appearance_mode ) )

    def change_scale( self, new_scaling : str ):
        new_scaling_float = int( new_scaling.replace( "%", "" ) ) / 100
        ctk.set_widget_scaling( new_scaling_float )

#     def change_theme( self, theme : str ):
#         ctk.set_default_color_theme( f'./theme/{ str( theme ) }.json' )
        

class Clock( ctk.CTkFrame ) :
    def __init__( self, master ) :
        super().__init__( master )    

        self.date_label = ctk.CTkLabel(
                master,
                font = ("Segoe Script", 30),
                fg_color = "transparent",
                text = strftime( "%B %d, %Y" ),
        )
        self.day_label = ctk.CTkLabel(
                master,
                font = ("Segoe Script", 30),
                fg_color = "transparent",
                text = strftime( "%A" ),
        )         
        self.time_label = ctk.CTkLabel( 
                master,
                font = ("Segoe Script", 30),
                fg_color = "transparent",
                text = strftime( "%H:%M:%S %p" ),
        )
        self.time_label.after( 1000, func = self.update )
    def update( self ):
        self.time_label.configure( text = strftime( "%H:%M:%S %p" ) )
        self.day_label.configure( text = strftime( "%A" ) )
        self.date_label.configure( text = strftime( "%B %d, %Y" ) )
        self.time_label.after( 1000, func = self.update )

class Textbox( ctk.CTkFrame ):
    def __init__( self, master ) :
        super().__init__( master )
        self.textbox = ctk.CTkTextbox(
                master,
                corner_radius = 0,
                border_width = 0,
                # border_color = 'grey20',
                font = ctk.CTkFont( size=15, weight='bold' )
        )
class Progressbar( ctk.CTkFrame ) :
    def __init__( self, master ) :
        super().__init__( master )
        self.progressbar = ctk.CTkProgressBar(
                master,
                orientation='horizontal',
                height = 30,
                border_width = 2,
                corner_radius = 2,
                progress_color = '#7cc0ea',
        )