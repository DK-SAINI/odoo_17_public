# -*- coding: utf-8 -*-
{
    "name": "Owl Framework",
    "summary": "Short (1 phrase/line) summary of the module's purpose",
    "author": "Dk Company",
    "website": "https://www.yourcompany.com",
    "version": "17.0.0.1",
    "depends": ["base"],
    "data": [
        # 'security/ir.model.access.csv',
        "views/menu.xml",
    ],
    "assets": {
        # 'web.assets_frontend': {
        # },
        "web.assets_backend": {
            "/owl_framework/static/src/component/*/*.js",
            "/owl_framework/static/src/component/*/*.xml",
            "/owl_framework/static/src/component/*/*.css",
        },
    },
}
