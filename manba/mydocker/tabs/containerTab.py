import customtkinter as ctk
from CTkTable import *
import webbrowser

class DockerContainerTab :
    def __init__( self, docker_tab ) :
        self.container_tab = docker_tab.add( 'container' )
        self._setup_ui( )

    def _setup_ui( self ) :

        self.container_label = ctk.CTkLabel(
            self.container_tab,
            text = "Docker Container Management",
            font = ctk.CTkFont(
                family="Courier New",
                size=16,
                weight="bold",
                slant="italic",
                underline=True,
                overstrike=False
            )
        )

        self.container_label.pack(
            pady = 5 ,
            padx = 5 ,
        )

        self.left_frame = ctk.CTkFrame(
            self.container_tab,
            width = 700,
            height = 100,
            corner_radius = 10,
            
        )
        self.left_frame.pack(
            side = 'left',
            fill = 'both',
            expand = True,
            padx = ( 20, 0 ),
            pady = ( 20, 20 ),
        )

        self.right_frame = ctk.CTkFrame(
            self.container_tab,
            width = 300,
            height = 100,
            corner_radius = 10,
            
        )
        self.right_frame.pack(
            side = 'right',
            fill = 'both',
            expand = True,
            padx = ( 20, 20 ),
            pady = ( 20, 20 ),
        )

##### Left Frame
        self.left_frame.grid_columnconfigure( 0, weight = 1 )
        self.left_frame.grid_columnconfigure( 1, weight = 0 )
        self.left_frame.grid_rowconfigure( 0, weight = 1 )
        self.left_frame.grid_rowconfigure( 1, weight = 1 )
        self.left_frame.grid_rowconfigure( 2, weight = 1 )
        self.left_frame.grid_rowconfigure( 3, weight = 1 )
        self.left_frame.grid_rowconfigure( 4, weight = 1 )
        self.left_frame.grid_rowconfigure( 5, weight = 1 )

        self.container_label = ctk.CTkLabel(
            self.left_frame,
            text = "Container Configuration",
            font = ctk.CTkFont(
                family="Courier New",
                size=18,
                weight="bold",
                overstrike=False
            )
        )
        self.container_label.grid(
            column = 0,
            row = 0,
            columnspan = 2,
            pady = ( 20, 0 ),
            padx = ( 10, 10 ),
            sticky = 'ew',
        )

### Create Docker Container
        self.container_start_label = ctk.CTkLabel(
            self.left_frame,
            text = "Run Container: ",
            font = ctk.CTkFont(
                family="Arial",
                size=16,
                weight="bold",
                overstrike=False
            )
        )

        self.container_start_label.grid(
            row = 1,
            column = 0,
            sticky = 'w' ,
            pady = ( 25 , 0 ),
            padx = ( 40, 0 ),
        )

        self.container_start_entry = ctk.CTkEntry(
            self.left_frame ,
            placeholder_text = "container idx",
            font = ctk.CTkFont(
                size=15,
            )
        )

        self.container_start_entry.grid(
            row = 1,
            column = 1,
            sticky = 'we' ,
            pady = ( 25 , 0 ),
            padx = ( 0, 20 ),
        )
