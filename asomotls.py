	
import datasource
    
class AsomoTools:
	''' This class provides an interface to deal with the shhet objects
		returned by xlrd, '''
	
	# our two data containers now just sheets
   	#mapa_list = []
   	#cmpr_list = []
	
	# set the diference list to be identical to the 
	# generetad campare list and get ready to pop this out
	#dif_list= None
	
	# will have the Files objects
	##data = None
	
	def __init__(self):
		''' inxtaciate the Files object to our data atribute '''
		##global datasource
		self.data = datasource.Files()
		self.dif_list= []
		self.mapa_list = []
		self.cmpr_list = []
		self.format_list = []
		
	def load_mapa_sheet_list(self):
		''' iterate throught the map 'sheet' and later
			we will try with the intire book '''
			
		# we are only interested only in col 0 & 1 for now
		for rx in range(self.data.mapa_sheet.nrows):
			ky = self.data.mapa_sheet.cell(rx, 1).value
			vl = self.data.mapa_sheet.cell(rx, 0).value
			self.mapa_list.append({ky :vl})
			
	def load_cmpr_sheet_list(self):
		''' iterate throught the compare 'sheet' and later
			we will try with the intire book '''
			
		# only col 0 & 1 will be used at all luckily the downloaded
		# campare sheets are uniformly formated
		for rx in range(self.data.cmpr_sheet.nrows):
			ky = self.data.cmpr_sheet.cell(rx, 1).value
			vl = self.data.cmpr_sheet.cell(rx, 0).value
			self.cmpr_list.append({ky :vl})
		
#	def gen_dif_list(self):
#		''' spot items that are on the campare list and in the map list
#			and get them out of the difference list '''
#		for el in self.cmpr_list:
#			for il in self.mapa_list:
#				found=0
#				if el == il:
#					found=1
#				else:
#					pass
#				if found:
#					self.dif_list.remove(el)
					
	def gen_dif_list(self):
		for el in self.cmpr_list:
			if el not in self.mapa_list:
				self.dif_list.append(el)
			
	def display_results(self):
		''' iterate through a lisy of dictionaries
   			used to display the difference list '''
		for el in self.dif_list:
			for ky, vl in el.iteritems():
				self.format_list.append(ky + " ---> " + vl)
		
		self.format_list.sort()
		
		for el in self.format_list:
			print el
