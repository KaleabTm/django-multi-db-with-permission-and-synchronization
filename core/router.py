# core/routers.py
class MultiDBRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'user_and_org':
            return 'user_org'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'user_and_org':
            return 'user_org'
        return 'default'

    def allow_migrate(self, db, app_label, **hints):
        return db == 'default'
