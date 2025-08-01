import customtkinter as ctk
from CTkTable import *
import webbrowser

class DockerNetworkTab :
    def __init__( self, docker_tab ) :
        self.network_tab = docker_tab.add( 'network' )
        self._setup_ui( )

    def _setup_ui( self ) :

        self.network_label = ctk.CTkLabel(
            self.network_tab,
            text = "Docker network Management",
            font = ctk.CTkFont(
                family="Courier New",
                size=16,
                weight="bold",
                slant="italic",
                underline=True,
                overstrike=False
            )
        )

        self.network_label.pack(
            pady = 5 ,
            padx = 5 ,
        )

        self.left_frame = ctk.CTkFrame(
            self.network_tab,
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
            self.network_tab,
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
        self.left_frame.grid_rowconfigure( 0, weight = 0 )
        self.left_frame.grid_rowconfigure( 1, weight = 0 )
        self.left_frame.grid_rowconfigure( 2, weight = 0 )
        self.left_frame.grid_rowconfigure( 3, weight = 0 )
        self.left_frame.grid_rowconfigure( 4, weight = 0 )
        self.left_frame.grid_rowconfigure( 5, weight = 0 )
        self.left_frame.grid_rowconfigure( 6, weight = 0 )
        self.left_frame.grid_rowconfigure( 7, weight = 0 )
        self.left_frame.grid_rowconfigure( 8, weight = 0 )
        self.left_frame.grid_rowconfigure( 9, weight = 0 )
        self.left_frame.grid_rowconfigure( 10, weight = 0 )

        self.network_label = ctk.CTkLabel(
            self.left_frame,
            text = "Container Network Configuration",
            font = ctk.CTkFont(
                family="Courier New",
                size=18,
                weight="bold",
                overstrike=False
            )
        )
        self.network_label.grid(
            column = 0,
            row = 0,
            columnspan = 2,
            pady = ( 20, 0 ),
            padx = ( 10, 10 ),
            sticky = 'ew',
        )

### Create Docker network
        self.network_assign_label = ctk.CTkLabel(
            self.left_frame,
            text = "Choose the container ",
            font = ctk.CTkFont(
                family="Arial",
                size=16,
                weight="bold",
                overstrike=False
            )
        )

        self.network_assign_label.grid(
            row = 1,
            column = 0,
            sticky = 'w' ,
            pady = ( 25 , 0 ),
            padx = ( 40, 0 ),
        )

        self.network_assign_entry = ctk.CTkEntry(
            self.left_frame ,
            placeholder_text = "container idx",
            font = ctk.CTkFont(
                size=15,
            )
        )

        self.network_assign_entry.grid(
            row = 1,
            column = 1,
            sticky = 'we' ,
            pady = ( 25 , 0 ),
            padx = ( 0, 20 ),
        )
#
        self.network_choice_entry = ctk.CTkLabel(
            self.left_frame,
            text = "Choose Network: ",
            font = ctk.CTkFont(
                family="Arial",
                size=16,
                weight="bold",
                overstrike=False
            )
        )

        self.network_choice_entry.grid(
            row = 2,
            column = 0,
            sticky = 'w' ,
            pady = ( 25 , 0 ),
            padx = ( 40, 0 ),
        )

        self.network_choice_entry = ctk.CTkEntry(
            self.left_frame ,
            placeholder_text = "my_docker_network",
            font = ctk.CTkFont(
                size=15,
            )
        )

        self.network_choice_entry.grid(
            row = 2,
            column = 1,
            sticky = 'we' ,
            pady = ( 25 , 0 ),
            padx = ( 0, 20 ),
        )

        self.network_static_ip_label = ctk.CTkLabel(
            self.left_frame,
            text = "Static IP:",
            font = ctk.CTkFont(
                family="Arial",
                size=16,
                weight="bold",
                overstrike=False
            )
        )

        self.network_static_ip_label.grid(
            row = 3,
            column = 0,
            sticky = 'w' ,
            pady = ( 25 , 0 ),
            padx = ( 40, 0 ),
        )

        self.network_static_ip_entry = ctk.CTkEntry(
            self.left_frame ,
            placeholder_text = "172.18.0.xxx",
            font = ctk.CTkFont(
                size=15,
            )
        )

        self.network_static_ip_entry.grid(
            row = 3,
            column = 1,
            sticky = 'we' ,
            pady = ( 25 , 0 ),
            padx = ( 0, 20 ),
        )
        ##
        self.port_label = ctk.CTkLabel(
            self.left_frame,
            text = "Port:",
            font = ctk.CTkFont(
                family="Arial",
                size=16,
                weight="bold",
                overstrike=False
            )
        )

        self.port_label.grid(
            row = 4,
            column = 0,
            sticky = 'w' ,
            pady = ( 25 , 0 ),
            padx = ( 40, 0 ),
        )

        self.port_entry = ctk.CTkEntry(
            self.left_frame ,
            placeholder_text = "8080",
            font = ctk.CTkFont(
                size=15,
            )
        )

        self.port_entry.grid(
            row = 4,
            column = 1,
            sticky = 'we' ,
            pady = ( 25 , 0 ),
            padx = ( 0, 20 ),
        )

        self.network_setting_label = ctk.CTkLabel(
            self.left_frame,
            text = "Create Docker Network",
            font = ctk.CTkFont(
                family="Courier New",
                size=18,
                weight="bold",
                overstrike=False
            )
        )
        self.network_setting_label.grid(
            row =5,
            column = 0,
            columnspan = 2,
            sticky = 'ew' ,
            pady = ( 25 , 0 ),
            padx = ( 10, 10 ),
        )

        self.create_network_label = ctk.CTkLabel(
            self.left_frame,
            text = "Create docker network:",
            font = ctk.CTkFont(
                family="Arial",
                size = 16,
                weight="bold",
                overstrike=False
            )
        )
        self.create_network_label.grid(
            row =6,
            column = 0,
            sticky = 'w' ,
            pady = ( 25 , 0 ),
            padx = ( 40, 0 ),
        )

        self.create_network_entry = ctk.CTkEntry(
            self.left_frame ,
            placeholder_text = "New network name",
            font = ctk.CTkFont(
                size=15,
            )
        )

        self.create_network_entry.grid(
            row = 6,
            column = 1,
            sticky = 'we' ,
            pady = ( 25 , 0 ),
            padx = ( 0, 20 ),
        )

#####
        self.network_subnet_label = ctk.CTkLabel(
            self.left_frame,
            text = "Subnet:",
            font = ctk.CTkFont(
                family="Arial",
                size = 16,
                weight="bold",
                overstrike=False
            )
        )
        self.network_subnet_label.grid(
            row = 7,
            column = 0,
            sticky = 'w' ,
            pady = ( 25 , 0 ),
            padx = ( 40, 0 ),
        )

        self.network_subnet_entry = ctk.CTkEntry(
            self.left_frame ,
            placeholder_text = "172.18.0.0/16",
            font = ctk.CTkFont(
                size=15,
            )
        )

        self.network_subnet_entry.grid(
            row = 7,
            column = 1,
            sticky = 'we' ,
            pady = ( 25 , 0 ),
            padx = ( 0, 20 ),
        )

        self.network_gateway_label = ctk.CTkLabel(
            self.left_frame,
            text = "Gateway:",
            font = ctk.CTkFont(
                family="Arial",
                size = 16,
                weight="bold",
                overstrike=False
            )
        )
        self.network_gateway_label.grid(
            row =8,
            column = 0,
            sticky = 'w' ,
            pady = ( 25 , 0 ),
            padx = ( 40, 0 ),
        )

        self.network_gateway_entry = ctk.CTkEntry(
            self.left_frame ,
            placeholder_text = "172.18.0.1",
            font = ctk.CTkFont(
                size=15,
            )
        )

        self.network_gateway_entry.grid(
            row = 8,
            column = 1,
            sticky = 'we' ,
            pady = ( 25 , 0 ),
            padx = ( 0, 20 ),
        )




        self.network_delete = ctk.CTkLabel(
            self.left_frame,
            text = "Delete Docker Network",
            font = ctk.CTkFont(
                family="Courier New",
                size=18,
                weight="bold",
                overstrike=False
            )
        )
        self.network_delete.grid(
            row =9,
            column = 0,
            columnspan = 2,
            sticky = 'ew' ,
            pady = ( 25 , 0 ),
            padx = ( 10, 10 ),
        )

        self.network_delete_label = ctk.CTkLabel(
            self.left_frame,
            text = "Delete network:",
            font = ctk.CTkFont(
                family="Arial",
                size = 16,
                weight="bold",
                overstrike=False
            )
        )
        self.network_delete_label.grid(
            row =10,
            column = 0,
            sticky = 'w' ,
            pady = ( 25 , 0 ),
            padx = ( 40, 0 ),
        )

        self.network_delete_entry = ctk.CTkEntry(
            self.left_frame ,
            placeholder_text = "network idx",
            font = ctk.CTkFont(
                size=15,
            )
        )

        self.network_delete_entry.grid(
            row = 10,
            column = 1,
            sticky = 'we' ,
            pady = ( 25 , 0 ),
            padx = ( 0, 20 ),
        )

        self.network_execute = ctk.CTkButton( 
            self.left_frame, 
            text="Execute",
            width = 250,
            height = 50,
            font = ctk.CTkFont( "Segoe Script", 20 ),
        )
        self.network_execute.grid( 
            row = 11,
            column = 0,
            columnspan = 2,
            sticky = 'we' ,
            pady = ( 20 , 10 ),
            padx = ( 10, 10 ),
        )

##### Right Frame
        self.id_label = ctk.CTkLabel(
            self.right_frame,
            text = "Container ID",
            font = ctk.CTkFont(
                family="Courier New",
                size=16,
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
            [ 'idx', "ID", "Names" ],
            [ '1', '2b7c51034242', 'nginx02' ],
            [ '2', '2b7c51034242', 'nginx01' ],
            [ '3', '2b7c51034242', 'my_web_server' ],
            [ '4', '2b7c51034242', 'ubuntu02' ],
            [ '5', '2b7c51034242', 'ubuntu01' ],
        ]

        self.check_id_table = CTkTable( 
                master = self.right_frame,
                values = test_id_list,
                width = 80
            )
        self.check_id_table.grid(
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


        self.network_label = ctk.CTkLabel(
            self.right_frame,
            text = "Docker Network",
            font = ctk.CTkFont(
                family="Courier New",
                size=16,
                weight="bold",
                overstrike=False
            )
        )

        self.network_label.grid(
            row = 3,
            column = 0,
            columnspan = 2,
            pady = ( 30, 0 ),
            padx = ( 10, 10 ),
            sticky = 'ew',
        )
        
        test_network_list = [
            [ 'idx',"Network ID", "Names" ],
            [ '1','41ecd807f659', 'docker_network_123' ],
            [ '2','22a4550ffe7a', 'bridge' ],
            [ '3','10f57fa303b9', 'host' ],
            [ '4','c683be21172b', 'my_docker_network' ],
            [ '5','2b7ee5201314', 'nonw' ],
        ]

        self.test_network_list = CTkTable( 
                master = self.right_frame,
                values = test_network_list,
                width = 130
            )
        self.test_network_list.grid(
            row = 4,
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
            row = 5,
            column = 0,
            columnspan = 2,
            sticky = 'e' ,
            pady = ( 35 , 0 ),
            padx = ( 10, 0 ),
        )