#
        self.container_stop_label = ctk.CTkLabel(
            self.left_frame,
            text = "Stop Container: ",
            font = ctk.CTkFont(
                family="Arial",
                size=16,
                weight="bold",
                overstrike=False
            )
        )

        self.container_stop_label.grid(
            row = 2,
            column = 0,
            sticky = 'w' ,
            pady = ( 25 , 0 ),
            padx = ( 40, 0 ),
        )

        self.container_stop_entry = ctk.CTkEntry(
            self.left_frame ,
            placeholder_text = "container idx",
            font = ctk.CTkFont(
                size=15,
            )
        )

        self.container_stop_entry.grid(
            row = 2,
            column = 1,
            sticky = 'we' ,
            pady = ( 25 , 0 ),
            padx = ( 0, 20 ),
        )

        self.container_command_label = ctk.CTkLabel(
            self.left_frame,
            text = "Through command:",
            font = ctk.CTkFont(
                family="Arial",
                size=16,
                weight="bold",
                overstrike=False
            )
        )

        self.container_command_label.grid(
            row = 3,
            column = 0,
            sticky = 'w' ,
            pady = ( 25 , 0 ),
            padx = ( 40, 0 ),
        )

        self.container_command_entry = ctk.CTkEntry(
            self.left_frame ,
            placeholder_text = "docker run ...",
            font = ctk.CTkFont(
                size=15,
            )
        )

        self.container_command_entry.grid(
            row = 3,
            column = 1,
            sticky = 'we' ,
            pady = ( 25 , 0 ),
            padx = ( 0, 20 ),
        )

        self.container_removal_label = ctk.CTkLabel(
            self.left_frame,
            text = "Remove container:",
            font = ctk.CTkFont(
                family="Arial",
                size=16,
                weight="bold",
                overstrike=False
            )
        )

        self.container_removal_label.grid(
            row =4,
            column = 0,
            sticky = 'w' ,
            pady = ( 25 , 0 ),
            padx = ( 40, 0 ),
        )

        self.container_removal_entry = ctk.CTkEntry(
            self.left_frame ,
            placeholder_text = "container idx",
            font = ctk.CTkFont(
                size=15,
            )
        )

        self.container_removal_entry.grid(
            row = 4,
            column = 1,
            sticky = 'we' ,
            pady = ( 25 , 0 ),
            padx = ( 0, 20 ),
        )

        self.docker_exec = ctk.CTkLabel(
            self.left_frame,
            text = "Exec docker container:",
            font = ctk.CTkFont(
                family="Arial",
                size = 16,
                weight="bold",
                overstrike=False
            )
        )
        self.docker_exec.grid(
            row =5,
            column = 0,
            sticky = 'w' ,
            pady = ( 25 , 20 ),
            padx = ( 40, 0 ),
        )

        self.container_exec_entry = ctk.CTkEntry(
            self.left_frame ,
            placeholder_text = "container idx",
            font = ctk.CTkFont(
                size=15,
            )
        )

        self.container_exec_entry.grid(
            row = 5,
            column = 1,
            sticky = 'we' ,
            pady = ( 25 , 20 ),
            padx = ( 0, 20 ),
        )

        self.container_execute = ctk.CTkButton( 
            self.left_frame, 
            text="Execute",
            width = 250,
            height = 50,
            font = ctk.CTkFont( "Segoe Script", 20 ),
        )
        self.container_execute.grid( 
            row = 6,
            column = 0,
            columnspan = 2,
            sticky = 'we' ,
            pady = ( 10 , 20 ),
            padx = ( 10, 10 ),
        )

##### Right Frame
        self.show_container_label = ctk.CTkLabel(
            self.right_frame,
            text = "Docker container information",
            font = ctk.CTkFont(
                family="Courier New",
                size=18,
                weight="bold",
                overstrike=False
            )
        )
        self.show_container_label.grid(
            column = 0,
            row = 0,
            columnspan = 2,
            pady = ( 20, 0 ),
            padx = ( 10, 10 ),
            sticky = 'ew',
        )

        # For demo Only
        test_container_list = [
            [ "idx", "ID", "Names" ,"Tag"],
            [ '1', '2b7c51034242', 'hello', 'latest' ],
            [ '2', '2b7c51034242', 'ubuntu', 'latest' ],
            [ '3', '2b7c51034242', 'nginx', 'alpine' ],
            [ '4', '2b7c51034242', 'nginx', 'latest' ],
            [ '5', '2b7c51034242', 'hello-world', 'latest' ],
            [ '6', '2b7c51034242', 'hello', 'latest' ],
            [ '7', '2b7c51034242', 'ubuntu', 'latest' ],
            [ '8', '2b7c51034242', 'nginx', 'alpine' ],
            [ '9', '2b7c51034242', 'nginx', 'latest' ],
            [ '10', '2b7c51034242', 'hello-world', 'latest' ],
            [ '11', '2b7c51034242', 'hello', 'latest' ],
            [ '12', '2b7c51034242', 'ubuntu', 'latest' ],
            [ '13', '2b7c51034242', 'nginx', 'alpine' ],
            [ '14', '2b7c51034242', 'nginx', 'latest' ],
            [ '15', '2b7c51034242', 'hello-world', 'latest' ],
        ]

        self.show_container_table = CTkTable( 
                master = self.right_frame,
                values = test_container_list,
                width = 100
            )
        self.show_container_table.grid(
            row = 1,
            column = 0,
            columnspan = 2,
            padx= ( 20, 0 ),
            pady = ( 10, 0 ),
            sticky = "ew"            
        )


        self.refrash_btn = ctk.CTkButton( 
            self.right_frame, 
            text="Refresh",
            width = 130,
            height = 30,
            font = ctk.CTkFont( "Segoe Script", 15 ),
        )
        self.refrash_btn.grid( 
            row = 2,
            column = 0,
            columnspan = 2,
            sticky = 'e' ,
            pady = ( 35 , 0 ),
            padx = ( 10, 10 ),
        )