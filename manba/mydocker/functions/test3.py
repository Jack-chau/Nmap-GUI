import customtkinter as ctk

class ContainerManager:
    def __init__( self ) :
        self.app = ctk.CTk( )
        self.app.title( "Container Management" )
        self.app.geometry( '700x300' )

        self.data = [
            ["my-nginx2", "exited"],
            ["my-nginx", "exited"]
        ]
        
        self.create_container_table( )

    def create_container_table( )
    # Main frame for the table
    table_frame = ctk.CTkFrame( self.app )
    table_frame.pack( padx=20, pady=20, fill='both', expand=True )
    
    headers = ['Name', "Status", 'Action' ]

    for col, header in enumerate( headers ): 
        header_label = ctk.CTkLabel(
            table_frame,
            text = header,
            font = ctk.CTkFont( weight="bold", size=14 ),
            height = 40,
            fg_color="#2E86AB",
            text_color="white"
        )
        # Make the Action header span3 colums worth of space
        if header == "Action" :
            header_label.header_label.grid(row=0, column=col, columnspan=3, padx=2, pady=2, sticky="nsew")
        else:
                header_label.grid(row=0, column=col, padx=2, pady=2, sticky="nsew")
    
    for row, row_data in enumerate( self.data, 1 ) :
        for col in range( 2 ) :
            label = ctk.CTkLabel(
                table_frame,
                text = row_data[col],
                height = 35,
                corner_radius = 5,
                fg_color = "#F8F9FA" if row % 2 == 0 else "#E9ECEF",
                text_color="black"
            )