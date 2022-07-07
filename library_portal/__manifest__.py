{
    "name": "Library Portal",
    "discription": "Portal for library members",
    "author": "Mikola Ostroukh",
    "license": "AGPL-3",
    "depends": ["library_checkout", "portal"],
    "data": [
        "security/ir.model.access.csv",
        "security/library_security.xml",
        "views/main_templates.xml",
        "views/portal_templates.xml",
    ],
    "assets": {
        "web.assets_frontend": {
            "library_portal/static/src/css/library.css",
        }
    }
}