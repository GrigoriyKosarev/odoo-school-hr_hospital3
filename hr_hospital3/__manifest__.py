{
    'name': "Hospital",

    'summary': """
        Module hospital. Data clients.
    """,

    'license': 'OPL-1',

    'author': "grigoriykosarev@gmail.com",
    'website': "http://www.grigoriy-kosarev.com",

    'category': 'Uncategorized',
    'version': '15.0.1.0.0',

    'depends': [
        'base',
    ],

    'external_dependencies': {'python': [], },

    'data': [
        'security/ir.model.access.csv',
        'views/hs3_hospital_menu.xml',
        'views/patient_views.xml',
        'views/doctor_views.xml',
        'views/diagnosis_views.xml',
        'views/disease_views.xml',
        'views/disease_type_views.xml',
    ],

    'demo': [
    ],
}
