from rest_framework import permissions
from .permissions import IsStaffEditorPermissions


class StaffEditorPermissionMixins():
    permissions_classes  = [permissions.IsAdminUser, IsStaffEditorPermissions]