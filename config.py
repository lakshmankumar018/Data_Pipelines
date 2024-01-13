import os

database_details = {
    'dev':{
        'source_database':{
            'DB_TYPE':'mysql',
            'DB_HOST':'localhost',
            'DB_PORT':'3306',
            'DB_NAME':'lakshman',
            #'DB_USER':'root',
            'DB_USER':os.environ.get('SOURCE_DB_USER'),
            'DB_PASS':os.environ.get('SOURCE_DB_PASS')
            #'DB_PASS':'root@6666'

        },
'target_database':{
            'DB_TYPE':'mysql',
            'DB_HOST': 'localhost',
            'DB_PORT': '3306',
            'DB_NAME':'datapipeline_test',
            #'DB_USER':'root',
            #'DB_PASS':'root@6666'
            'DB_USER':os.environ.get('TARGET_DB_USER'),
            'DB_PASS':os.environ.get('TARGET_DB_PASS')

        }
    }
}