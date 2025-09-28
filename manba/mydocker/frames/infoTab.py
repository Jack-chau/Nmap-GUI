import customtkinter as ctk
from CTkTable import *

class DockerInfoTab( ) :
    def __init__( self, docker_tab ) :
        self.info_tab = docker_tab.add( 'Info' )
        self.setup_ui( )

    def setup_ui( self ) :
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

        self.left_frame = ctk.CTkFrame(
            self.info_tab,
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
            self.info_tab,
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
        self.left_frame.grid_columnconfigure( 1, weight = 1 )
        self.left_frame.grid_rowconfigure( 0, weight = 0 )
        self.left_frame.grid_rowconfigure( 1, weight = 0 )
        # self.left_frame.grid_rowconfigure( 2, weight = 0 )
        # self.left_frame.grid_rowconfigure( 3, weight = 0 )
        # self.left_frame.grid_rowconfigure( 4, weight = 0 )
        # self.left_frame.grid_rowconfigure( 5, weight = 0 )
        # self.left_frame.grid_rowconfigure( 6, weight = 0 )
        # self.left_frame.grid_rowconfigure( 7, weight = 0 )

        self.id_label = ctk.CTkLabel(
            self.left_frame,
            text = "Running Container",
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
            [ '6', '2b7c51034242', 'nginx02' ],
            [ '7', '2b7c51034242', 'nginx01' ],
            [ '8', '2b7c51034242', 'my_web_server' ],
            [ '9', '2b7c51034242', 'ubuntu02' ],
            [ '10', '2b7c51034242', 'ubuntu01' ],
            [ '11', '2b7c51034242', 'my_web_server' ],
            [ '12', '2b7c51034242', 'ubuntu02' ],
            [ '13', '2b7c51034242', 'ubuntu01' ],
        ]

        self.check_id_table = CTkTable( 
                master = self.left_frame,
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
            self.left_frame, 
            text="Refresh",
            width = 130,
            height = 30,
            font = ctk.CTkFont( "Segoe Script", 15 ),
        )
        self.refrash_btn.grid( 
            row = 3,
            column = 0,
            columnspan = 2,
            sticky = 'e' ,
            pady = ( 35 , 0 ),
            padx = ( 10, 10 ),
        )


# ### Check Box

##### Right Frame

        self.show_image_label = ctk.CTkLabel(
            self.right_frame,
            text = "Docker image information",
            font = ctk.CTkFont(
                family="Courier New",
                size=18,
                weight="bold",
                overstrike=False
            )
        )
        self.show_image_label.grid(
            column = 0,
            row = 0,
            columnspan = 2,
            pady = ( 20, 0 ),
            padx = ( 10, 10 ),
            sticky = 'ew',
        )

        # For demo Only
        test_image_list = [
            [ 'idx',"ID", "Names" ,"Tag"],
            [ '1','2b7c51034242', 'hello', 'latest' ],
            [ '2','2b7c51034242', 'ubuntu', 'latest' ],
            [ '3','2b7c51034242', 'nginx', 'alpine' ],
            [ '4','2b7c51034242', 'nginx', 'latest' ],
            [ '5','2b7c51034242', 'hello-world', 'latest' ],
        ]

        self.show_image_table = CTkTable( 
                master = self.right_frame,
                # header_color = '',
                values = test_image_list,
                width = 100
            )
        self.show_image_table.grid(
            row = 1,
            column = 0,
            columnspan = 2,
            padx= ( 40, 0 ),
            pady = ( 10, 0 ),
            sticky = "nsew"            
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
