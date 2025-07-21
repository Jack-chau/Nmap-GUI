import docker
import subprocess

class DockerInfo :
	def __init__( self ):
		try :
			self.client = docker.from_env( )
		except :
			print( 'Fail to initialize Docker client')
# Ping
	def check_connection( self ) :
		try :
			self.client.ping( )
			welcome = rf"""
				 🫧
			   🫧🫧🫧          
			 🫧🫧🫧🫧🫧🫧     
			🫧🫧🫧🫧🫧🫧🫧🫧
			################"\___/ ===
			{{    /  ====	\___/ 
			 \____ o         __/
			  \    \       __/
			   \    \    ___/
				\____\____/
					
			DOCKER: 🐳Yea!!!🐳
	🔥🔥🔥Docker are successfully connected!🔥🔥🔥
			"""
			print(welcome)
		except Exception as e :
			print( f"❌Failed to connect to Docker: {str( e ) }❌" )
		
# Check docker client version
	def check_docker_client_version( self ) :
		client_ver = docker.__version__
		print( client_ver )

# Check docker server version
	def check_docker_server_version( self ) :
		server_ver = self.client.version( )
		print( server_ver[ "Version" ] )

# Check docker context
	def show_docker_contexts( self ) :
		try :
			result = subprocess.run( [ 'docker', 'context', 'ls' ], capture_output = True, text = True, check = True )
			print( result.stdout )
		except subprocess.CalledProcessError as e :
			print( f"Error executing command: {e}" )
			print( f"Error output: {e.stderr}" )

# Check docker info in detail
	def show_docker_info( self ) :
		try :
			result = subprocess.run( [ 'docker', 'info' ], capture_output = True, text = True, check = True )
			print( result.stdout )
		except subprocess.CalledProcessError as e :
			print( f"Error executing command: {e}" )
			print( f"Error output: {e.stderr}" )

# Show all containers
	def show_all_containers( self ) :
		containers = self.client.containers.list( all = all )
		containers_list = list( )
		for container in containers :
			containers_list.append(
				{
					'id' : container.short_id,
					'name' : container.name,
					'status' : container.status,
					'newtwork_name' : list( container.attrs['NetworkSettings']['Networks'].keys())[0],
					'ip_addr' : container.attrs['NetworkSettings']['IPAddress'],
					'port' : container.attrs['NetworkSettings']['Ports']
				}
			)
		if len( containers_list ) > 0 :
			self.show_container_info( containers_list )
		else :
			print( "No running container" )

# Show running containers
	def show_runing_containers( self ) :
		running_containers = self.client.containers.list( all = False )
		running_containers_list = list( )
		for container in running_containers :
			network_settings = container.attrs['NetworkSettings']['Networks']
			# Get network if exists
			if network_settings :
				network_info = dict()
				for network_name, network_setting in network_settings.items( ) :
					network = self.client.networks.get( network_setting[ 'NetworkID' ] )
					network_info[network_name] = {
						'driver' : network.attrs['Driver'],
						'network_id' : network.id,
						'ip_address' : network_setting['IPAddress'],
					}

			running_containers_list.append(
				{
					'id' : container.short_id,
					'name' : container.name,
					'status' : container.status,
					'newtwork_name' : list( network_info.keys())[0],
					'network_type' : network_info[network_name]['driver'],
					'ip_addr' : network_info[network_name]['ip_address'] ,
					'ports' : ', '.join( container.attrs['NetworkSettings']['Ports'].keys() )
				}
			)
		if len( running_containers_list ) > 0 :
				self.show_container_info( running_containers_list )
			# print( running_containers_list )
		else :
			print( "No running containers" )


	def show_container_info( self, data_list ) :
		id = True
		name = True
		status = True
		network_type = True
		newtwork_name = True
		ip_addr = True
		port = True
		num_of_container = 1
		for i in data_list:
			print( f"The NO:{num_of_container} container status:")
			if i['id'] and id == True :
				keys = f"{'id'}\t"
				values = f"{i['id']}\t"

			if i['name'] and name == True :
				keys += f"\t{'name'}\t\t"
				values += f"{i['name']}\t\t"

			if i['status'] and status == True :
				keys += f"{'status'}\t\t" 
				values += f"{i['status']}\t\t"
				
			if i['network_type'] and newtwork_name == True :
				keys += f"{'network_type'}\t" 
				values += f"{i['network_type']}\t\t"  

			if i['newtwork_name'] and newtwork_name == True :
				keys += f"{'newtwork_name'}\t\t" 
				values += f"{i['newtwork_name']}\t" 

			if i['ip_addr'] and ip_addr == True :
				keys += f"{'ip_addr'}\t\t" 
				values += f"{i['ip_addr']}\t" 

			if i['ports'] and port == True :
				keys += f"{'port'}\t\t" 
				values += f"{i['ports']}\t" 
			num_of_container += 1
			print( keys )
			print( values )
			print( '\n' )

# Container Inspect
	def inspect_container( self, target_container ) :
		try :
			target_container = self.client.containers.get( target_container )
			container_attrs = target_container.attrs

			print( f"Container Name: { target_container.name }" )
			print( f"Container ID: { target_container.id }" )

			print( f"Status: { target_container.status }" )
			print( f"Image: { target_container.image.tags }" )
			print( f"Time Created: { target_container.attrs[ "Created" ] }" )

			print( "\nNetwork Settings:" )
			networks = target_container.attrs[ 'NetworkSettings' ][ 'Networks' ]
			port = target_container.attrs[ 'NetworkSettings' ][ 'Ports' ]
			if not port : 
				port = "NA"
				for net_name, net_config in networks.items( ) :
					print( f"\tNetwork: { net_name }" )
					print( f"\tIP Address: {net_config["IPAddress"]}")
				return
			for net_name, net_config in networks.items( ) :
				print( f"\tNetwork: { net_name }" )
				print( f"\tIP Address: {net_config["IPAddress"]}")
				print( f"\tPorts: { ', '.join( port.keys()) }")
		except docker.errors.NotFound:
			print(f"Container {target_container} not found")
		except docker.errors.APIError as e:
			print(f"Docker API error: {e}")

	def inspect_network( self, target_network ) :
		try :
			network = self.client.networks.get( target_network )
			output = {
				"Name" : network.name,
				"ID" : network.id,
				"Driver" : network.attrs[ 'Driver' ],
				"Subment" : network.attrs['IPAM']['Config'][0]['Subnet'],
				"Gateway" : network.attrs['IPAM']['Config'][0]['Gateway'],
				"Created" : network.attrs['Created'],
			}
			
			for key, value in output.items( ):
				print( f"{key:10}: {value}" )

		except docker.errors.NotFound :
			return f"Network {target_network} not found."
		except Exception as e :
			return f"Error: {str(e)}"

a = DockerInfo()
print( a.show_runing_containers() )

	# a.run_container( image="nginx:alpine", name="my_web_server", ports={'80/tcp':8080}, network="my-docker-network" )
	# print( a.list_all_containers() )
	# a.run_container( image = 'alpine', command = [ 'echo', 'hello', 'world'], name = 'alpine3', detach=True )
	# print( a.list_runing_containers( ) )