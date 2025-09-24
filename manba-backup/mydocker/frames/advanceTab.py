import customtkinter as ctk
from CTkTable import *

class DockerAdvanceTab( ) :
    def __init__( self, docker_tab ) :
        self.advance_tab = docker_tab.add( 'Advance' )
        self.setup_ui( )

    def setup_ui( self ) :
        self.advance_label = ctk.CTkLabel(
            self.advance_tab,
            text = "Hello! Here is the magic begin ~",
            font = ctk.CTkFont(
                family="Courier New",
                size=16,
                weight="bold",
                slant="italic",
                underline=True,
                overstrike=False
            )
        )

        self.advance_label.pack(
            pady = 5 ,
            padx = 5 ,
        )

        self.left_frame = ctk.CTkFrame(
            self.advance_tab,
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
            self.advance_tab,
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
        self.left_frame.grid_rowconfigure( 2, weight = 0 )
        self.left_frame.grid_rowconfigure( 3, weight = 0 )
        self.left_frame.grid_rowconfigure( 4, weight = 0 )
        self.left_frame.grid_rowconfigure( 5, weight = 0 )
        self.left_frame.grid_rowconfigure( 6, weight = 0 )
        self.left_frame.grid_rowconfigure( 7, weight = 0 )

        self.install_label = ctk.CTkLabel(
            self.left_frame,
            text = "What you want to install? >_<* ",
            font = ctk.CTkFont(
                family="Courier New",
                size=16,
                weight="bold",
                overstrike=False
            )
        )
        self.install_label.grid(
            column = 0,
            row = 0,
            columnspan = 2,
            pady = ( 20, 20 ),
            padx = ( 10, 10 ),
            sticky = 'ew',
        )

### Check Box
        self.net_tools = ctk.CTkCheckBox(
            self.left_frame ,
            text = "Net-tools",
            onvalue = "on",
            offvalue = "off",
            font = ctk.CTkFont(
                size=15,
            )
        )
        self.net_tools.grid(
            row = 1,
            column = 0,
            sticky = 'w' ,
            pady = ( 20, 20 ),
            padx = ( 40, 0 ),
        )

        self.iputils_ping = ctk.CTkCheckBox(
            self.left_frame ,
            text = "Iputils",
            onvalue = "on",
            offvalue = "off",
            font = ctk.CTkFont(
                size=15,
            )
        )

        self.iputils_ping.grid(
            row = 1,
            column = 1,
            sticky = 'w' ,
            pady = ( 20, 20 ),
            padx = ( 10, 20 ),
        )

        self.sudo = ctk.CTkCheckBox(
            self.left_frame ,
            text = "Sudo",
            onvalue = "on",
            offvalue = "off",
            font = ctk.CTkFont(
            size=15,
            )
        )

        self.sudo.grid(
            row = 2,
            column = 0,
            sticky = 'w' ,
            pady = ( 20, 20 ),
            padx = ( 40, 0 ),
        )

        self.openssh_client = ctk.CTkCheckBox(
            self.left_frame ,
            text = "Openssh-client",
            onvalue = "on",
            offvalue = "off",
            font = ctk.CTkFont(
            size=15,
            )
        )
        self.openssh_client.grid(
            row = 2,
            column = 1,
            sticky = 'w' ,
            pady = ( 20, 20 ),
            padx = ( 10, 0 ),
        )

        self.python3 = ctk.CTkCheckBox(
            self.left_frame ,
            text = "Python3",
            onvalue = "on",
            offvalue = "off",
            font = ctk.CTkFont(
            size=15,
            )
        )

        self.python3.grid(
            row = 3,
            column = 0,
            sticky = 'w' ,
            pady = ( 20, 20 ),
            padx = ( 40, 0 ),
        )

        self.wget = ctk.CTkCheckBox(
            self.left_frame ,
            text = "Wget",
            onvalue = "on",
            offvalue = "off",
            font = ctk.CTkFont(
            size=15,
            )
        )
        self.wget.grid(
            row = 3,
            column = 1,
            sticky = 'w' ,
            pady = ( 20, 20 ),
            padx = ( 10, 0 ),
        )

        self.container_config = ctk.CTkLabel(
            self.left_frame,
            text = "Container Configuration ",
            font = ctk.CTkFont(
                family = "Courier New",
                size = 16,
                weight = "bold",
                overstrike = False
            )
        )
        self.container_config.grid(
            column = 0,
            row = 4,
            columnspan = 2,
            pady = ( 20, 20 ),
            padx = ( 10, 10 ),
            sticky = 'ew',
        )

        self.container_name = ctk.CTkCheckBox(
            self.left_frame ,
            text = "Container Name:",
            onvalue = "on",
            offvalue = "off",
            font = ctk.CTkFont(
            size=15,
            )
        )
        self.container_name.grid(
            row = 5,
            column = 0,
            sticky = 'w' ,
            pady = ( 20, 20 ),
            padx = ( 40, 0 ),
        )

        self.container_name_entry = ctk.CTkEntry(
            self.left_frame ,
            placeholder_text = "ID or Name",
            font = ctk.CTkFont(
                size=15,
            )
        )

        self.container_name_entry.grid(
            row = 5,
            column = 1,
            sticky = 'we' ,
            pady = ( 20, 20 ),
            padx = ( 10, 20 ),
        )

        self.ip_address = ctk.CTkCheckBox(
            self.left_frame ,
            text = "IP address:",
            onvalue = "on",
            offvalue = "off",
            font = ctk.CTkFont(
            size=15,
            )
        )
        self.ip_address.grid(
            row = 6,
            column = 0,
            sticky = 'w' ,
            pady = ( 20, 20 ),
            padx = ( 40, 0 ),
        )

        self.ip_address_entry = ctk.CTkEntry(
            self.left_frame ,
            placeholder_text = "IP address",
            font = ctk.CTkFont(
                size=15,
            )
        )

        self.ip_address_entry.grid(
            row = 6,
            column = 1,
            sticky = 'we' ,
            pady = ( 20, 20 ),
            padx = ( 10, 20 ),
        )

        self.go_install = ctk.CTkButton( 
            self.left_frame, 
            text="$.$ Go Install $.$",
            width = 200,
            height = 40,
            font = ctk.CTkFont( "Segoe Script", 18 ),
        )

        self.go_install.grid( 
            row = 7,
            column = 0,
            columnspan = 2,
            sticky = 'we' ,
            pady = ( 35 , 10 ),
            padx = ( 10, 10 ),
        )
        self.clear_btn = ctk.CTkButton( 
            self.left_frame, 
            text="@_@ CLEAR @_@",
            width = 200,
            height = 40,
            font = ctk.CTkFont( "Segoe Script", 18 ),
        )
        self.clear_btn.grid( 
            row = 8,
            column = 0,
            columnspan = 2,
            sticky = 'we' ,
            pady = ( 35 , 10 ),
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
