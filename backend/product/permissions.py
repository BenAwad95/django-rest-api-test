from rest_framework import permissions


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        print('This list of permissions')
        print(user.get_all_permissions())
        if user.is_staff:
            if user.has_perm('product.view_product'):
                return True
            return False
        return False