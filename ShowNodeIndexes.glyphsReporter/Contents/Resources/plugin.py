# encoding: utf-8

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


from GlyphsApp.plugins import *
from GlyphsApp import OFFCURVE

class ShowNodeIndexes(ReporterPlugin):

	def settings(self):
		self.menuName = Glyphs.localize({
			'en': u'Node Indexes',
			'de': u'Indexnummern',
			'nl': u'Indexgetallen'
		})
		self.generalContextMenus = [
			{'name': Glyphs.localize({
				'en': u'Toggle Display of BCP Indexes',
				'de': u'Anfasser-Indexnummern ein/ausblenden',
				'nl': u'Indexgetallen voor BCPs in/uitschakelen'
			}), 'action': self.toggleBCPs},
		]
		NSUserDefaults.standardUserDefaults().registerDefaults_({
			"com.mekkablue.ShowNodeIndexes.displayBCPs": True
		})
					
		
	def foreground(self, layer):
		displayBCPs = Glyphs.defaults["com.mekkablue.ShowNodeIndexes.displayBCPs"]
		for thisPath in layer.paths:
			for i in range(len(thisPath.nodes)):
				thisNode = thisPath.nodes[i]
				if thisNode.type != OFFCURVE or displayBCPs:
					self.drawTextAtPoint("%i"%i, thisNode.position, fontColor=NSColor.brownColor())
	
	def toggleBCPs(self):
		Glyphs.defaults["com.mekkablue.ShowNodeIndexes.displayBCPs"] = not Glyphs.defaults["com.mekkablue.ShowNodeIndexes.displayBCPs"]

