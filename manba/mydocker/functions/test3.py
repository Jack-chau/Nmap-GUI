import customtkinter as ctk
from tkinter import messagebox

class CheckboxTableApp( ctk.CTk ):
    def __init__( self ) :
        self.title( "Checkbox Table Example" )
        self.geometry( "600x400" )

        # Configure grid layout
        self.grid.columnconfigure( 0, weight = 1)
        self.grid.rowconfigure( 1, weight = 1 )

        self.create_table( )

        self.get_selected_button = ctk.CTkButton(
            self,
            text = "Get Selected",
            command = self.get_selected_items
        )
        self.get_selected_button.grid( row = 2, column = 0, padx = 10, pady = 10, sticky = 'e' )

    def create_table( self ) :
        self.checkboxes = [ ]
        
        self.data = [
            {"idx": 1, "id": "2b7c51034242", "name": "nginx02"},
            {"idx": 2, "id": "2b7c51034242", "name": "nginx01"},
            {"idx": 3, "id": "2b7c51034242", "name": "my_web_server"},
            {"idx": 4, "id": "2b7c51034242", "name": "ubuntu02"},
            {"idx": 5, "id": "2b7c51034242", "name": "ubuntu01"}
        ]

        # Create a frame for the entire table
        table_container = ctk.CTkFrame( self ):
        table_container.grid(row=0, column=0, padx=10, pady=10, sticky="nsew", rowspan=2)
        table_container.grid_columnconfigure(0, weight=1)
        table_container.grid_rowconfigure(1, weight=1)

        # Create header labels
        header = [ 'Select', 'ID', 'Names' ]
        for i, header in enumerate( headers ) :
            label = ctk.CTkLabel(
                header_frame,
                text = heander,
                font = ctk.CTkFont( weight = 'bold' )
            )
            if i == 0 :
                label.grid(row=0, column=i, padx=(10, 5), pady=10, sticky="w")
            elif i == len(headers) - 1:
                label.grid(row=0, column=i, padx=(5, 10), pady=10, sticky="ew")
            else:
                label.grid(row=0, column=i, padx=5, pady=10, sticky="ew")
        



