from models.component import ComponentModel

cpus = [
    ComponentModel(category="CPU", brand="AMD", name="Ryzen 5 3600", price=80, socket="AM4"),
    ComponentModel(category="CPU", brand="AMD", name="Ryzen 5 5600X", price=148, socket="AM4"),
    ComponentModel(category="CPU", brand="AMD", name="Ryzen 7 5700X", price=194, socket="AM4"),
    ComponentModel(category="CPU", brand="AMD", name="Ryzen 7 5800X3D", price=330, socket="AM4"),
    ComponentModel(category="CPU", brand="AMD", name="Ryzen 9 5900X", price=255, socket="AM4"),
    ComponentModel(category="CPU", brand="AMD", name="Ryzen 5 7600X", price=172, socket="AM5"),
    ComponentModel(category="CPU", brand="AMD", name="Ryzen 7 7700X", price=217, socket="AM5"),
    ComponentModel(category="CPU", brand="AMD", name="Ryzen 7 7800X3D", price=389, socket="AM5"),
    ComponentModel(category="CPU", brand="AMD", name="Ryzen 5 9600X", price=174, socket="AM5"),
    ComponentModel(category="CPU", brand="AMD", name="Ryzen 7 9700X", price=339, socket="AM5"),
    ComponentModel(category="CPU", brand="AMD", name="Ryzen 7 9800X3D", price=444, socket="AM5"),
    ComponentModel(category="CPU", brand="AMD", name="Ryzen 9 9950X", price=549, socket="AM5"),
]

motherboards = [
    ComponentModel(category="Motherboard", brand="MSI", name="MAG B550 Tomahawk", price=140, socket="AM4", memory_type="DDR4", form_factor="ATX"),
    ComponentModel(category="Motherboard", brand="Gigabyte", name="B550M AORUS Elite", price=134, socket="AM4", memory_type="DDR4", form_factor="Micro-ATX"),
    ComponentModel(category="Motherboard", brand="Gigabyte", name="B550I AORUS Pro AX", price=209, socket="AM4", memory_type="DDR4", form_factor="Mini-ITX"),
    ComponentModel(category="Motherboard", brand="MSI", name="MAG B650 Tomahawk WiFi", price=189, socket="AM5", memory_type="DDR5", form_factor="ATX"),
    ComponentModel(category="Motherboard", brand="MSI", name="MAG X870 Tomahawk WiFi", price=220, socket="AM5", memory_type="DDR5", form_factor="ATX"),
    ComponentModel(category="Motherboard", brand="Gigabyte", name="B650M AORUS Elite AX", price=130, socket="AM5", memory_type="DDR5", form_factor="Micro-ATX"),
    ComponentModel(category="Motherboard", brand="ASUS", name="ROG Strix B650E-I Gaming WiFi", price=380, socket="AM5", memory_type="DDR5", form_factor="Mini-ITX"),
]

mmemory = [
    ComponentModel(category="RAM", brand="Corsair", name="Vengeance LPX 16GB (2x8GB) DDR4-3200", price=123, memory_type="DDR4"),
    ComponentModel(category="RAM", brand="G.Skill", name="Ripjaws V 32GB (2x16GB) DDR4-3600", price=265, memory_type="DDR4"),
    ComponentModel(category="RAM", brand="Corsair", name="Vengeance 32GB (2x16GB) DDR5-6000", price=440, memory_type="DDR5"),
    ComponentModel(category="RAM", brand="G.Skill", name="Trident Z5 RGB 32GB (2x16GB) DDR5-6000", price=588, memory_type="DDR5"),
    ComponentModel(category="RAM", brand="Kingston", name="FURY Beast 32GB (2x16GB) DDR5-5600", price=630, memory_type="DDR5"),
]

