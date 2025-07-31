import customtkinter as ctk
from mydocker.dockerMainFrame import DockerMainFrame
from mydocker.tabs.infoTab import DockerInfoTab
from mydocker.functions.infoFun import DockerInfoFuns
from mydocker.functions.imageFun import DockerImageFuns

class MyDockerPage( ctk.CTkFrame ) :
    def __init__( self, master ) :
        super( ).__init__( master )
# Inheritant GUI
        self.main_frame = DockerMainFrame( master )
# Ingeritant Functions
        self.info_funs = DockerInfoFuns( )
        self.image_funs = DockerImageFuns( )

# Combine Docker GUI and Functions
        self.main_frame.docker_out_frame( )
        self.check_connection( )
        self.main_frame.info_tab.check_it_out.configure( command = self.check_it_out )
        self.main_frame.info_tab.clear_btn.configure( command = self.clear_textbox )
        self.main_frame.image_tab.image_execute.configure( command = self.docker_image )

    def clear_textbox( self ) :
        self.main_frame.docker_textbox.delete( '0.0', 'end' )

# For Docker Info Tab
    def check_connection( self ) :
        self.clear_textbox( )
        self.main_frame.docker_textbox.insert( 'end', self.info_funs.check_connection( ) )

    def update_textbox( self, text ) :
        self.main_frame.docker_textbox.insert( 'end', text )
        self.main_frame.docker_textbox.see( 'end' )

    def check_it_out( self ) :
        self.clear_textbox( )
        if self.main_frame.info_tab.docker_cli_version.get() == 'on':
            self.main_frame.docker_textbox.insert( 'end', self.info_funs.check_docker_client_version( ) )
        
        if self.main_frame.info_tab.docker_server_version.get() == 'on':
            self.main_frame.docker_textbox.insert( 'end', self.info_funs.check_docker_server_version( ) )
        
        if self.main_frame.info_tab.docker_context.get() == 'on':    
            self.main_frame.docker_textbox.insert( 'end', self.info_funs.show_docker_contexts( ) )        
        
        if self.main_frame.info_tab.docker_info.get() == 'on':    
            self.main_frame.docker_textbox.insert( 'end', self.info_funs.show_docker_info( ) )        
        
        if self.main_frame.info_tab.docker_networks.get() == 'on':    
            self.main_frame.docker_textbox.insert( 'end', self.info_funs.show_network_contexts( ) ) 

        if self.main_frame.info_tab.running_containers.get() == 'on':    
            self.main_frame.docker_textbox.insert( 'end', self.info_funs.show_runing_containers( ) )        
        
        if self.main_frame.info_tab.container_inspect.get() == 'on':    
            self.main_frame.docker_textbox.insert( 'end', self.info_funs.inspect_container( self.main_frame.info_tab.container_inspect_entry.get() ) )        
        
        if self.main_frame.info_tab.network_inspect.get() == 'on':    
            self.main_frame.docker_textbox.insert( 'end', self.info_funs.inspect_network( self.main_frame.info_tab.network_inspect_entry.get() ) )        

# For Docker Image Tag
    def docker_image( self ) :

        self.clear_textbox( )

        image_name = self.main_frame.image_tab.image_name_entry.get( )
        image_version = self.main_frame.image_tab.image_version_entry.get( )
        command = self.main_frame.image_tab.image_command_entry.get( )
        rmi_image = self.main_frame.image_tab.image_removal_entry.get( )

        if command :
            self.main_frame.image_tab.image_name_entry.configure( state="disabled" )
            self.main_frame.image_tab.image_version_entry.configure( state="disabled" )
            self.update_textbox( f"Executing: {command}....\n" )
            self.image_funs.pull_image_command(
                command,
                callback = self.update_textbox
            )
        elif image_name:
            version = image_version if image_version else 'latest'
            try:
                self.main_frame.image_tab.image_command_entry.configure( state="disabled" )
                self.update_textbox( f"Pulled image: {image_name}:{version}\n" )
                self.image_funs.pull_image( image_name, version, callback = self.update_textbox )
            except Exception as e:
                self.update_textbox(f"Error: {str(e)}\n")

        elif rmi_image:
            self.image_funs.remove_image( rmi_image, callback = self.update_textbox)
        else:
            self.update_textbox("Error: No image specified\n")




