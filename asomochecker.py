
import asomotls
"""	
class App:
		
	main = None
		
	def __init__(self):
		self.main = Asomotools()
		
	def start(self):
		self.main.load_cmpr_sheet_list()
		self.main.load_mapa_sheet_list()
		self.main.gen_dif_list()
		self.main.display_results()
		
"""
def start():
	main = asomotls.AsomoTools()
	main.load_cmpr_sheet_list()
	main.load_mapa_sheet_list()
	main.gen_dif_list()
	main.display_results()
