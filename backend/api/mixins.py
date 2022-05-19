from rest_framework import permissions
from .permissions import IsStaffEditorPermissions
from products.models import Product

class StaffEditorPermissionMixins():
    permissions_classes  = [permissions.IsAdminUser, IsStaffEditorPermissions]


class ProductdQuerySetMixins():
    def get_queryset(self, *args, **kwargs):
        qs = Product.objects.all()        
        request = self.request
        user = request.user        
        user_qs = qs.filter(user=user)
        if user.is_staff:
            return qs
            
        return user_qs