gpus = [
    ComponentModel(category="GPU", brand="Gigabyte", name="GeForce RTX 2060 Mini ITX OC", price=339, gpu_length=170),
    ComponentModel(category="GPU", brand="NVIDIA", name="GeForce RTX 2070 SUPER Founders Edition", price=165, gpu_length=267),
    ComponentModel(category="GPU", brand="NVIDIA", name="GeForce RTX 2080 Ti Founders Edition", price=275, gpu_length=267),
    ComponentModel(category="GPU", brand="MSI", name="GeForce RTX 3060 Aero ITX OC", price=503, gpu_length=172),
    ComponentModel(category="GPU", brand="NVIDIA", name="GeForce RTX 3070 Founders Edition", price=250, gpu_length=242),
    ComponentModel(category="GPU", brand="NVIDIA", name="GeForce RTX 3080 Founders Edition", price=350, gpu_length=285),
    ComponentModel(category="GPU", brand="MSI", name="GeForce RTX 4060 Aero ITX OC", price=330, gpu_length=167),
    ComponentModel(category="GPU", brand="NVIDIA", name="GeForce RTX 4070 Founders Edition", price=765, gpu_length=244),
    ComponentModel(category="GPU", brand="NVIDIA", name="GeForce RTX 4080 Founders Edition", price=1074, gpu_length=304),
    ComponentModel(category="GPU", brand="ASUS", name="ROG Strix GeForce RTX 4090 OC", price=3099, gpu_length=358),
    ComponentModel(category="GPU", brand="MSI", name="GeForce RTX 5060 Ventus 2X OC", price=470, gpu_length=197),
    ComponentModel(category="GPU", brand="NVIDIA", name="GeForce RTX 5070 Founders Edition", price=849, gpu_length=242),
    ComponentModel(category="GPU", brand="NVIDIA", name="GeForce RTX 5080 Founders Edition", price=1654, gpu_length=304),
    ComponentModel(category="GPU", brand="NVIDIA", name="GeForce RTX 5090 Founders Edition", price=4999, gpu_length=304),
    ComponentModel(category="GPU", brand="Sapphire", name="Pulse Radeon RX 5600 XT", price=115, gpu_length=254),
    ComponentModel(category="GPU", brand="AMD", name="Radeon RX 5700 XT 50th Anniversary", price=150, gpu_length=272),
    ComponentModel(category="GPU", brand="ASRock", name="Radeon RX 6600 Challenger ITX", price=235, gpu_length=179),
    ComponentModel(category="GPU", brand="AMD", name="Radeon RX 6700 XT", price=300, gpu_length=267),
    ComponentModel(category="GPU", brand="AMD", name="Radeon RX 6800 XT", price=700, gpu_length=267),
    ComponentModel(category="GPU", brand="AMD", name="Radeon RX 7600", price=340, gpu_length=204),
    ComponentModel(category="GPU", brand="AMD", name="Radeon RX 7800 XT", price=480, gpu_length=267),
    ComponentModel(category="GPU", brand="AMD", name="Radeon RX 7900 XTX", price=1000, gpu_length=287),
    ComponentModel(category="GPU", brand="Sapphire", name="Pulse Radeon RX 9060 XT", price=520, gpu_length=240),
    ComponentModel(category="GPU", brand="Sapphire", name="Pulse Radeon RX 9070", price=740, gpu_length=280),
    ComponentModel(category="GPU", brand="Sapphire", name="Pulse Radeon RX 9070 XT", price=790, gpu_length=320),
]

storage = [
    ComponentModel(category="Storage", brand="Samsung", name="990 Pro 1TB", price=239),
    ComponentModel(category="Storage", brand="Western Digital", name="WD_Black SN850X 1TB", price=248),
    ComponentModel(category="Storage", brand="Crucial", name="P3 Plus 1TB", price=57),
    ComponentModel(category="Storage", brand="Samsung", name="870 Evo 1TB", price=328),
]

coolers = [
    ComponentModel(category="Cooler", brand="Noctua", name="NH-L9a-AM5", price=50, cooler_height=37),
    ComponentModel(category="Cooler", brand="Thermalright", name="Peerless Assassin 120 SE", price=35, cooler_height=155),
    ComponentModel(category="Cooler", brand="Noctua", name="NH-U12S", price=100, cooler_height=158),
    ComponentModel(category="Cooler", brand="Noctua", name="NH-D15", price=121, cooler_height=165),
]

power_supplies = [
    ComponentModel(category="PSU", brand="be quiet!", name="Pure Power 12 M 650W", price=95),
    ComponentModel(category="PSU", brand="Corsair", name="RM750e", price=100),
    ComponentModel(category="PSU", brand="MSI", name="MAG A750GL PCIE5", price=110),
    ComponentModel(category="PSU", brand="Corsair", name="RM850x", price=145),
]

cases = [
    ComponentModel(category="Case", brand="Cooler Master", name="MasterBox NR200", price=90, form_factor="Mini-ITX", max_gpu_length=330, max_cooler_height=155),
    ComponentModel(category="Case", brand="Fractal Design", name="North", price=140, form_factor="ATX", max_gpu_length=355, max_cooler_height=170),
    ComponentModel(category="Case", brand="NZXT", name="H5 Flow (2024)", price=85, form_factor="ATX", max_gpu_length=410, max_cooler_height=170),
]

components_list = cpus + motherboards + memory + gpus + storage + coolers + power_supplies + cases
