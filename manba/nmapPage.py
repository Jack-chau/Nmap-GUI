import customtkinter as ctk
import nmap
import sqlite3
from sqlite3 import Error
from datetime import datetime
from clock import Clock

class NmapPage( ctk.CTkFrame ) :
    def __init__( self, master ) :
        super( ).__init__( master )

        # Configuration
        # self.database = r'sasqdemo.db'
        # self.conn = self.create_connection( self.database )
        # self.data = self.select_all_records( )
        self.font_style = ( "Helventica bold", 15 )

        # Nmap Sidebar Frame
        self.nmap_sidebar = ctk.CTkFrame( 
                master, 
                width = 70, 
                corner_radius = 0 
        )
        self.nmap_sidebar.grid( 
                row = 0, 
                rowspan = 4, 
                column = 2, 
                sticky = 'nsew' 
        )
        self.clock_frame = Clock( self.nmap_sidebar )

        # Sidebar
        self.page_label = ctk.CTkLabel( 
                self.nmap_sidebar, 
                text = "Nmap Page", 
                font = ctk.CTkFont("Segoe Script", 30 ),
                
        )
        self.page_label.pack( 
                side = 'top',
                pady = ( 40, 30 ),
        )
        # left sidebar window 1


        self.scan_network = ctk.CTkButton( 
                self.nmap_sidebar, 
                text="Scan Network",
                width = 180,
                height = 50,
                font = ctk.CTkFont( "Segoe Script", 15 ),
                # text_color= 'purple'
                #command = self.scan_network
        )
        self.scan_network.pack( 
                side = 'top',
                pady = ( 20, 20 ),
                padx = ( 0, 0 )

        )

        self.save_btn = ctk.CTkButton(
                self.nmap_sidebar, 
                text = "Save Record", 
                #command = self.save_results 
                width = 180,
                height = 50,
                font = ctk.CTkFont("Segoe Script", 15 ),
                # text_color= 'purple'
        )
        self.save_btn.pack(
                side = 'top',
                pady = ( 10 , 50 ),
                padx = ( 0 , 0 )
        )

