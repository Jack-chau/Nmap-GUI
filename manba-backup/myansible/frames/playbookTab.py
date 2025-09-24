import customtkinter as ctk
from CTkTable import *

class AnsiblePlaybookTab :
    
    def __init__( self, ansible_tab ) :
        self.ansible_tab = ansible_tab.add( 'Playbook' )
        self._setup_ui( )

    def _setup_ui( self ) :

        self.ansible_label = ctk.CTkLabel(
            self.ansible_tab,
            text = "PlayBook Page",
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

        self.playbook_label = ctk.CTkLabel(
            self.left_frame,
            text = "Run Playbook",
            font = ctk.CTkFont(
                family="Courier New",
                size=25,
                weight="bold",
                overstrike=False
            )
        )
        self.playbook_label.grid(
            column = 0,
            row = 0,
            columnspan = 2,
            pady = ( 10, 0 ),
            padx = ( 10, 10 ),
            sticky = 'ew',
        )

### Add Section Container
        self.inventory_label = ctk.CTkLabel(
            self.left_frame,
            text = "Inventory file: ",
            font = ctk.CTkFont(
                family="Arial",
                size=25,
                weight="bold",
                overstrike=False
            )
        )

        self.inventory_label.grid(
            column = 0,
            row = 1,
            sticky = 'w' ,
            pady = ( 10 , 0 ),
            padx = ( 30, 0 ),
        )

        self.inventory_entry = ctk.CTkEntry(
            self.left_frame ,
            placeholder_text = "Inventory file",
            font = ctk.CTkFont(
                size=15,
            )
        )

        self.inventory_entry.grid(
            row = 1,
            column = 1,
            sticky = 'we' ,
            pady = ( 10 , 0 ),
            padx = ( 0, 20 ),
        )

        self.playbook_label = ctk.CTkLabel(
            self.left_frame,
            text = "Playbook File: ",
            font = ctk.CTkFont(
                family="Arial",
                size=25,
                weight="bold",
                overstrike=False
            )
        )

        self.playbook_label.grid(
            column = 0,
            row = 2,
            sticky = 'w' ,
            pady = ( 10 , 0 ),
            padx = ( 30, 0 ),
        )

        self.playbook_entry = ctk.CTkEntry(
            self.left_frame ,
            placeholder_text = "playbook file",
            font = ctk.CTkFont(
                size=15,
            )
        )

        self.playbook_entry.grid(
            row = 2,
            column = 1,
            sticky = 'we' ,
            pady = ( 10 , 0 ),
            padx = ( 0, 20 ),
        )

        self.ping_btn = ctk.CTkButton( 
            self.left_frame, 
            text="Try Ping",
            width = 150,
            height = 40,
            font = ctk.CTkFont( "Segoe Script", 15 ),
        )
        self.ping_btn.grid( 
            row = 3,
            column = 0,
            # columnspan = 2,
            sticky = 'e' ,
            pady = ( 10 , 0 ),
            padx = ( 0, 8 ),
        )

        self.run_playbook_btn = ctk.CTkButton( 
            self.left_frame, 
            text="Run Playbook",
            width = 150,
            height = 40,
            font = ctk.CTkFont( "Segoe Script", 15 ),
        )
        self.run_playbook_btn.grid( 
            row = 3,
            column = 1,
            # columnspan = 2,
            sticky = 'e' ,
            pady = ( 10 , 0 ),
            padx = ( 8, 20 ),
        )

##### Right Frame
        self.inventory_label = ctk.CTkLabel(
            self.right_frame,
            text = "Inventory Files",
            font = ctk.CTkFont(
                family="Courier New",
                size=16,
                weight="bold",
                overstrike=False
            )
        )
        self.inventory_label.grid(
            column = 0,
            row = 0,
            columnspan = 2,
            pady = ( 20, 0 ),
            padx = ( 10, 10 ),
            sticky = 'ew',
        )

        # For demo Only
        test_id_list = [
            [ 'idx', "File name", ],
            [ '1', 'inventory.ini' ],
            [ '2', 'myinventory.ini' ],
            [ '3', 'webUpdate.ini' ],
            [ '4', 'jackInventory.ini' ],
            [ '5', 'StupidMe.ini' ],
        ]

        self.inventory_table = CTkTable( 
                master = self.right_frame,
                values = test_id_list,
                width = 200
            )
        self.inventory_table.grid(
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


        self.playbook_label = ctk.CTkLabel(
            self.right_frame,
            text = "Playbook Files",
            font = ctk.CTkFont(
                family="Courier New",
                size=16,
                weight="bold",
                overstrike=False
            )
        )

        self.playbook_label.grid(
            row = 3,
            column = 0,
            columnspan = 2,
            pady = ( 30, 0 ),
            padx = ( 10, 10 ),
            sticky = 'ew',
        )
        
        playbook_list = [
            [ 'idx', "Playbook files" ],
            [ '1', 'myPlaybook.yaml' ],
            [ '2', 'BadBoyJack.yaml' ],
            [ '3', 'UpdateWeb.yaml' ],
            [ '4', 'LoveScience.yaml' ],
            [ '5', 'BelieveLove.yaml' ],
        ]

        self.playbook_list_table = CTkTable( 
                master = self.right_frame,
                values = playbook_list,
                width = 200
            )
        self.playbook_list_table.grid(
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