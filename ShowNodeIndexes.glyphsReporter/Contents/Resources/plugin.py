# encoding: utf-8
from __future__ import division, print_function, unicode_literals

###########################################################################################################
#
#
#	Reporter Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Reporter
#
#
###########################################################################################################

import objc
from GlyphsApp import *
from GlyphsApp.plugins import *

class ShowNodeIndexes(ReporterPlugin):

	@objc.python_method
	def settings(self):
		self.menuName = Glyphs.localize({
			'en': 'Node Indexes',
			'es': 'listado de nodos',
			'de': 'Indexnummern',
			'fr': 'numéros de nœuds',
			'nl': 'Indexgetallen',
		})
		self.generalContextMenus = [
			{'name': Glyphs.localize({
				'en': 'Toggle Display of BCP Indexes',
				'es': 'Mostrar/ocultar listado de manejadores',
				'de': 'Anfasser-Indexnummern ein/ausblenden',
				'fr': 'Afficher/masquer les numéros des poignées',
				'nl': 'Indexgetallen voor BCPs in/uitschakelen',
			}), 'action': self.toggleBCPs},
		]
		Glyphs.registerDefault( "com.mekkablue.ShowNodeIndexes.displayBCPs", True )
	
	@objc.python_method
	def foreground(self, layer):
		displayBCPs = Glyphs.defaults["com.mekkablue.ShowNodeIndexes.displayBCPs"]
		for thisPath in layer.paths:
			for i in range(len(thisPath.nodes)):
				thisNode = thisPath.nodes[i]
				if thisNode.type != OFFCURVE or displayBCPs:
					self.drawTextAtPoint("%i"%i, thisNode.position, fontColor=NSColor.brownColor())
	
	def toggleBCPs(self):
		Glyphs.defaults["com.mekkablue.ShowNodeIndexes.displayBCPs"] = not Glyphs.defaults["com.mekkablue.ShowNodeIndexes.displayBCPs"]

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
