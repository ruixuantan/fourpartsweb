from fourpartsweb.app import create_celery_app

celery = create_celery_app()


@celery.task(name="clean_db")
def clean_db():
    print('CELERY UP')
