from ui import Console
from service import Service

if __name__ == '__main__':
    service = Service()
    console = Console(service)
    console.run()