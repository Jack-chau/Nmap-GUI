import docker
class DockerNetworkFun( ) :
	def __init__( self ):
		try :
			self.client = docker.from_env( )
		except :
			print( 'Fail to initialize Docker client')

	
	def list_networks( self ) :
		return( self.client.networks.list( ) )
		
	def create_network( self, name, driver = "bridge" ) :
		return self.client.networks.create( name, driver=driver )
		
	def set_static_ip( self, container_id, network_name, ip_addr ) :
		try :
			# Get the container
			container = self.client.container.get( container_id )

			# Get the network
			network = self.client.networks.get( network_name )

    		# Disconnect if network already added
			if network_name in container.attrs[ 'NetworkSettings' ][ 'Networks' ]:
				network.disconnect( container )
				
			# Assign network and set static IP
			self.client.api.connect_container_to_network(
				container.id,
				network_name,
				ipv4_address = ip_addr
			)
				
			# Verify the container was assigned static IP
			container.reload()
			assigned_ip = container.attrs[ 'NetworkSettings' ][ 'Networks' ] [ network_name ][ "IPAddress" ]
				
			if assigned_ip == ip_addr :
				print( f"Sucessfully assigned static IP {ip_addr} to container { container_id }." )
				return
			else :
				print( f"Failed to assign static IP." )
				return
		except Exception as e :
			print( f"Unexpected error: {str( e )}" )
