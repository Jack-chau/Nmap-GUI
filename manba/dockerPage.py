import customtkinter as ctk
from CTkTable import *
from features import Clock, Appearance, Textbox, Progressbar
from datetime import datetime
import docker

class ContainerManagement( ctk.CTkFrame ) :
    def __init__( self, master ) :
        super( ).__init__( master )
        self.font_style = ( "Helventica bold", 15 )

        # docker Sidebar Frame
        self.docker_sidebar = ctk.CTkFrame( 
            master, 
            width = 70, 
            corner_radius = 0 
        )
        self.docker_sidebar.grid( 
            row = 0, 
            rowspan = 4, 
            column = 2, 
            sticky = 'nsew' 
        )

        # Clock
        self.date_label = Clock( self.docker_sidebar ).date_label
        self.date_label.pack(
            side = 'top',
            pady = ( 10, 0 )
        )
        self.day_label = Clock( self.docker_sidebar ).day_label
        self.day_label.pack(
            side = 'top',
        )
        self.time_label = Clock( self.docker_sidebar ).time_label
        self.time_label.pack(
            side = 'top',
            pady = ( 15 , 0)
        )

        # Sidebar
        self.page_label = ctk.CTkLabel( 
            self.docker_sidebar, 
            text = "Container Management", 
            font = ctk.CTkFont("Segoe Script", 30 ),
        )
        self.page_label.pack( 
            side = 'top',
            pady = ( 40, 30 ),
        )
        # left sidebar window 1


        self.container_btn = ctk.CTkButton( 
            self.docker_sidebar, 
            text="Containers",
            width = 250,
            height = 50,
            font = ctk.CTkFont( "Segoe Script", 20 ),
            # command = self.scan_network
        )
        self.container_btn.pack( 
            side = 'top',
            pady = ( 50, 20 ),
            padx = ( 0, 0 )

        )

        self.img_btn = ctk.CTkButton(
            self.docker_sidebar, 
            text = "Images", 
            width = 250,
            height = 50,
            font = ctk.CTkFont("Segoe Script", 20 ),
        )
        self.img_btn.pack(
            side = 'top',
            pady = ( 10 , 40 ),
            padx = ( 0 , 0 ),
        )
        self.network_btn = ctk.CTkButton(
            self.docker_sidebar, 
            text = "Networks", 
            width = 250,
            height = 50,
            font = ctk.CTkFont("Segoe Script", 20 ),
        )
        self.network_btn.pack(
            side = 'top',
            pady = ( 0 , 50 ),
            padx = ( 0 , 0 )
        )

        # Appearance
        self.appearance_label = Appearance( self.docker_sidebar ).appearance_label
        self.appearance_label.configure( 
            font = ctk.CTkFont("Segoe Script", 30 )
        )
        self.appearance_label.pack( 
            side = 'top',
            pady = ( 150, 20 )
        )

        self.appearance_option_menu = Appearance( self.docker_sidebar ).appearance_optionmenu
        self.appearance_option_menu.configure(
            width = 200,
            height = 50, 
            font = ctk.CTkFont("Segoe Script", 25 ),
            dropdown_font = ctk.CTkFont("Segoe Script", 25 ),
        )
        self.appearance_option_menu.pack( 
            side = 'top',
            pady = ( 20, 20 )
        )

        self.scale_label = Appearance( self.docker_sidebar ).scale_label
        self.scale_label.configure( 
            font = ctk.CTkFont("Segoe Script", 30 )
        )
        self.scale_label.pack( 
            side = 'top',
            pady = ( 20, 20 )
        )

        # self.change_theme = Appearance( self.docker_sidebar ).change_theme
        # self.change_theme.configure( 
        #     font = ctk.CTkFont("Segoe Script", 30 )
        # )
        # self.change_theme.pack( 
        #     side = 'top',
        #     pady = ( 20, 20 )
        # )

        self.scale_optionmenu = Appearance( self.docker_sidebar ).scale_optionmenu
        self.scale_optionmenu.configure(
            width = 200,
            height = 50,
            font = ctk.CTkFont("Segoe Script", 25 ),
            dropdown_font = ctk.CTkFont("Segoe Script", 25 ),
        )
        self.scale_optionmenu.pack(
            side = 'top',
        )

        # Docker Frame
        self.docker_frame = ctk.CTkFrame(
            master,
            width = 300 ,
            border_width = 20,
            corner_radius = 10,
        )
        self.docker_frame.grid( 
            row = 0, 
            column = 4,
            columnspan = 3,
            rowspan = 2,
            sticky = 'nsew',
        )
        # self.docker_tab = ctk.CTkTabview(
        #     self.docker_frame,
        #     width = 50,
        #     height = 400,
        # )
        # self.preview_tab.pack(
        #     side = 'top',
        # )
        # self.preview_tab.add( 'Scan Config' )
        # self.preview_tab.add( 'Scan Log' )
  

        # Text Box Frame
        self.docker_textbox_frame = ctk.CTkFrame( 
            master, 
            width = 70, 
            corner_radius = 0 
        )
        self.docker_textbox_frame.grid( 
            row = 2, 
            rowspan = 2, 
            column = 4,
            columnspan = 3,
            sticky = 'nsew',
        )
        # Textbox
        self.docker_textbox = Textbox( self.docker_textbox_frame ).textbox
        self.docker_textbox.pack(
            side = 'top',
            padx = ( 0, 0 ),
            pady = ( 20, 0 ),
            expand = True,
            fill = 'both',
        )
        # Progress bar
        self.progressbar = Progressbar( self.docker_textbox_frame ).progressbar
        self.progressbar.pack(
            side = 'top',
            fill = 'both',
            padx = (10,10),
            pady = (10,10),
        )
        self.progressbar.set( 0 )
        # self.progressbar.forget()

        # Note Frame
        self.note_frame = ctk.CTkFrame( 
            master, 
            width = 400,
            border_width = 10,
        )
        self.note_frame.grid( 
            row = 0, 
            column = 8, 
            rowspan = 2,
            sticky = 'nsew',
        )

        # Will Update to preview
        self.action_log_tab = ctk.CTkTabview(
            self.note_frame,
            width = 400,
            height = 500,
        )
        self.action_log_tab.pack(
            side = 'top',
            padx = ( 3, 3 ),
            pady = ( 0, 0 )
        )

        # Tab choice
        self.action_log_tab.add( 'Action Log' )

        self.action_label = ctk.CTkLabel(
            self.action_log_tab.tab( 'Action Log' ), 
            text = "Action Log : ",
            font = ( "Comic Sans MS", 30 ),
            width = 400,
        )
        self.action_label.grid(
            row = 0, 
            column = 0, 
            padx = ( 10, 0 ), 
            pady = ( 20, 0 ), 
            sticky = "nsew",
        )
        self.scrollable_frame = ctk.CTkScrollableFrame(
            self.action_log_tab.tab( 'Action Log' ),
            height = 400,
        )
        self.scrollable_frame.grid(
            row = 1,
            column = 0,
            padx= ( 10, 0 ),
            pady = ( 10, 0 ),
            sticky = "nsew" 
        )

        # For demo Only
        test_list = [
            [ "ID", "Description" ],
            [ 1, 'docker images' ],
            [ 2, 'docker ps' ],
            [ 3, 'docker ps -a' ],
            [ 4, 'docker network ls' ],
            [ 5, 'docker run --help' ],
            [ 6, 'docker' ]
        ]

        self.action_table = CTkTable( 
                master = self.scrollable_frame,
                # header_color = '',
                values = test_list,
                hover_color = 'gray20',
                width = 180
            )
        self.action_table.grid(
            row = 1,
            column = 0,
            padx= ( 10, 0 ),
            pady = ( 10, 0 ),
            sticky = "nsew"            
        )

        # self.ip_entry = ctk.CTkEntry(
        #     self.preview_tab.tab( 'Running Container' ), 
        #     placeholder_text = "IP address",
        #     width= 200,
        # )
        # self.ip_entry.grid(
        #     row=0, 
        #     column=1, 
        #     padx=(10,10), 
        #     pady=(25, 10), 
        #     sticky="ew"
        # )

        # Remark Frame
        self.remark_frame = ctk.CTkFrame( 
            master, 
            width = 300,
            border_width = 20,
            corner_radius = 10,
        )
        self.remark_frame.grid( 
            row = 2, 
            column = 8,
            rowspan = 2,
            sticky = 'nsew',
        )
        self.remark_box = ctk.CTkTextbox(
            self.remark_frame,
            font = ( "Comic Sans MS", 20 ),
            border_width = 10,
        )
        self.remark_box.pack(
            side = 'top',
            expand = True,
            fill = 'both'
    
        )
        self.remark_box.insert( 
            "0.0",
            "\nRemarks:\n\n"
        )

    def clear_textbox(self):
        self.docker_textbox.delete( '0.0', 'end' )
