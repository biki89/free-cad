#***************************************************************************
#*                                                                         *
#*   Copyright (c) 2012                                              *  
#*   Daniel Falck <ddfalck@gmail.com>                                      *  
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   This program is distributed in the hope that it will be useful,       *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Library General Public License for more details.                  *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with this program; if not, write to the Free Software   *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************


class CNCWorkbench (Workbench ):
    """CNC module. Here toolbars & icons are placed. """
    from utils import Paths
    import CNCGui
    from machining_ops import profile_op1 as profile
#    import newTab3
#    from newTab3 import runTab

    Icon = Paths.iconsPath() + "/end_mill.xpm"
#    Icon = Paths.iconsPath() + "/end_mill.png"
#    Icon = Paths.iconsPath() + "/Ico.png"
    MenuText = "CNC Machining"
    ToolTip = "A CNC programming workbench using python libs"
#    MenuText = str(Translator.translate("CNC Workbench"))
#    ToolTip = str(Translator.translate("CNC Workbench"))

#    profile = Paths.modulePath() + "/machining_ops/"
#    import profile

    def Initialize(self):

        FreeCAD.Console.PrintWarning("Nothing is set up yet\n")
        # run self-tests
        depsOK = False
        try:
            from pivy import coin
            if FreeCADGui.getSoDBVersion() != coin.SoDB.getVersion():
                raise AssertionError("FreeCAD and Pivy use different versions of Coin. This will lead to unexpected behaviour.")
        except AssertionError:
            FreeCAD.Console.PrintWarning("Error: FreeCAD and Pivy use different versions of Coin. This will lead to unexpected behaviour.\n")
        except ImportError:
            FreeCAD.Console.PrintWarning("Error: Pivy not found, CNC workbench will be disabled.\n")
        except:
            FreeCAD.Console.PrintWarning("Error: Unknown error while trying to load Pivy\n")
        else:
            try:
                from PySide import QtGui,QtCore
            except ImportError:
                FreeCAD.Console.PrintWarning("Error: PySide not found, Draft workbench will be disabled.\n")
            else:
                depsOK = True

        if depsOK:
            FreeCAD.Console.PrintMessage("everything checked out ok\n")


    def Activated(self):
#        self.tab = self.getComboView(self.getMainWindow())
#        self.tab2=QtGui.QDialog()
#        self.tab.addTab(self.tab2,"A Special Tab")
#        self.tab2.show()
        FreeCAD.Console.PrintMessage("It's alive!!!!!\n")
        self.profile.createTask()



    def Deactivated(self):
#        tab = getComboView(getMainWindow())
#        tab.removeTab(2)
        FreeCAD.Console.PrintMessage("One of our 'red shirts' on the planet surface is dead Jim!\n")

#    def ContextMenu(self, recipient):
#        if (recipient == "View"):
#            if (FreeCAD.activeCNCCommand == None):
#                if (FreeCADGui.Selection.getSelection()):
#                    self.appendContextMenu("CNC",self.cmdList+self.modList)
#                    self.appendContextMenu("Display options",self.treecmdList)
#                else:
#                    self.appendContextMenu("CNC",self.cmdList)
#            else:
#                if (FreeCAD.activeCNCCommand.featureName == "Profile"):
#                    self.appendContextMenu("",self.profile)
#        else:
#            if (FreeCADGui.Selection.getSelection()):
#                self.appendContextMenu("Display options",self.treecmdList)



Gui.addWorkbench(CNCWorkbench())
