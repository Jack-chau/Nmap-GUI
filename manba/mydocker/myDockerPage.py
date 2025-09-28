import customtkinter as ctk
# import main frame and tabs
from mydocker.frames.dockerMainFrame import DockerMainFrame
# import functions
# from mydocker.functions.infoFun import DockerInfoFuns
from mydocker.functions.imageFun import DockerImageFuns
from mydocker.functions.containerFun import DockerContainerFun
from mydocker.functions.networkFun import DockerNetworkFun
from mydocker.functions.trobleShootFun import DockerTBFun

class MyDockerPage( ctk.CTkFrame ) :
    def __init__( self, master ) :
        super( ).__init__( master )
# Inheritant GUI
        self.main_frame = DockerMainFrame( master )
# Ingeritant Functions
        self.image_funs = DockerImageFuns( )
        self.container_funs = DockerContainerFun( )
        self.network_funs = DockerNetworkFun( )
        self.ts_funs = DockerTBFun( )
# Combine Docker GUI and Functions
        self.main_frame.docker_frame( )
        self.check_connection( )

# Image Tab
        self.main_frame.image_tab.image_execute.configure( command = self.docker_image )

# Container Tab
        self.main_frame.container_tab.create_container_btn.configure( command = self.create_docker_container )

# Troble Shooting Tab
        self.main_frame.trobleshoot_tab.check_it_out.configure( command = self.docker_info )
        self.main_frame.trobleshoot_tab.clear_btn.configure( command = self.clear_textbox )


    def clear_textbox( self ) :
        self.main_frame.docker_textbox.delete( '0.0', 'end' )

    def check_connection( self ) :
        self.clear_textbox( )
        self.main_frame.docker_textbox.insert( 'end', self.ts_funs.check_connection( ) )

    def update_textbox( self, text ) :
        self.main_frame.docker_textbox.insert( 'end', text )
        self.main_frame.docker_textbox.see( 'end' )

# For Docker Image Tab
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

# Docker Container Tab
    def create_docker_container( self ) :
        self.clear_textbox( )

        container_name = self.main_frame.container_tab.name_entry.get( )
        container_name = str( container_name ) if container_name else "Not_Named"
        container_image = str ( self.main_frame.container_tab.image_entry.get( ).lower() )
        container_network = self.main_frame.container_tab.network_entry.get( )
        container_network = str( container_network ) if container_network else None
        container_ip = self.main_frame.container_tab.staticIP_entry.get( )
        container_ip = str( container_ip ) if container_ip else None
        published_port = self.main_frame.container_tab.pub_port_entry.get( )
        published_port = str( published_port ) if published_port else None

        if not container_name : 
            self.update_textbox( f"Please name the container you want to create!!!\n")
        if not container_image :
            self.update_textbox( f"Please enter the image you want to create!!!\n")
        try :
            result = self.container_funs.new_container( 
                name = container_name,
                image = container_image,
                detach = True,  
                network = container_network,
                static_ip = container_ip,
                ports = published_port,
            )
            if result :
                self.update_textbox( result )
            else :
                self.update_textbox( "Fail to create container" )

        except Exception as e :
            print( f"❌Fail to create container" )
            print( e )

# For Trobleshoot Tab

    def docker_info( self ) :
        self.clear_textbox( )
        if self.main_frame.trobleshoot_tab.check_connection.get() == 'on':
            self.main_frame.docker_textbox.insert( 'end', self.ts_funs.check_connection( ) )

        if self.main_frame.trobleshoot_tab.docker_cli_version.get() == 'on':
            self.main_frame.docker_textbox.insert( 'end', self.ts_funs.check_docker_client_version( ) )

        if self.main_frame.trobleshoot_tab.docker_server_version.get() == 'on':
            self.main_frame.docker_textbox.insert( 'end', self.ts_funs.check_docker_server_version( ) )
        
        if self.main_frame.trobleshoot_tab.docker_context.get() == 'on':    
            self.main_frame.docker_textbox.insert( 'end', self.ts_funs.show_docker_contexts( ) )        
        
        if self.main_frame.trobleshoot_tab.docker_info.get() == 'on':    
            self.main_frame.docker_textbox.insert( 'end', self.ts_funs.show_docker_info( ) )        
        
        if self.main_frame.trobleshoot_tab.docker_networks.get() == 'on':    
            self.main_frame.docker_textbox.insert( 'end', self.ts_funs.show_network_contexts( ) ) 

        if self.main_frame.trobleshoot_tab.running_containers.get() == 'on':    
            self.main_frame.docker_textbox.insert( 'end', self.ts_funs.show_runing_containers( ) )        
        
        if self.main_frame.trobleshoot_tab.container_inspect.get() == 'on':    
            self.main_frame.docker_textbox.insert( 'end', self.ts_funs.inspect_container( self.main_frame.trobleshoot_tab.container_inspect_entry.get() ) )        
        
        if self.main_frame.trobleshoot_tab.network_inspect.get() == 'on':    
            self.main_frame.docker_textbox.insert( 'end', self.ts_funs.inspect_network( self.main_frame.trobleshoot_tab.network_inspect_entry.get() ) ) 


        
            
        


