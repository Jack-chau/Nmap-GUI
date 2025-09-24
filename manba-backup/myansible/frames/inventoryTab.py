import customtkinter as ctk
from CTkTable import *

class AnsibleInventoryTab :
    
    def __init__( self, ansible_tab ) :
        self.ansible_tab = ansible_tab.add( 'Inventory' )
        self._setup_ui( )

    def _setup_ui( self ) :

        self.ansible_label = ctk.CTkLabel(
            self.ansible_tab,
            text = "Create Inventory File ",
            font = ctk.CTkFont(
                family="Courier New",
                size=30,
                weight="bold",
                slant="italic",
                underline=True,
                overstrike=False
            )
        )

        self.ansible_label.pack(
            pady = 5 ,
            padx = 5 ,
        )

        self.left_frame = ctk.CTkFrame(
            self.ansible_tab,
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
            self.ansible_tab,
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
        self.left_frame.grid_rowconfigure( 6, weight = 1 )
        self.left_frame.grid_rowconfigure( 7, weight = 1 )

        self.inventory_label = ctk.CTkLabel(
            self.left_frame,
            text = "Custom Inventory File",
            font = ctk.CTkFont(
                family="Courier New",
                size=18,
                weight="bold",
                overstrike=False
            )
        )
        self.inventory_label.grid(
            column = 0,
            row = 0,
            columnspan = 2,
            pady = ( 10, 0 ),
            padx = ( 10, 10 ),
            sticky = 'ew',
        )

### Add Section Container
        self.section_label = ctk.CTkLabel(
            self.left_frame,
            text = "Add Section: ",
            font = ctk.CTkFont(
                family="Arial",
                size=16,
                weight="bold",
                overstrike=False
            )
        )

        self.section_label.grid(
            column = 0,
            row = 1,
            sticky = 'w' ,
            pady = ( 5 , 0 ),
            padx = ( 40, 0 ),
        )

        self.section_entry = ctk.CTkEntry(
            self.left_frame ,
            placeholder_text = "Section:",
            font = ctk.CTkFont(
                size=15,
            )
        )

        self.section_entry.grid(
            row = 1,
            column = 1,
            sticky = 'we' ,
            pady = ( 5 , 0 ),
            padx = ( 0, 20 ),
        )

        self.ip_label = ctk.CTkLabel(
            self.left_frame,
            text = "Static IP: ",
            font = ctk.CTkFont(
                family="Arial",
                size=16,
                weight="bold",
                overstrike=False
            )
        )

        self.ip_label.grid(
            column = 0,
            row = 2,
            sticky = 'w' ,
            pady = ( 5 , 0 ),
            padx = ( 40, 0 ),
        )

        self.ip_entry = ctk.CTkEntry(
            self.left_frame ,
            placeholder_text = "172.18.0.10",
            font = ctk.CTkFont(
                size=15,
            )
        )

        self.ip_entry.grid(
            row = 2,
            column = 1,
            sticky = 'we' ,
            pady = ( 5 , 0 ),
            padx = ( 0, 20 ),
        )

        self.user_label = ctk.CTkLabel(
            self.left_frame,
            text = "User Name: ",
            font = ctk.CTkFont(
                family="Arial",
                size=16,
                weight="bold",
                overstrike=False
            )
        )

        self.user_label.grid(
            column = 0,
            row = 3,
            sticky = 'w' ,
            pady = ( 5 , 0 ),
            padx = ( 40, 0 ),
        )

        self.user_entry = ctk.CTkEntry(
            self.left_frame ,
            placeholder_text = "User name",
            font = ctk.CTkFont(
                size=15,
            )
        )

        self.user_entry.grid(
            row = 3,
            column = 1,
            sticky = 'we' ,
            pady = ( 5 , 0 ),
            padx = ( 0, 20 ),
        )

        self.user_password_label = ctk.CTkLabel(
            self.left_frame,
            text = "Password: ",
            font = ctk.CTkFont(
                family="Arial",
                size=16,
                weight="bold",
                overstrike=False
            )
        )

        self.user_password_label.grid(
            column = 0,
            row = 4,
            sticky = 'w' ,
            pady = ( 5 , 0 ),
            padx = ( 40, 0 ),
        )

        self.user_password_entry = ctk.CTkEntry(
            self.left_frame ,
            placeholder_text = "password",
            font = ctk.CTkFont(
                size=15,
            )
        )

        self.user_password_entry.grid(
            row = 4,
            column = 1,
            sticky = 'we' ,
            pady = ( 5 , 0 ),
            padx = ( 0, 20 ),
        )

        self.file_name_label = ctk.CTkLabel(
            self.left_frame,
            text = "File Name: ",
            font = ctk.CTkFont(
                family="Arial",
                size=16,
                weight="bold",
                overstrike=False
            )
        )

        self.file_name_label.grid(
            column = 0,
            row = 5,
            sticky = 'w' ,
            pady = ( 5 , 0 ),
            padx = ( 40, 0 ),
        )

        self.file_name_entry = ctk.CTkEntry(
            self.left_frame ,
            placeholder_text = "New File name",
            font = ctk.CTkFont(
                size=15,
            )
        )
        self.file_name_entry.grid(
            row = 5,
            column = 1,
            sticky = 'we' ,
            pady = ( 5 , 0 ),
            padx = ( 0, 20 ),
        )

        self.run_btn = ctk.CTkButton( 
            self.left_frame, 
            text="Run",
            width = 150,
            height = 40,
            font = ctk.CTkFont( "Segoe Script", 15 ),
        )
        self.run_btn.grid( 
            row = 6,
            column = 0,
            # columnspan = 2,
            sticky = 'e' ,
            pady = ( 10 , 0 ),
            padx = ( 0, 8 ),
        )

        self.read_btn = ctk.CTkButton( 
            self.left_frame, 
            text="Read file",
            width = 150,
            height = 40,
            font = ctk.CTkFont( "Segoe Script", 15 ),
        )
        self.read_btn.grid( 
            row = 6,
            column = 1,
            # columnspan = 2,
            sticky = 'e' ,
            pady = ( 10 , 0 ),
            padx = ( 8, 20 ),
        )

        self.save_btn = ctk.CTkButton( 
            self.left_frame, 
            text="Save",
            width = 150,
            height = 40,
            font = ctk.CTkFont( "Segoe Script", 15 ),
        )
        self.save_btn.grid( 
            row = 7,
            column = 0,
            # columnspan = 2,
            sticky = 'e' ,
            pady = ( 10 , 0 ),
            padx = ( 0, 8 ),
        )

        self.clear_btn = ctk.CTkButton( 
            self.left_frame, 
            text="Clear",
            width = 150,
            height = 40,
            font = ctk.CTkFont( "Segoe Script", 15 ),
        )
        self.clear_btn.grid( 
            row = 7,
            column = 1,
            # columnspan = 2,
            sticky = 'e' ,
            pady = ( 10 , 0 ),
            padx = ( 8 , 20 ),
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
            [ "idx", "container", 'network', "ip"],
            [ '1', 'ubuntu', 'jack-net', '172.18.0.10' ],
            [ '2', 'nginx', 'bridge', '172.18.0.11' ],
            [ '3', 'kkpark', 'jack-net', '172.18.0.12' ],
            [ '4', 'kali', 'bridge', '172.18.0.13' ],
            [ '5', 'my-web-server', 'abc', '172.18.0.14' ],
            [ '6', 'omygod', 'my-net', '172.18.0.15' ],
            [ '7', 'yea', 'neta', '172.18.0.16' ],
            [ '8', 'IamRich', 'netb', '172.18.0.17' ],
            [ '9', 'Sick', 'netc', '172.18.0.18' ],
            [ '10', 'IamChamp', 'netnetnet', '172.18.0.19' ],
            [ '11', 'JackIsCool', 'Unet', '172.18.0.20' ],
            [ '12', 'JackIsMe', 'mynet', '172.18.0.21' ],
            [ '13', 'WhatUp', 'anet', '172.18.0.21' ],
            [ '14', 'Hello-World', 'cnet', '172.18.0.23' ],
            [ '15', 'UareStupid', 'nonet', '172.18.0.14' ],
        ]

        self.show_ansible_table = CTkTable( 
                master = self.right_frame,
                values = test_container_list,
                width = 100
            )
        self.show_ansible_table.grid(
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