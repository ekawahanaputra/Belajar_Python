class Service:
    jumlah_menu = 1   # Disebut class variable - variable milik class Service

    def __init__(self,Type, service_1K, service_10K, service_20K, service_30K, service_40K, service_50K):
        Type : type_Vehicle
        self.pertama : service_1K
        self.kedua : service_20K
        self.ketiga : service_10K
        self.keempat : service_30K
        self.kelima : service_40K
        self.keenam : service_50K           # Disebut Instance Variable - variable milik object
        Service.jumlah_menu += 1            # Deklarasi class variable
        
        print ("Harga service 50K ", Type, " adalah", service_50K, '\n')

print ('Daftar harga jasa\n')
print ('No ', Service.jumlah_menu)
Service_Agya = Service ('Agya', 'free', 'free service', 'Rp 500.000', 'Rp 600.000', 'Rp 650.000','700.000')

print ('No ', Service.jumlah_menu)
Service_Calya = Service ('Calya', 'free', 'free service', 'Rp 550.000', 'Rp 650.000', 'Rp 700.000', '750.000')

print ('No ', Service.jumlah_menu)
Service_Avanza = Service ('Avanza', 'free', 'free service', 'Rp 700.000', 'Rp 750.000', 'Rp 800.000','850.000')

