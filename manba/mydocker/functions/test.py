import customtkinter as ctk
from CTkTable import *

class TableWithButtons:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.geometry("800x500")
        self.app.title("Table with Buttons")
        
        self.create_table_with_buttons()
        
    def button_callback(self, row, col, value):
        print(f"Button clicked at row {row}, column {col}, value: {value}")
        # Add your button action here
        
    def create_table_with_buttons(self):
        # Sample data
        data = [
            ["Product", "Price", "Action"],
            ["Laptop", "$999", "Buy"],
            ["Mouse", "$25", "Buy"],
            ["Keyboard", "$75", "Buy"]
        ]
        
        # Create frame for table
        table_frame = ctk.CTkFrame(self.app)
        table_frame.pack(padx=20, pady=20, fill="both", expand=True)
        
        # Create headers
        for col in range(3):
            header = ctk.CTkLabel(
                table_frame, 
                text=data[0][col],
                font=ctk.CTkFont(weight="bold"),
                width=120,
                height=40
            )
            header.grid(row=0, column=col, padx=1, pady=1, sticky="nsew")
        
        # Create data rows with buttons
        for row in range(1, len(data)):
            for col in range(3):
                if col == 2:  # Button column
                    btn = ctk.CTkButton(
                        table_frame,
                        text=data[row][col],
                        width=120,
                        height=35,
                        command=lambda r=row, c=col, v=data[row][0]: self.button_callback(r, c, v)
                    )
                    btn.grid(row=row, column=col, padx=1, pady=1, sticky="nsew")
                else:
                    label = ctk.CTkLabel(
                        table_frame,
                        text=data[row][col],
                        width=120,
                        height=35
                    )
                    label.grid(row=row, column=col, padx=1, pady=1, sticky="nsew")
        
        # Configure grid weights
        for i in range(3):
            table_frame.grid_columnconfigure(i, weight=1)
        for i in range(len(data)):
            table_frame.grid_rowconfigure(i, weight=1)

    def run(self):
        self.app.mainloop()

# Run the app
app = TableWithButtons()
app.run()