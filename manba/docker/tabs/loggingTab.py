import customtkinter as ctk
from CTkTable import *

class DockerInfoTab :
    def __init__( self, docker_tab ) :
        self.info_tab = docker_tab.add( 'info' )
        self._setup_ui( )

    def _setup_ui( self ) :

        self.info_label = ctk.CTkLabel(
            self.info_tab,
            text = "Hello! Welcome to check docker information!",
            font = ctk.CTkFont(
                family="Courier New",
                size=16,
                weight="bold",
                slant="italic",
                underline=True,
                overstrike=False
            )
        )

        self.info_label.pack(
            pady = 5 ,
            padx = 5 ,
        )

        self.left_info_frame = ctk.CTkFrame(
            self.info_tab,
            # fg_color = "grey20",
            width = 300,
            height = 100,
            # border_width = 2,
            corner_radius = 10,
            
        )
        self.left_info_frame.pack(
            side = 'left',
            fill = 'both',
            expand = True,
            padx = ( 20, 0 ),
            pady = ( 20, 20 ),
        )

        self.right_info_frame = ctk.CTkFrame(
            self.info_tab,
            # fg_color = "grey20",
            width = 500,
            height = 100,
            # border_width = 2,
            corner_radius = 10,
            
        )
        self.right_info_frame.pack(
            side = 'right',
            fill = 'both',
            expand = True,
            padx = ( 20, 20 ),
            pady = ( 20, 20 ),
        )

##### Left Frame
        self.left_info_frame.grid_columnconfigure( 0, weight = 1 )
        self.left_info_frame.grid_columnconfigure( 1, weight = 1 )
        self.left_info_frame.grid_rowconfigure( 0, weight = 0 )
        self.left_info_frame.grid_rowconfigure( 1, weight = 0 )
        self.left_info_frame.grid_rowconfigure( 2, weight = 0 )
        self.left_info_frame.grid_rowconfigure( 3, weight = 0 )
        self.left_info_frame.grid_rowconfigure( 4, weight = 0 )
        self.left_info_frame.grid_rowconfigure( 5, weight = 0 )

        self.check_label = ctk.CTkLabel(
            self.left_info_frame,
            text = "What you want to check? ^_^",
            font = ctk.CTkFont(
                family="Courier New",
                size=18,
                weight="bold",
                overstrike=False
            )
        )
        self.check_label.grid(
            column = 0,
            row = 0,
            columnspan = 2,
            pady = ( 20, 0 ),
            padx = ( 10, 10 ),
            sticky = 'ew',
        )

