import customtkinter as ctk
from sidebar.menuPage import SwitchMenu
from mydocker.dockerPage import MyDockerPage

def main() :
    app = Notorious()
    app.mainloop()

class Notorious( ctk.CTk ) :
    def __init__( self ) :
        super( ).__init__( )
        ctk.set_appearance_mode( 'light' )
        ctk.set_default_color_theme( './theme/rime.json' )
        ctk.set_widget_scaling( 1.0 )
        # root window size
        self.title( "IShowSpeed" )
        self.geometry( f'{1800}x{1200}+{180}+{80}' )
        #self.resizable( False, False )

        # define grid ( 10 column * 4 row )
        self.grid_columnconfigure( 0, weight = 0 )
        self.grid_columnconfigure( 1, weight = 0 )
        self.grid_columnconfigure( 2, weight = 2 )
        self.grid_columnconfigure( 3, weight = 1 )
        self.grid_columnconfigure( 4,  weight = 15 )
        self.grid_columnconfigure( 5,  weight = 1 )
        self.grid_columnconfigure( 6,  weight = 2 )
        self.grid_columnconfigure( 7,  weight = 1 )
        self.grid_columnconfigure( 8,  weight = 1 )
        self.grid_columnconfigure( 9,  weight = 1 )
        self.grid_rowconfigure( ( 0, 1, 2 ), weight = 1 )
        self.grid_rowconfigure( 3, weight = 1)

        # Menu Frame
        self.switch_menu = SwitchMenu( self )

        # Docker Page
        self.MyDockerPage = MyDockerPage( self )

if __name__ == "__main__":   
    main()

      