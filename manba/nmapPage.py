import customtkinter as ctk
from features import Clock, Appearance, Textbox, Progressbar
import nmap
import sqlite3
from sqlite3 import Error
from datetime import datetime

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
        self.date_label = Clock( self.nmap_sidebar ).date_label
        self.date_label.pack(
                side = 'top',
                pady = ( 10, 0 )
        )
        self.day_label = Clock( self.nmap_sidebar ).day_label
        self.day_label.pack(
                side = 'top',
        )
        self.time_label = Clock( self.nmap_sidebar ).time_label
        self.time_label.pack(
                side = 'top',
                pady = ( 20 , 0)
        )     
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

        # Appearance
        self.appearance_label = Appearance( self.nmap_sidebar ).appearance_label
        self.appearance_label.configure( 
                font = ctk.CTkFont("Segoe Script", 20 )
        )
        self.appearance_label.pack( 
                side = 'top',
                pady = ( 150, 20 )
        )

        self.appearance_optionmenu = Appearance( self.nmap_sidebar ).appearance_optionmenu
        self.appearance_optionmenu.configure(
                width = 150,
                height = 40, 
                font = ctk.CTkFont("Segoe Script", 15 ),
                dropdown_font = ctk.CTkFont("Segoe Script", 15 ),
        )
        self.appearance_optionmenu.pack( 
                side = 'top',
                pady = ( 20, 20 )
        )

        self.scale_label = Appearance( self.nmap_sidebar ).scale_label
        self.scale_label.configure( 
                font = ctk.CTkFont("Segoe Script", 20 )
        )
        self.scale_label.pack( 
                side = 'top',
                pady = ( 10, 20 )
        )

        self.scale_optionmenu = Appearance( self.nmap_sidebar ).scale_optionmenu
        self.scale_optionmenu.configure(
                width = 150,
                height = 40,
                font = ctk.CTkFont("Segoe Script", 15 ),
                dropdown_font = ctk.CTkFont("Segoe Script", 15 ),
        )
        self.scale_optionmenu.pack(
                side = 'top',
        )

        # Text Box        
        self.nmap_textbox_frame = ctk.CTkFrame( 
                master, 
                width = 70, 
                corner_radius = 0 
        )
        self.nmap_textbox_frame.grid( 
                row = 0, 
                rowspan = 4, 
                column = 3, 
                sticky = 'nsew' 
        )
        self.nmap_textbox = Textbox( self.nmap_textbox_frame ).textbox
        self.nmap_textbox.pack(
                side = 'top',
                padx = ( 0,0 ),
                pady = ( 0, 0 ),
                expand = True,
                fill = 'both',
        )
        # Progress bar
        self.progressbar = Progressbar( self.nmap_textbox_frame ).progressbar
        self.progressbar.pack(
                side = 'top',
                fill = 'both',
                padx = (10,10),
                pady = (10,10),
        )
        self.progressbar.set( 0.52 )
        # self.progressbar.forget()