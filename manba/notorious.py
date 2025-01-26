import customtkinter as ctk
from menuPage import SwitchMenu

def main() :
    app = Notorious()
    app.mainloop()


class Notorious( ctk.CTk ) :
    def __init__( self ) :
        super( ).__init__( )
        ctk.set_appearance_mode( 'dark' )
        ctk.set_default_color_theme( 'green' )
        # root window size
        self.title( "Dream Big" )
        self.geometry( f'{2300}x{1600}+{900}+{300}' )

        # define grid
        self.grid_columnconfigure( 0, weight = 0 )
        self.grid_columnconfigure( 1, weight = 0 )
        self.grid_columnconfigure( 2, weight = 5 )
        self.grid_columnconfigure( 3,  weight = 3 )
        self.grid_columnconfigure( 4,  weight = 3 )
        self.grid_rowconfigure( ( 0, 1, 2 ), weight = 1 )
        self.grid_rowconfigure( 3, weight = 1)

        # Menu Frame
        menu_frame = SwitchMenu( self )



if __name__ == "__main__":   
    main()

      