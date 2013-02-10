
#
# Copyright (c) 2013 Jonathan Topf
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#


import maya.cmds as cmds
import maya.mel as mel

shelf_name = 'jt_tools'
main_shelf_parent = 'MayaWindow|toolBar2|MainShelfLayout|formLayout14|ShelfLayout'
button_list = []

#--------------------------------------------------------------------------------------------------
# jt_autorig.
#--------------------------------------------------------------------------------------------------
button_list.append(['jt_autorig', 'jt_autorig.png', 'python', """
import jt_autorig
reload(jt_autorig)
jt_autorig.load_ui()
"""])

#--------------------------------------------------------------------------------------------------
# jt_jitter.
#--------------------------------------------------------------------------------------------------
button_list.append(['jt_jitter', 'jt_jitter.png', 'python', """
import maya.cmds as cmds
selection = cmds.ls(sl=True)
if selection:    
    jitter_deformer = cmds.deformer(selection[0], type='jt_jitter')[0]
    cmds.connectAttr('time1.outTime', jitter_deformer + '.seed')
else:
    cmds.warning('nothing selected')
"""])

#--------------------------------------------------------------------------------------------------
# jt_ctl_curve
#--------------------------------------------------------------------------------------------------
button_list.append(['jt_ctl_curve', 'jt_ctl_curve.png', 'python', """
import jt_ctl_curve
reload(jt_ctl_curve)
jt_ctl_curve.load_ui()
"""])

#--------------------------------------------------------------------------------------------------
# jt_weight_slider.
#--------------------------------------------------------------------------------------------------
button_list.append(['jt_weight_slider', 'jt_weight_slider.png', 'python', """
import jt_weight_slider
reload(jt_weight_slider)
jt_weight_slider.load_ui()
"""])

#--------------------------------------------------------------------------------------------------
# jt_pass_through_bs.
#--------------------------------------------------------------------------------------------------
button_list.append(['jt_pass_through_bs', 'jt_pass_through_bs.png', 'python', """
import jt_pass_through_bs
reload(jt_pass_through_bs)
jt_pass_through_bs.load_ui()
"""])

#--------------------------------------------------------------------------------------------------
# jt_locator_at_selection.
#--------------------------------------------------------------------------------------------------
button_list.append(['jt_locator_at_selection', 'jt_locator_at_selection.png', 'python', """
import jt_locator_at_selection
reload(jt_locator_at_selection)
jt_locator_at_selection.create()
"""])


def add_shelf_buton(shelf_name, button_name, icon, type, command):

    print icon
    cmds.shelfButton(button_name, p=shelf_name, i=icon, c=command, stp=type)


def populate_shelf(shelf_name, button_list):
    for button in button_list:
        add_shelf_buton(shelf_name, button[0], button[1], button[2], button[3])


def create_shelf(shelf_name):

    if cmds.shelfLayout(shelf_name, exists=True, q=True):
        cmds.deleteUI(shelf_name)
    
    cmds.setParent(main_shelf_parent)
    cmds.shelfLayout(shelf_name)
    # cmds.saveAllShelves(main_shelf_parent)

    populate_shelf(shelf_name, button_list)

    # fix stupid maya error with shelves generated via python
    top_level_shelf = mel.eval('string $m = $gShelfTopLevel')
    shelves = cmds.shelfTabLayout(top_level_shelf, query=True, tabLabelIndex=True)
    for index, shelf in enumerate(shelves):
        cmds.optionVar(stringValue=('shelfName%d' % (index+1), str(shelf)))





