
import os
import xlrd

class Files:
	''' this class handels the xls files loading and provides
		an interface for xlrd '''
	# initialize our two books
	mapa_book = None
	cmpr_book = None
	
	# this is to be used for multisheet books
   	n_of_mapa_sheets = None
   	n_of_cmpr_sheets = None
   	
   	# lets get one sheet each for now
   	mapa_sheet = None
   	cmpr_sheet = None
   	
   	def __init__(self):
   		''' initialize our object's atributes '''
   		#self.mapa_book, self.cmpr_book = 
   		self.get_books()
   		#self.mapa_sheet, self.cmpr_sheet = 
   		self.get_sheets()
   		
   		# these are going to be needed for multisheet books
   		self.n_of_mapa_sheets = self.mapa_book.nsheets
   		self.n_of_cmpr_sheets = self.cmpr_book.nsheets
   		
   	
	def get_books(self):
		''' get xlrd.book objects from the two xls files '''
		self.mapa_book = xlrd.open_workbook(
                "/home/med/Desktop/asomo/canarias/correc/r.mapa.xls"
                )
   		self.cmpr_book = xlrd.open_workbook(
                "/home/med/Desktop/asomo/canarias/correc/r.cmpr.xls")
   		# return mapa, cmpr
   		
   	def get_sheets(self):
   		''' get sheet objects our main toy, now only index 0 is used '''
   		self.mapa_sheet = self.mapa_book.sheet_by_index(0)
   		self.cmpr_sheet = self.cmpr_book.sheet_by_index(0)
   		#return mapa, cmpr
   		
   	
