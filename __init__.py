'''
Copyright (C) 2018 Samy Tichadou
samytichadou@gmail.com
mydreamart6@gmail.com

Created by Samy Tichadou (tonton)
Updated By Alex Paul(My Dream Art)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

bl_info = {
    "name": "Smart Config",
    "description": "Save your Blender configuration, including installed addons",
    "author": "Samy Tichadou (tonton), Alex Paul(Update)",
    "version": (2, 0, 0),
    "blender": (2, 83, 0),
    "location": "Import-Export Menus",
    "wiki_url": "https://github.com/samytichadou/SMART-CONFIG_blender_addon/tree/v0.1",
    "tracker_url": "https://github.com/samytichadou/SMART-CONFIG_blender_addon/issues/new",  
    "category": "Import-Export" }

import bpy


# load and reload submodules
##################################

import importlib
from . import developer_utils
importlib.reload(developer_utils)
modules = developer_utils.setup_addon_modules(__path__, __name__, "bpy" in locals())

# from .export_function import smart_config_menu_export_config
from .export_function import SmartConfig_Export
from .addon_prefs import SmartConfig_AddonPrefs

# from .import_function import smart_config_menu_import_config    
from .import_function import SmartConfig_Import    


# register
##################################

import traceback

class TODOTASK_PT_NPanel(bpy.types.Panel):
    bl_idname = "Smart Config"
    bl_category = "Smart Config"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "SC Functions"

    def draw(self, context):
        self.layout.operator('smartconfig.import_config', text="Import Configuration (.sc)", icon='NONE')
        self.layout.operator('smartconfig.export_config', text="Export Configuration (.sc)", icon='NONE')

# class
###################################

classes = [SmartConfig_Export,
            SmartConfig_Import,
            SmartConfig_AddonPrefs,
            TODOTASK_PT_NPanel
            ]


def register():
    try:
        for cls in classes:
            bpy.utils.register_class(cls)
    except: traceback.print_exc()

    print("Registered {} with {} modules".format(bl_info["name"], len(modules)))
    
    # bpy.types.TOPBAR_HT_upper_bar.append(smart_config_menu_export_config)
    # bpy.types.TOPBAR_HT_upper_bar.append(smart_config_menu_import_config)

def unregister():
    
    try:
        for cls in classes:
            bpy.utils.unregister_class(cls)
    except: traceback.print_exc()

    print("Unregistered {}".format(bl_info["name"]))

    # bpy.types.TOPBAR_HT_upper_bar.remove(smart_config_menu_export_config)
    # bpy.types.TOPBAR_HT_upper_bar.remove(smart_config_menu_import_config)