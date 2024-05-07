'''
# Define a router for the Product model
class ProductRouter:
    def db_for_read(self, model, **hints):
        if model.meta.app.label == 'Product':
            return 'products_db'
        return None

    def db_for_write(self, model, **hints):
        if model.meta.app.label == 'Product':
            return 'products_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'Product' and obj2._meta.app_label == 'Product':
            return True

        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app.label == 'Product':
            return 'products_db'
        return None 
'''