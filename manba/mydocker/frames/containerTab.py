import customtkinter as ctk
from CTkTable import *
import webbrowser
import docker

class DockerContainerTab :
    def __init__( self, docker_tab ) :
        self.container_tab = docker_tab.add( 'Container' )
        self.client = docker.from_env( )
        self.show_all_containers( )
        self._setup_ui( )

    # Show all containers
    def show_all_containers( self ) :
        all_containers = self.client.containers.list( all = all )
        all_containers_list = list( )
        for container in all_containers :
            network_settings = container.attrs['NetworkSettings']['Networks']
            # Get network if exists
            if network_settings :
                network_info = dict( )
                # for key and values in network_settings.items( )
                for network_name, network_setting in network_settings.items( ) :
                    network = self.client.networks.get( network_setting[ 'NetworkID' ] )
                    network_info[network_name] = {
                        'driver' : network.attrs['Driver'],
                        'network_id' : network.id,
                        'ip_address' : network_setting['IPAddress'],
                        }
            all_containers_list.append(
                {
					'id' : container.short_id,
					'name' : container.name,
					'status' : container.status,
					'newtwork_name' : list( network_info.keys() )[0],
					'network_type' : network_info[network_name]['driver'],
					'ip_addr' : network_info[network_name]['ip_address'] ,
					'ports' : ', '.join( container.attrs['NetworkSettings']['Ports'].keys() )
				}
			)
        if len( all_containers_list ) > 0 :
            return( all_containers_list )
        else :
            return( "No running containers" )

    def _setup_ui( self ) :

        self.container_label = ctk.CTkLabel(
            self.container_tab,
            text = "Docker Container Management",
            font = ctk.CTkFont(
                family="Courier New",
                size=16,
                weight="bold",
                slant="italic",
                underline=True,
                overstrike=False
            )
        )

        self.container_label.pack(
            pady = 5 ,
            padx = 5 ,
        )

        self.left_frame = ctk.CTkFrame(
            self.container_tab,
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
            self.container_tab,
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
        self.left_frame.grid_rowconfigure( 8, weight = 1 )
        self.left_frame.grid_rowconfigure( 9, weight = 1 )

        self.container_label = ctk.CTkLabel(
            self.left_frame,
            text = "Create Container",
            font = ctk.CTkFont(
                family="Courier New",
                size=18,
                weight="bold",
                overstrike=False
            )
        )
        self.container_label.grid(
            column = 0,
            row = 0,
            columnspan = 2,
            pady = ( 10, 0 ),
            padx = ( 10, 10 ),
            sticky = 'ew',
        )

### Create Docker Container
        self.name_label = ctk.CTkLabel(
            self.left_frame,
            text = "Container Name: ",
            font = ctk.CTkFont(
                family="Arial",
                size=16,
                weight="bold",
                overstrike=False
            )
        )

        self.name_label.grid(
            column = 0,
            row = 1,
            sticky = 'w' ,
            pady = ( 5 , 0 ),
            padx = ( 40, 0 ),
        )

        self.name_entry = ctk.CTkEntry(
            self.left_frame ,
            placeholder_text = "Container Name",
            font = ctk.CTkFont(
                size=15,
            )
        )

        self.name_entry.grid(
            row = 1,
            column = 1,
            sticky = 'we' ,
            pady = ( 5 , 0 ),
            padx = ( 0, 20 ),
        )

        self.image_label = ctk.CTkLabel(
            self.left_frame,
            text = "Image: ",
            font = ctk.CTkFont(
                family="Arial",
                size=16,
                weight="bold",
                overstrike=False
            )
        )

        self.image_label.grid(
            column = 0,
            row = 2,
            sticky = 'w' ,
            pady = ( 5 , 0 ),
            padx = ( 40, 0 ),
        )

        self.image_entry = ctk.CTkEntry(
            self.left_frame ,
            placeholder_text = "Image:version",
            font = ctk.CTkFont(
                size=15,
            )
        )

        self.image_entry.grid(
            row = 2,
            column = 1,
            sticky = 'we' ,
            pady = ( 5 , 0 ),
            padx = ( 0, 20 ),
        )

        self.network_label = ctk.CTkLabel(
            self.left_frame,
            text = "Network Name: ",
            font = ctk.CTkFont(
                family="Arial",
                size=16,
                weight="bold",
                overstrike=False
            )
        )

        self.network_label.grid(
            column = 0,
            row = 3,
            sticky = 'w' ,
            pady = ( 5 , 0 ),
            padx = ( 40, 0 ),
        )

        self.network_entry = ctk.CTkEntry(
            self.left_frame ,
            placeholder_text = "Network Name",
            font = ctk.CTkFont(
                size=15,
            )
        )

        self.network_entry.grid(
            row = 3,
            column = 1,
            sticky = 'we' ,
            pady = ( 5 , 0 ),
            padx = ( 0, 20 ),
        )

        self.staticIP_label = ctk.CTkLabel(
            self.left_frame,
            text = "Static IP: ",
            font = ctk.CTkFont(
                family="Arial",
                size=16,
                weight="bold",
                overstrike=False
            )
        )

        self.staticIP_label.grid(
            column = 0,
            row = 4,
            sticky = 'w' ,
            pady = ( 5 , 0 ),
            padx = ( 40, 0 ),
        )

        self.staticIP_entry = ctk.CTkEntry(
            self.left_frame ,
            placeholder_text = "172.18.0.10",
            font = ctk.CTkFont(
                size=15,
            )
        )

        self.staticIP_entry.grid(
            row = 4,
            column = 1,
            sticky = 'we' ,
            pady = ( 5 , 0 ),
            padx = ( 0, 20 ),
        )

        self.pub_port_label = ctk.CTkLabel(
            self.left_frame,
            text = "Published Port: ",
            font = ctk.CTkFont(
                family="Arial",
                size=16,
                weight="bold",
                overstrike=False
            )
        )
        self.pub_port_label.grid(
            column = 0,
            row = 5,
            sticky = 'w' ,
            pady = ( 5 , 0 ),
            padx = ( 40, 0 ),
        )

        self.pub_port_entry = ctk.CTkEntry(
            self.left_frame ,
            placeholder_text = "hostport:container_port",
            font = ctk.CTkFont(
                size=15,
            )
        )

        self.pub_port_entry.grid(
            row = 5,
            column = 1,
            sticky = 'we' ,
            pady = ( 5 , 0 ),
            padx = ( 0, 20 ),
        )

        self.create_container_btn = ctk.CTkButton( 
            self.left_frame, 
            text="Create Container",
            width = 140,
            height = 40,
            font = ctk.CTkFont( "Segoe Script", 15 ),
        )
        self.create_container_btn.grid( 
            row = 6,
            column = 0,
            columnspan = 2,
            sticky = 'e' ,
            pady = ( 10 , 0 ),
            padx = ( 10, 20 ),
        )
# Stop or Remove Container

        self.container_label = ctk.CTkLabel(
            self.left_frame,
            text = "Stop or Remove Container",
            font = ctk.CTkFont(
                family="Courier New",
                size=18,
                weight="bold",
                overstrike=False
            )
        )
        self.container_label.grid(
            column = 0,
            row = 7,
            columnspan = 2,
            pady = ( 10, 0 ),
            padx = ( 10, 10 ),
            sticky = 'ew',
        )
        self.container_start_label = ctk.CTkLabel(
            self.left_frame,
            text = "Start Container: ",
            font = ctk.CTkFont(
                family="Arial",
                size=16,
                weight="bold",
                overstrike=False
            )
        )

        self.container_start_label.grid(
            row = 8,
            column = 0,
            sticky = 'w' ,
            pady = ( 25 , 0 ),
            padx = ( 40, 0 ),
        )

        self.container_start_entry = ctk.CTkEntry(
            self.left_frame ,
            placeholder_text = "container idx",
            font = ctk.CTkFont(
                size=15,
            )
        )

        self.container_start_entry.grid(
            row = 8,
            column = 1,
            sticky = 'we' ,
            pady = ( 25 , 0 ),
            padx = ( 0, 20 ),
        )

        self.container_stop_label = ctk.CTkLabel(
            self.left_frame,
            text = "Stop Container: ",
            font = ctk.CTkFont(
                family="Arial",
                size=16,
                weight="bold",
                overstrike=False
            )
        )

        self.container_stop_label.grid(
            row = 9,
            column = 0,
            sticky = 'w' ,
            pady = ( 25 , 0 ),
            padx = ( 40, 0 ),
        )

        self.container_stop_entry = ctk.CTkEntry(
            self.left_frame ,
            placeholder_text = "container idx",
            font = ctk.CTkFont(
                size=15,
            )
        )

        self.container_stop_entry.grid(
            row = 9,
            column = 1,
            sticky = 'we' ,
            pady = ( 25 , 0 ),
            padx = ( 0, 20 ),
        )

        self.container_removal_label = ctk.CTkLabel(
            self.left_frame,
            text = "Remove container:",
            font = ctk.CTkFont(
                family="Arial",
                size=16,
                weight="bold",
                overstrike=False
            )
        )

        self.container_removal_label.grid(
            row = 10,
            column = 0,
            sticky = 'w' ,
            pady = ( 25 , 0 ),
            padx = ( 40, 0 ),
        )

        self.container_removal_entry = ctk.CTkEntry(
            self.left_frame ,
            placeholder_text = "container idx",
            font = ctk.CTkFont(
                size=15,
            )
        )

        self.container_removal_entry.grid(
            row = 10,
            column = 1,
            sticky = 'we' ,
            pady = ( 25 , 0 ),
            padx = ( 0, 20 ),
        )
    
        self.container_execute = ctk.CTkButton( 
            self.left_frame, 
            text="Execute",
            width = 140,
            height = 40,
            font = ctk.CTkFont( "Segoe Script", 15 ),
        )
        self.container_execute.grid( 
            row = 11,
            column = 0,
            columnspan = 2,
            sticky = 'e' ,
            pady = ( 10 , 20 ),
            padx = ( 10, 20 ),
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
            pady = ( 10, 0 ),
            padx = ( 60, 10 ),
            sticky = 'ew',
        )

        # For demo Only
        running_container = self.show_all_containers( )
        self.container_list = list( )
        self.container_list.append( [ 'Name','Status','Action'])
        for i in running_container :
            self.container_list.append( [ i['name'], i['status'] ] )
        print( self.container_list )

        

        self.id_table = CTkTable( 
                master = self.right_frame,
                values = self.container_list,
                width = 50,
        )

        self.id_table.grid(
            row = 1,
            column = 0,
            columnspan = 2,
            padx= ( 30, 0 ),
            pady = ( 10, 0 ),
            sticky = "ew"
        )

        # for 





























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
