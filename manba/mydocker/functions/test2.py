import customtkinter as ctk

class ContainerManager:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.title("Container Management")
        self.app.geometry("700x300")
        
        self.data = [
            ["my-nginx2", "exited"],
            ["my-nginx", "exited"]
        ]
        
        self.create_container_table()
        
    def create_container_table(self):
        # Main frame for the table
        table_frame = ctk.CTkFrame(self.app)
        table_frame.pack(padx=20, pady=20, fill="both", expand=True)
        
        # Create headers
        headers = ["Name", "Status", "Action"]  # Merged header
        
        for col, header in enumerate(headers):
            header_label = ctk.CTkLabel(
                table_frame, 
                text=header,
                font=ctk.CTkFont(weight="bold", size=14),
                height=40,
                corner_radius=5,
                fg_color="#2E86AB",
                text_color="white"
            )
            
            # Make the Action header span 3 columns worth of space
            if header == "Action":
                header_label.grid(row=0, column=col, columnspan=3, padx=2, pady=2, sticky="nsew")
            else:
                header_label.grid(row=0, column=col, padx=2, pady=2, sticky="nsew")
        
        # Create data rows with action buttons
        for row, row_data in enumerate(self.data, 1):
            # Name and Status labels
            for col in range(2):
                label = ctk.CTkLabel(
                    table_frame,
                    text=row_data[col],
                    height=35,
                    corner_radius=5,
                    fg_color="#F8F9FA" if row % 2 == 0 else "#E9ECEF",
                    text_color="black"
                )
                label.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
            
            # Action buttons frame (replaces the merged Action header area)
            action_frame = ctk.CTkFrame(table_frame, fg_color="transparent")
            action_frame.grid(row=row, column=2, columnspan=3, padx=2, pady=2, sticky="nsew")
            
            # Add action buttons
            ctk.CTkButton(
                action_frame,
                text="Start",
                width=80,
                height=30,
                fg_color="#4CAF50",
                hover_color="#45a049",
                command=lambda name=row_data[0]: self.start_container(name)
            ).pack(side="left", padx=5)
            
            ctk.CTkButton(
                action_frame,
                text="Stop",
                width=80,
                height=30,
                fg_color="#F44336",
                hover_color="#d32f2f",
                command=lambda name=row_data[0]: self.stop_container(name)
            ).pack(side="left", padx=5)
            
            ctk.CTkButton(
                action_frame,
                text="Remove",
                width=80,
                height=30,
                fg_color="#FF9800",
                hover_color="#f57c00",
                command=lambda name=row_data[0]: self.remove_container(name)
            ).pack(side="left", padx=5)
        
        # Configure grid weights
        table_frame.grid_columnconfigure(0, weight=2)  # Name column
        table_frame.grid_columnconfigure(1, weight=1)  # Status column
        table_frame.grid_columnconfigure(2, weight=3)  # Action column (spans multiple visual columns)
        
        for row in range(len(self.data) + 1):
            table_frame.grid_rowconfigure(row, weight=1)
    
    def start_container(self, name):
        print(f"Starting container: {name}")
        # Add your start container logic here
    
    def stop_container(self, name):
        print(f"Stopping container: {name}")
        # Add your stop container logic here
    
    def remove_container(self, name):
        print(f"Removing container: {name}")
        # Add your remove container logic here
    
    def run(self):
        self.app.mainloop()

# Create and run the application
app = ContainerManager()
app.run()