# -*- coding: utf-8 -*-
{
    "name": "icon_picker_widget",
    "description": """
        Long description of module's purpose
    """,
    "author": "My Company",
    "website": "https://www.yourcompany.com",
    "category": "Uncategorized",
    "version": "17.0.0.1",
    # any module necessary for this one to work correctly
    "depends": ["base"],
    "assets": {
        # "web.assets_frontend": [
            
        # ],
        "web.assets_backend": [
            "icon_picker_widget/static/src/libs/fontawesome/css/*.css",
            "icon_picker_widget/static/src/js/icon_picker_widget.js",
            "icon_picker_widget/static/src/css/icon_picker_widget.css",
            "icon_picker_widget/static/src/xml/icon_picker_widget.xml",
        ],
    },
    "license": "LGPL-3",
    "installable": True,
    "auto_install": False,
    "application": False,
}
