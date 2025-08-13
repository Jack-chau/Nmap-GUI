import docker
import subprocess

class DockerNetworkFun( ) :
	def __init__( self ):
		try :
			self.client = docker.from_env( )
		except :
			print( 'Fail to initialize Docker client')

	def list_networks( self ) :
		result = ''
		try :
			network_list = subprocess.run(
				[ 'docker', 'network', 'ls' ],
				capture_output = True,
				text = True,
				check = True,
			)
			result += network_list.stdout
			return result
		except Exception as e  :
			return e

	def create_network( self,
						name = None, 
						driver = "bridge",
						subnet = None,
						gateway = None,
						attachable = True,	
					) :
		try :
			output = ""
			if not name : 
				return f"Please Input the network name!\n"
			
			ipam_config = { "driver" : "default" }
			config = dict( )
			if subnet :
				config["subnet"] = str( subnet )
				if gateway :
					config["gateway"] = str( gateway )
			
			ipam_config["config"] = [ config ]

			network = self.client.networks.create(
							name = str( name ),
							driver = driver,
							attachable = attachable,
							ipam = ipam_config
						)
			if network :
				output += f"docker network name: {name} has been created.\n\n"
				output += self.list_networks( )
			else :
				print( "Failed to create network." )

		except docker.errors.APIError as e:
			return f"Failed to create network: {str(e)}\n"
		except Exception as e:
			return f"Unexpected error: {str(e)}\n"		

	def remove_network( self, name ) :
		try :
			network = self.client.networks.get( str( name ) )
			network.remove( )
			return f"network name '{name}' has been removed"
		except Exception as e:
			return f"Unexpected error: {str(e)}\n"	


	# def set_static_ip(self, container_id, network_name, ip_addr):
    #     """Assign static IP to container in specified network
        
    #     Args:
    #         container_id (str): Container ID or name
    #         network_name (str): Network name
    #         ip_addr (str): IPv4 address to assign
            
    #     Returns:
    #         str: Success/error message
            
    #     Raises:
    #         RuntimeError: If operation fails
    #     """
    #     try:
    #         # Get container and network objects
    #         container = self.client.containers.get(container_id)  # Fixed: containers instead of container
    #         network = self.client.networks.get(network_name)

    #         # Disconnect if already connected
    #         if network_name in container.attrs['NetworkSettings']['Networks']:
    #             network.disconnect(container)

    #         # Connect with static IP
    #         network.connect(
    #             container,
    #             ipv4_address=ip_addr
    #         )

    #         # Verify assignment
    #         container.reload()
    #         assigned_ip = container.attrs['NetworkSettings']['Networks'][network_name]['IPAddress']
            
    #         if assigned_ip == ip_addr:
    #             return f"Successfully assigned static IP {ip_addr} to container {container_id}"
    #         return "IP assignment verification failed"
            
    #     except docker.errors.NotFound as e:
    #         raise RuntimeError(f"Container or network not found: {str(e)}")
    #     except Exception as e:
    #         raise RuntimeError(f"Failed to set static IP: {str(e)}")


dnf = DockerNetworkFun()
# dnf.create_network(name="my-net2", subnet="192.168.2.0/24", gateway = '192.168.2.2')
# print( dnf.remove_network( name='my-net2') )
# dnf.set_static_ip("my-container", "my-net", "192.168.1.100")