import docker
from pprint import pprint

# Create Docker client
client = docker.from_env()

def inspect_container(container_name_or_id):
    try:
        # Get the container
        container = client.containers.get(container_name_or_id)
        
        # Get all container attributes
        container_attrs = container.attrs
        
        # Print formatted output
        print(f"\nInspecting container: {container.name} ({container.id})")
        print("=" * 50)
        
        # Basic info
        print(f"Status: {container.status}")
        print(f"Image: {container.image.tags}")
        print(f"Created: {container.attrs['Created']}")
        
        # Network info
        print("\nNetwork Settings:")
        networks = container.attrs['NetworkSettings']['Networks']
        for net_name, net_config in networks.items():
            print(f"  Network: {net_name}")
            print(f"    IP Address: {net_config['IPAddress']}")
            print(f"    MAC Address: {net_config['MacAddress']}")
        
        # Mounts/volumes
        print("\nMounts:")
        for mount in container.attrs['Mounts']:
            print(f"  Source: {mount['Source']}")
            print(f"  Destination: {mount['Destination']}")
            print(f"  Mode: {mount['Mode']}")
            print("  " + "-" * 30)
        
        # Environment variables
        print("\nEnvironment Variables:")
        for env in container.attrs['Config']['Env']:
            print(f"  {env}")
            
        return container_attrs
        
    except docker.errors.NotFound:
        print(f"Container {container_name_or_id} not found")
    except docker.errors.APIError as e:
        print(f"Docker API error: {e}")

# Usage
container_info = inspect_container("be977b1dfc14")