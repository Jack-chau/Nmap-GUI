import customtkinter as ctk
from menuPage import SwitchMenu
from nmapPage import NmapPage

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
        self.geometry( f'{1300}x{800}+{300}+{200}' )
        self.resizable( False, False )

        # define grid
        self.grid_columnconfigure( 0, weight = 0 )
        self.grid_columnconfigure( 1, weight = 0 )
        self.grid_columnconfigure( 2, weight = 1 )
        self.grid_columnconfigure( 3,  weight = 2 )
        self.grid_columnconfigure( 4,  weight = 8 )
        self.grid_columnconfigure( 5,  weight = 2 )
        self.grid_rowconfigure( ( 0, 1, 2 ), weight = 1 )
        self.grid_rowconfigure( 3, weight = 1)

        # Menu Frame
        self.menu_frame = SwitchMenu( self )
        self.nmap_frame = NmapPage( self )
        
if __name__ == "__main__":   
    main()

      