from rest_framework import permissions


class IsStaffEditorPermissions(permissions.DjangoModelPermissions):

    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    def has_permission(self, request, view):
        user = request.user 
        print(user.username)
        if not user.is_staff:
            return False
        
        return super().has_permission(request, view)


    # This is for checking user permissions manually 
    # def has_permission(self, request, view):
    #     user = request.user
    #     if user.is_staff:
    #         print(user.get_all_permissions())
    #         if user.has_perm("products.view_product"):
    #             return True
    #         if user.has_perm("products.change_product"):
    #             return True
    #         if user.has_perm("product.add_product"):
    #             return True
    #         return False

    #     return False