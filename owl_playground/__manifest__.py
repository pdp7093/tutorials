{
    'name':'Owl Playground',
    'version':'1.0',
    'category':'Learning',
    'depends':['web'],
    'data':[
        'views/assets.xml',
    ],
    'assets':{
        'web.assets_backend':[
            'owl_playground/static/src/js/hello_component.js',
            'owl_playground/static/src/xml/hello_component.xml',
        ],
    },
    'installable':True,
    'application':False,
}