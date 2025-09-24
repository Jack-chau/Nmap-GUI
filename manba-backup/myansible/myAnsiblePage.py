import customtkinter as ctk
from myansible.frames.ansibleMainFrame import AnsibleMainFrame

class MyAnsiblePage( ctk.CTkFrame ) :
    def __init__( self, master ) :
        super( ).__init__( master )
# Inheritant GUI
        self.main_frame = AnsibleMainFrame( master )
        self.main_frame.ansible_frame( )

    