### Check Box
        self.docker_cli_version = ctk.CTkCheckBox(
            self.left_info_frame ,
            text = "Docker Client Version",
            onvalue = "on",
            offvalue = "off",
            font = ctk.CTkFont(
                size=15,
            )
        )
        self.docker_cli_version.grid(
            row = 1,
            column = 0,
            sticky = 'w' ,
            pady = ( 25 , 25),
            padx = ( 40, 0 ),
        )

        self.docker_server_version = ctk.CTkCheckBox(
            self.left_info_frame ,
            text = "Docker Server Version",
            onvalue = "on",
            offvalue = "off",
            font = ctk.CTkFont(
                size=15,
            )
        )

        self.docker_server_version.grid(
            row = 1,
            column = 1,
            sticky = 'w' ,
            pady = ( 25 , 25),
            padx = ( 10, 20 ),
        )

        self.docker_context = ctk.CTkCheckBox(
            self.left_info_frame ,
            text = "Docker context",
            onvalue = "on",
            offvalue = "off",
            font = ctk.CTkFont(
            size=15,
            )
        )

        self.docker_context.grid(
            row = 2,
            column = 0,
            sticky = 'w' ,
            pady = ( 25 , 25),
            padx = ( 40, 0 ),
        )

        self.docker_info = ctk.CTkCheckBox(
            self.left_info_frame ,
            text = "Docker Info",
            onvalue = "on",
            offvalue = "off",
            font = ctk.CTkFont(
            size=15,
            )
        )
        self.docker_info.grid(
            row = 2,
            column = 1,
            sticky = 'w' ,
            pady = ( 25 , 25),
            padx = ( 10, 0 ),
        )

        self.all_containers = ctk.CTkCheckBox(
            self.left_info_frame ,
            text = "Docker Networks",
            onvalue = "on",
            offvalue = "off",
            font = ctk.CTkFont(
            size=15,
            )
        )

        self.all_containers.grid(
            row = 3,
            column = 0,
            sticky = 'w' ,
            pady = ( 25 , 25),
            padx = ( 40, 0 ),
        )

        self.running_containers = ctk.CTkCheckBox(
            self.left_info_frame ,
            text = "Running Containers",
            onvalue = "on",
            offvalue = "off",
            font = ctk.CTkFont(
            size=15,
            )
        )
        self.running_containers.grid(
            row = 3,
            column = 1,
            sticky = 'w' ,
            pady = ( 25 , 25),
            padx = ( 10, 0 ),
        )

        self.container_enter = ctk.CTkEntry(
            self.left_info_frame,
            placeholder_text = "Container ID or Name",
            width = 50,
            height = 50,
            font = ctk.CTkFont( size=14 ),
            corner_radius = 10,
        )
        self.container_enter.grid( 
            row = 4,
            column = 0,
            columnspan = 2,
            sticky = 'we' ,
            pady = ( 5 , 0 ),
            padx = ( 10, 10 ),
        )

        self.docker_inspect = ctk.CTkCheckBox(
            self.left_info_frame ,
            text = "Container logs",
            onvalue = "on",
            offvalue = "off",
            font = ctk.CTkFont(
            size=15,
            )
        )
        self.docker_inspect.grid(
            row = 5,
            column = 0,
            sticky = 'w' ,
            pady = ( 25 , 25),
            padx = ( 10, 0 ),
        )

        self.docker_network = ctk.CTkCheckBox(
            self.left_info_frame ,
            text = "Container Inspect",
            onvalue = "on",
            offvalue = "off",
            font = ctk.CTkFont(
            size=15,
            )
        )

        self.docker_network.grid(
            row = 5,
            column = 1,
            sticky = 'w' ,
            pady = ( 25 , 0),
            padx = ( 40, 0 ),
        )

        self.docker_network_inspect = ctk.CTkCheckBox(
            self.left_info_frame ,
            text = "Network Inspect",
            onvalue = "on",
            offvalue = "off",
            font = ctk.CTkFont(
            size=15,
            )
        )
        self.docker_network_inspect.grid(
            row = 6,
            column = 0,
            sticky = 'w' ,
            pady = ( 25 , 0),
            padx = ( 10, 0 ),
        )
        self.check_it_out = ctk.CTkButton( 
            self.left_info_frame, 
            text="CHECK IT OUT!",
            width = 250,
            height = 50,
            font = ctk.CTkFont( "Segoe Script", 20 ),
        )
        self.check_it_out.grid( 
            row = 7,
            column = 0,
            columnspan = 2,
            sticky = 'we' ,
            pady = ( 35 , 0 ),
            padx = ( 10, 10 ),
        )

##### Right Frame
        self.id_label = ctk.CTkLabel(
            self.right_info_frame,
            text = "Check Container ID",
            font = ctk.CTkFont(
                family="Courier New",
                size=18,
                weight="bold",
                overstrike=False
            )
        )
        self.id_label.grid(
            column = 0,
            row = 0,
            columnspan = 2,
            pady = ( 20, 0 ),
            padx = ( 10, 10 ),
            sticky = 'ew',
        )

        # For demo Only
        test_id_list = [
            [ "ID", "Names" ],
            [ '2b7c51034242', 'nginx02' ],
            [ '2b7c51034242', 'nginx01' ],
            [ '2b7c51034242', 'my_web_server' ],
            [ '2b7c51034242', 'ubuntu02' ],
            [ '2b7c51034242', 'ubuntu01' ],
        ]

        self.check_id_table = CTkTable( 
                master = self.right_info_frame,
                # header_color = '',
                values = test_id_list,
                hover_color = 'gray20',
                width = 180
            )
        self.check_id_table.grid(
            row = 1,
            column = 0,
            columnspan = 2,
            padx= ( 10, 0 ),
            pady = ( 10, 0 ),
            sticky = "ew"            
        )

        self.network_label = ctk.CTkLabel(
            self.right_info_frame,
            text = "Check Network",
            font = ctk.CTkFont(
                family="Courier New",
                size=18,
                weight="bold",
                overstrike=False
            )
        )

        self.network_label.grid(
            row = 2,
            column = 0,
            columnspan = 2,
            pady = ( 30, 0 ),
            padx = ( 10, 10 ),
            sticky = 'ew',
        )
        
        test_network_list = [
            [ "Network ID", "Names" ],
            [ '41ecd807f659', 'docker_network_123' ],
            [ '22a4550ffe7a', 'bridge' ],
            [ '10f57fa303b9', 'host' ],
            [ 'c683be21172b', 'my_docker_network' ],
            [ '2b7ee5201314', 'nonw' ],
        ]

        self.test_network_list = CTkTable( 
                master = self.right_info_frame,
                # header_color = '',
                values = test_network_list,
                hover_color = 'gray20',
                width = 180
            )
        self.test_network_list.grid(
            row = 3,
            column = 0,
            columnspan = 2,
            padx= ( 10, 0 ),
            pady = ( 10, 0 ),
            sticky = "ew"            
        )
