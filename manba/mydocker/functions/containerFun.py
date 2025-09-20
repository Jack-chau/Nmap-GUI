import docker
import subprocess
class DockerContainerFun :
	def __init__( self ):
		try :
			self.client = docker.from_env( )
		except :
			print( 'Fail to initialize Docker client')

	def docker_ps( self ):
		result = ''
		try: 
			docker_ps = subprocess.run( 
				[ 'docker', 'ps' ],
				capture_output = True,
				text = True,
			)
			result += docker_ps.stdout
			return result
		except Exception as e :
			return( e )

	def docker_ps_all( self ):
		result = ''
		try: 
			docker_ps = subprocess.run( 
				[ 'docker', 'ps','-a' ],
				capture_output = True,
				text = True,
			)
			result += docker_ps.stdout
			return result
		except Exception as e :
			return( e )

	def new_container( self, 
					   name  = None, 
					   image = None, 
					   detach = True,
					   network = None, 
					   static_ip = None,
					   **kwargs
					) :

		image_defaults = {
            'ubuntu': '/bin/bash -c "while true; do sleep 1; done"',
            'centos': '/bin/bash -c "while true; do sleep 1; done"',
            'alpine': '/bin/sh -c "while true; do sleep 1; done"',
            'debian': '/bin/bash -c "while true; do sleep 1; done"'
        }

		base_image = image.split(':')[0].lower()

		if base_image in image_defaults:
			command = image_defaults[base_image]
		else :
			command = None

		port = kwargs.pop('ports', dict( ) )

		if port :
			host_port, container_port = port.split( ':' )
			port = { f"{container_port}/tcp" : int( host_port ) }

		try :
			container = self.client.containers.run( 
				name = name,
				image = image,
				detach = detach,
				command = command,
				ports = port,
			)

			if static_ip and network :
				docker_network = self.client.networks.get( network )
				docker_network.connect( container, ipv4_address = static_ip )

			container.reload( )

			result = ''

			if detach :
				result += ( f"container {container.id} is running with detach mode\n" )
			else :
				result += ( f"container {container.id} is running without detach mode\n" )

			result += self.docker_ps( )

			return result

		except Exception as e :
			return( e )

	def start_container( self, container ) :
		result = ''
		try :
			container = self.client.containers.get( str( container ) )
			container.start( )
			result += f"container: { container }\nhas been started\n\n"

			result += self.docker_ps( )
			return result

		except Exception as e :
			return( e )

	def stop_container( self, container_id ) :
		result = ''
		try :
			container = self.client.containers.get( container_id )
			container.stop()
			result += f"container: {container_id}\nhas been stoped\n\n"

			result += self.docker_ps( )
			return( result )
			
		except Exception as e :
			return( e )
	
	def remove_container( self, container_id , force = False ) :
		result = ''
		try :
			container = self.client.containers.get( container_id )
			container.remove( force = force )
			result += f"container: {container_id}\nhas been removed\n\n"

			result += self.docker_ps_all( )
			return result
		except Exception as e :
			return( e )
