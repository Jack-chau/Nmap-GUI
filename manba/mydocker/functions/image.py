class DockerImage :
	def __init__( self ):
		try :
			self.client = docker.from_env( )
		except :
			print( 'Fail to initialize Docker client')
    
    		
    def list_image( self ) :
		return self.client.imgaes.list( )
		
	def pull_image( self, repository, tag = "latest" ) :
		return self.client.imgaes.pull( f"{repository} : {tag}" )

	def remove_image( self, image_id, force = False ) : #If force=true, it force the removeal of image even it is currently in use.
		to_remove = input( f"Do you want to remove the image {image_id} ?")
		if to_remove :
			self.client.imgaes.remove( image_id, force = force )
			return f"The image {image_id} has been removed."
		else :
			return f"The action has been cancled."