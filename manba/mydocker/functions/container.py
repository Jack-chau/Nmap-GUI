
class DockerContainer :
	def __init__( self ):
		try :
			self.client = docker.from_env( )
		except :
			print( 'Fail to initialize Docker client')

	def run_container( self, image, command = None, detach = True, ports = None, name = None, network = None, static_ip = None ) :
		try :
			container = self.client.containers.run( 
				image = image,
				command = command,
				detach = detach,
				ports = ports,
				name = name,
				network = network,
				static_ip = static_ip
			)
			if detach :
				print( f"container {container.id} is running with detach mode" )
			else :
				print( f"container {container.id} is running without detach mode" )
			if network:
				net = self.client.networks.get( network )
				net.connect(
					container = container.id,
					ipv4_address = static_ip
				)
		
		except Exception as e :
			print( f"❌Fail to run container")
		
	def stop_container( self, container_id ) :
		try :
			container = self.client.container.get( container_id )
			container.stop()
			print( f"{container.id} is stoped." )
		except Exception as e :
			print( e )
	
	def remove_container( self, container_id , force = False ) :
		try :
			container = self.client.container.get( container_id )
			container.remove( force = force )
		except Exception as e :
			print( e )