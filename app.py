from crystalpayio import CrystalPayIO
from config import LOGIN, SECRET


signature = CrystalPayIO.signature("test")
print(signature)
        

