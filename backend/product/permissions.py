from rest_framework import permissions


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    #! This dict cover everythings you needs, you do not need for any of settings.
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
    # def has_permission(self, request, view):
    #     user = request.user
    #     print('This list of permissions')
    #     print(user.get_all_permissions())
    #     if user.is_staff:
    #         if user.has_perm('product.view_product'):
    #             return True
    #         return False
    #     return False