import docker
import subprocess

class DockerImageFuns :
	def __init__( self, root=None ):
		self.root = root
		try :
			self.client = docker.from_env( )
		except :
			return( 'Fail to initialize Docker client')
    		
	def list_image( self ):
		self.client.images.list( )
		
	def pull_image( self, repository, tag = "latest", callback = None) :
		# return self.client.images.pull( f"{repository} : {tag}" )
		try :
			install_image = f"{str( repository)}:{str(tag)}"
			output = ''
			pull_result = subprocess.run( 
							['docker', 'pull', install_image ],
							capture_output = True,
							text = True
						)
			output += f"docker pull {install_image} executed.\n\nDocker Image Pull Successfully!!!\n{'-' * 150}\n"
			image_result = subprocess.run( 
								['docker', 'images'],
								capture_output = True,
								text = True,
							)
			output += image_result.stdout
			print( output )

			if callback :
				callback( output )
				
		except Exception as e :
			if callback :
				callback( 'fail to pull image' )
		

	def remove_image( self, rmi_image, callback = None ) : #If force=true, it force the removeal of image even it is currently in use.
		try :
			output = ''
			pull_result = subprocess.run( 
							['docker', 'rmi', rmi_image ],
							capture_output = True,
							text = True
						)
			output += f"docker image {rmi_image} has been removed.\n{'-' * 150}\n"
			image_result = subprocess.run( 
								['docker', 'images'],
								capture_output = True,
								text = True,
							)
			output += image_result.stdout
			print( output )

			if callback :
				callback( output )
				
		except Exception as e :
			if callback :
				callback( 'fail to pull image' )

	def pull_image_command( self, command, callback = None ) :

		try :
			output = ''
			pull_result = subprocess.run( 
							command.split(),
							capture_output = True,
							text = True
						)
			output += f"{command} executed.\n\nDocker Image Pull Successfully!!!\n{'-' * 150}\n"
			image_result = subprocess.run( 
								['docker', 'images'],
								capture_output = True,
								text = True,
							)
			output += image_result.stdout
			print( output )
			if callback :
				callback( output )
				
		except Exception as e :
			if callback :
				callback( 'fail to pull image' )
		
